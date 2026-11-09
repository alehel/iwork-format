#![forbid(unsafe_code)]
#![deny(
    clippy::unwrap_used,
    clippy::expect_used,
    clippy::panic,
    clippy::unimplemented,
    clippy::todo,
    clippy::unreachable
)]

use std::io::{self, Write};
use std::path::Path;
use std::process::ExitCode;

use iwork_probe::{crypt, hex, iwa, package::Package, proto, text};

const USAGE: &str = "\
usage:
  iwork-probe list <file>
  iwork-probe hex <file> <part> [--decoded] [--offset N] [--len N]
  iwork-probe proto <file> <part> [--decoded] [--offset N] [--len N] [--depth N]
  iwork-probe chunks <file> <part>
  iwork-probe records <file> <part>
  iwork-probe refs <file> <part>
  iwork-probe text <file>

<file> is a document: a ZIP file or a folder package. Every command takes
--password P to read a password-protected document; its parts are decrypted as
they're read (experiments 0179 and 0180). `list` shows them as stored.
--decoded works on an .iwa part's decoded bytes instead of its stored ones; the offsets
that `chunks` and `records` print are offsets into those decoded bytes.
N may be decimal or 0x-prefixed hexadecimal.";

/// How deep `proto` nests into length-delimited values by default.
const DEFAULT_DEPTH: usize = 16;
/// How many bytes `hex` shows by default.
const DEFAULT_HEX_LEN: usize = 256;

fn main() -> ExitCode {
    let args: Vec<String> = std::env::args().skip(1).collect();
    match run(&args) {
        Ok(()) => ExitCode::SUCCESS,
        Err(e) => {
            let _ = writeln!(io::stderr(), "iwork-probe: {e}");
            ExitCode::FAILURE
        }
    }
}

/// Positional arguments and `--name value` options.
struct Args<'a> {
    positional: Vec<&'a str>,
    offset: usize,
    len: Option<usize>,
    depth: usize,
    decoded: bool,
    password: Option<&'a str>,
}

fn number(text: &str) -> Result<usize, String> {
    let parsed = match text.strip_prefix("0x") {
        Some(hex) => usize::from_str_radix(hex, 16),
        None => text.parse(),
    };
    parsed.map_err(|_| format!("{text:?} is not a number"))
}

fn parse(args: &[String]) -> Result<Args<'_>, String> {
    let mut parsed =
        Args { positional: Vec::new(), offset: 0, len: None, depth: DEFAULT_DEPTH, decoded: false, password: None };
    let mut iter = args.iter();
    while let Some(arg) = iter.next() {
        let mut value = || iter.next().ok_or_else(|| format!("{arg} needs a value")).and_then(|v| number(v));
        match arg.as_str() {
            "--offset" => parsed.offset = value()?,
            "--len" => parsed.len = Some(value()?),
            "--depth" => parsed.depth = value()?,
            "--decoded" => parsed.decoded = true,
            "--password" => parsed.password = Some(iter.next().ok_or("--password needs a value")?.as_str()),
            other if other.starts_with("--") => return Err(format!("unknown option {other}\n\n{USAGE}")),
            other => parsed.positional.push(other),
        }
    }
    Ok(parsed)
}

/// The slice `args` selects from a part's bytes.
fn window<'a>(bytes: &'a [u8], args: &Args<'_>, default_len: Option<usize>) -> Result<&'a [u8], String> {
    let rest = bytes
        .get(args.offset..)
        .ok_or_else(|| format!("offset {} is past the end of the part ({} bytes)", args.offset, bytes.len()))?;
    let len = args.len.or(default_len).unwrap_or(rest.len()).min(rest.len());
    Ok(rest.get(..len).unwrap_or(rest))
}

fn run(raw: &[String]) -> Result<(), String> {
    let args = parse(raw)?;
    let text = match args.positional.as_slice() {
        ["list", file] => list(file)?,
        ["hex", file, part] => {
            let bytes = read_maybe_decoded(file, part, &args)?;
            hex::dump(window(&bytes, &args, Some(DEFAULT_HEX_LEN))?, args.offset)
        }
        ["proto", file, part] => {
            let bytes = read_maybe_decoded(file, part, &args)?;
            proto::render(window(&bytes, &args, None)?, args.depth).map_err(|e| e.to_string())?
        }
        ["chunks", file, part] => chunks(file, part, &args)?,
        ["records", file, part] => records(file, part, &args)?,
        ["refs", file, part] => refs(file, part, &args)?,
        ["text", file] => texts(file, &args)?,
        _ => return Err(USAGE.to_string()),
    };
    let mut out = io::stdout().lock();
    match out.write_all(text.as_bytes()).and_then(|()| out.flush()) {
        // A closed pipe (piping into `head`) isn't an error worth reporting.
        Err(e) if e.kind() != io::ErrorKind::BrokenPipe => Err(e.to_string()),
        _ => Ok(()),
    }
}

/// A document opened for reading, with the key to its parts if it's password-protected.
struct Document<'a> {
    file: &'a str,
    package: Package,
    key: Option<crypt::Key>,
}

impl<'a> Document<'a> {
    fn open(file: &'a str, args: &Args<'_>) -> Result<Self, String> {
        let mut package = Package::open(Path::new(file)).map_err(|e| format!("{file}: {e}"))?;
        let key = match package.read(crypt::HEADER) {
            Err(_) => None,
            Ok(header) => {
                let password = args.password.ok_or_else(|| {
                    let hint = package.read(crypt::HINT).map(|h| String::from_utf8_lossy(&h).into_owned());
                    let hint = hint.map(|h| format!(" (hint: {h:?})")).unwrap_or_default();
                    format!("{file}: the document is password-protected{hint}; give it with --password")
                })?;
                Some(crypt::key(&header, password).map_err(|e| format!("{file}: {e}"))?)
            }
        };
        Ok(Self { file, package, key })
    }

    /// A part's bytes, decrypted if the document is password-protected.
    fn read(&mut self, part: &str) -> Result<Vec<u8>, String> {
        let stored = self.package.read(part).map_err(|e| format!("{}: {e}", self.file))?;
        match &self.key {
            Some(key) if crypt::is_encrypted(part) => {
                crypt::decrypt(key, part, &stored).map_err(|e| format!("{}: {e}", self.file))
            }
            _ => Ok(stored),
        }
    }
}

fn read(file: &str, part: &str, args: &Args<'_>) -> Result<Vec<u8>, String> {
    Document::open(file, args)?.read(part)
}

/// A part's bytes, decoded from its `.iwa` chunks when `--decoded` is given.
fn read_maybe_decoded(file: &str, part: &str, args: &Args<'_>) -> Result<Vec<u8>, String> {
    let bytes = read(file, part, args)?;
    if args.decoded { decode(part, &bytes).map(|d| d.bytes) } else { Ok(bytes) }
}

fn decode(part: &str, bytes: &[u8]) -> Result<iwa::Decoded, String> {
    iwa::decode(bytes).map_err(|e| format!("{part}: {e}"))
}

fn plural(n: usize, one: &str, many: &str) -> String {
    if n == 1 { format!("1 {one}") } else { format!("{n} {many}") }
}

fn chunks(file: &str, part: &str, args: &Args<'_>) -> Result<String, String> {
    let bytes = read(file, part, args)?;
    let decoded = decode(part, &bytes)?;
    let mut out = format!(
        "{part}: {}, {} stored bytes, {} decoded bytes\n{:>10} {:>5} {:>10} {:>10} {:>10}\n",
        plural(decoded.chunks.len(), "chunk", "chunks"),
        bytes.len(),
        decoded.bytes.len(),
        "offset",
        "type",
        "stored",
        "decoded",
        "decoded at"
    );
    for c in &decoded.chunks {
        out.push_str(&format!(
            "{:>10} {:>5} {:>10} {:>10} {:>10}\n",
            c.offset, c.chunk_type, c.stored, c.decoded, c.decoded_offset
        ));
    }
    Ok(out)
}

fn records(file: &str, part: &str, args: &Args<'_>) -> Result<String, String> {
    let bytes = read(file, part, args)?;
    let decoded = decode(part, &bytes)?;
    let records = iwa::records(&decoded.bytes).map_err(|e| format!("{part}: {e}"))?;
    let mut out = format!(
        "{part}: {}, {} decoded bytes\n{:>10} {:>6} {:>10} {:>8} {:>10} {:>7}  version\n",
        plural(records.len(), "record", "records"),
        decoded.bytes.len(),
        "header",
        "hlen",
        "payload",
        "len",
        "id",
        "type"
    );
    for r in &records {
        let head = format!("{:>10} {:>6}", r.header_offset, r.header_len);
        if r.payloads.is_empty() {
            out.push_str(&format!("{head} {:>10} {:>8} {:>10} {:>7}  -\n", "-", "-", r.id, "-"));
        }
        for p in &r.payloads {
            let type_number = p.type_number.map(|t| t.to_string()).unwrap_or_else(|| "-".to_string());
            let version = p
                .version
                .as_ref()
                .map(|v| v.iter().map(u64::to_string).collect::<Vec<_>>().join("."))
                .unwrap_or_else(|| "-".to_string());
            out.push_str(&format!("{head} {:>10} {:>8} {:>10} {type_number:>7}  {version}\n", p.offset, p.len, r.id));
        }
    }
    Ok(out)
}

/// Each payload's header-listed references, one record per line.
fn refs(file: &str, part: &str, args: &Args<'_>) -> Result<String, String> {
    let bytes = read(file, part, args)?;
    let decoded = decode(part, &bytes)?;
    let records = iwa::records(&decoded.bytes).map_err(|e| format!("{part}: {e}"))?;
    let mut out = format!("{part}: {}\n", plural(records.len(), "record", "records"));
    for r in &records {
        for p in &r.payloads {
            let type_number = p.type_number.map(|t| t.to_string()).unwrap_or_else(|| "-".to_string());
            let ids: Vec<String> = p.references.iter().map(u64::to_string).collect();
            let list = if ids.is_empty() { "-".to_string() } else { ids.join(" ") };
            out.push_str(&format!("{:>10} {type_number:>7}  {list}\n", r.id));
        }
    }
    Ok(out)
}

/// Every text record in the document, part by part, with its kind and text.
fn texts(file: &str, args: &Args<'_>) -> Result<String, String> {
    let mut document = Document::open(file, args)?;
    let parts = document.package.parts().map_err(|e| format!("{file}: {e}"))?;
    let mut out = String::new();
    for part in parts.iter().filter(|p| p.name.ends_with(".iwa")) {
        let bytes = document.read(&part.name)?;
        let decoded = decode(&part.name, &bytes)?;
        let records = iwa::records(&decoded.bytes).map_err(|e| format!("{}: {e}", part.name))?;
        for t in text::texts(&decoded.bytes, &records) {
            if t.text.is_empty() {
                continue;
            }
            // Field 1's meaning is Pages': 0 for the body, 1 for headers and footers. Numbers
            // also uses 1 for a sheet's text, so the label only reports the value.
            let kind = match t.kind {
                text::Kind::Body => "field 1 = 0".to_string(),
                text::Kind::HeaderOrFooter => "field 1 = 1".to_string(),
                text::Kind::Other(n) => format!("field 1 = {n}"),
                text::Kind::Unmarked => "no field 1".to_string(),
            };
            out.push_str(&format!("== {} object {} ({kind})\n{}\n", part.name, t.id, text::readable(&t.text)));
        }
    }
    Ok(out)
}

fn list(file: &str) -> Result<String, String> {
    let mut package = Package::open(Path::new(file)).map_err(|e| format!("{file}: {e}"))?;
    let kind = match package {
        Package::Zip(_) => "ZIP file",
        Package::Folder(_, None) => "folder package",
        Package::Folder(_, Some(_)) => "folder package with Index.zip",
    };
    let parts = package.parts().map_err(|e| format!("{file}: {e}"))?;
    let count = match parts.len() {
        1 => "1 part".to_string(),
        n => format!("{n} parts"),
    };
    let mut out = format!("{file}: {kind}, {count}\n{:>12} {:>12}  name\n", "size", "stored");
    for part in parts {
        let stored = part.stored_size.map(|s| format!("{s:>12}")).unwrap_or_else(|| format!("{:>12}", "-"));
        out.push_str(&format!("{:>12} {stored}  {}\n", part.size, part.name));
    }
    Ok(out)
}
