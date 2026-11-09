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

use iwork_probe::{hex, package::Package, proto};

const USAGE: &str = "\
usage:
  iwork-probe list <file>
  iwork-probe hex <file> <part> [--offset N] [--len N]
  iwork-probe proto <file> <part> [--offset N] [--len N] [--depth N]

<file> is a document: a ZIP file or a folder package.
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
}

fn number(text: &str) -> Result<usize, String> {
    let parsed = match text.strip_prefix("0x") {
        Some(hex) => usize::from_str_radix(hex, 16),
        None => text.parse(),
    };
    parsed.map_err(|_| format!("{text:?} is not a number"))
}

fn parse(args: &[String]) -> Result<Args<'_>, String> {
    let mut parsed = Args { positional: Vec::new(), offset: 0, len: None, depth: DEFAULT_DEPTH };
    let mut iter = args.iter();
    while let Some(arg) = iter.next() {
        let mut value = || iter.next().ok_or_else(|| format!("{arg} needs a value")).and_then(|v| number(v));
        match arg.as_str() {
            "--offset" => parsed.offset = value()?,
            "--len" => parsed.len = Some(value()?),
            "--depth" => parsed.depth = value()?,
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
            let bytes = read(file, part)?;
            hex::dump(window(&bytes, &args, Some(DEFAULT_HEX_LEN))?, args.offset)
        }
        ["proto", file, part] => {
            let bytes = read(file, part)?;
            proto::render(window(&bytes, &args, None)?, args.depth).map_err(|e| e.to_string())?
        }
        _ => return Err(USAGE.to_string()),
    };
    let mut out = io::stdout().lock();
    match out.write_all(text.as_bytes()).and_then(|()| out.flush()) {
        // A closed pipe (piping into `head`) isn't an error worth reporting.
        Err(e) if e.kind() != io::ErrorKind::BrokenPipe => Err(e.to_string()),
        _ => Ok(()),
    }
}

fn read(file: &str, part: &str) -> Result<Vec<u8>, String> {
    let mut package = Package::open(Path::new(file)).map_err(|e| format!("{file}: {e}"))?;
    package.read(part).map_err(|e| format!("{file}: {e}"))
}

fn list(file: &str) -> Result<String, String> {
    let mut package = Package::open(Path::new(file)).map_err(|e| format!("{file}: {e}"))?;
    let kind = match package {
        Package::Zip(_) => "ZIP file",
        Package::Folder(_) => "folder package",
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
