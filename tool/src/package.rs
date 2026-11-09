//! Open a document as a set of named parts, whether it's a ZIP file or a folder package. Only
//! the public ZIP format is assumed here; what the parts hold is for experiments to find out.

use std::fmt;
use std::fs;
use std::io::Read;
use std::path::{Component, Path, PathBuf};

/// The largest part read into memory.
pub const MAX_PART_BYTES: u64 = 512 * 1024 * 1024;
/// The most parts a package may list.
pub const MAX_PARTS: usize = 100_000;
/// How deep a folder package is walked.
const MAX_DEPTH: usize = 32;

#[derive(Debug)]
pub enum Error {
    Io(std::io::Error),
    Zip(zip::result::ZipError),
    NotFound(String),
    BadName(String),
    TooLarge { name: String, size: u64 },
    TooManyParts,
}

impl fmt::Display for Error {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        match self {
            Self::Io(e) => write!(f, "{e}"),
            Self::Zip(e) => write!(f, "not a readable ZIP file: {e}"),
            Self::NotFound(name) => write!(f, "no part named {name:?}"),
            Self::BadName(name) => write!(f, "part name {name:?} leaves the package"),
            Self::TooLarge { name, size } => {
                write!(f, "part {name:?} is {size} bytes, over the {MAX_PART_BYTES}-byte limit")
            }
            Self::TooManyParts => write!(f, "more than {MAX_PARTS} parts"),
        }
    }
}

impl std::error::Error for Error {}

impl From<std::io::Error> for Error {
    fn from(e: std::io::Error) -> Self {
        Self::Io(e)
    }
}

impl From<zip::result::ZipError> for Error {
    fn from(e: zip::result::ZipError) -> Self {
        Self::Zip(e)
    }
}

/// One part of a package.
#[derive(Clone, Debug, PartialEq, Eq)]
pub struct Part {
    /// Its path inside the package, with `/` separators.
    pub name: String,
    /// Its size in bytes, uncompressed.
    pub size: u64,
    /// Its size inside the ZIP file; `None` in a folder package.
    pub stored_size: Option<u64>,
}

/// The ZIP file a folder package keeps its `.iwa` parts in (experiment 0076).
pub const INDEX_ZIP: &str = "Index.zip";

pub enum Package {
    Zip(zip::ZipArchive<fs::File>),
    /// A folder package, and its `Index.zip` if it has one.
    Folder(PathBuf, Option<zip::ZipArchive<fs::File>>),
}

impl Package {
    pub fn open(path: &Path) -> Result<Self, Error> {
        if fs::metadata(path)?.is_dir() {
            let index = path.join(INDEX_ZIP);
            let inner = match fs::symlink_metadata(&index) {
                Ok(meta) if meta.is_file() => Some(zip::ZipArchive::new(fs::File::open(&index)?)?),
                _ => None,
            };
            Ok(Self::Folder(path.to_path_buf(), inner))
        } else {
            Ok(Self::Zip(zip::ZipArchive::new(fs::File::open(path)?)?))
        }
    }

    /// Every part, sorted by name.
    pub fn parts(&mut self) -> Result<Vec<Part>, Error> {
        let mut parts = Vec::new();
        match self {
            Self::Zip(archive) => zip_parts(archive, &mut parts)?,
            Self::Folder(root, inner) => {
                walk(root, root, 0, &mut parts)?;
                if let Some(archive) = inner {
                    zip_parts(archive, &mut parts)?;
                }
            }
        }
        parts.sort_by(|a, b| a.name.cmp(&b.name));
        Ok(parts)
    }

    /// The bytes of the part named `name`, uncompressed.
    pub fn read(&mut self, name: &str) -> Result<Vec<u8>, Error> {
        match self {
            Self::Zip(archive) => {
                let entry = archive.by_name(name).map_err(|e| match e {
                    zip::result::ZipError::FileNotFound => Error::NotFound(name.to_string()),
                    other => Error::Zip(other),
                })?;
                read_capped(entry, name)
            }
            Self::Folder(root, inner) => {
                // A part inside Index.zip is read from there; everything else from the folder.
                if let Some(archive) = inner {
                    match archive.by_name(name) {
                        Ok(entry) => return read_capped(entry, name),
                        Err(zip::result::ZipError::FileNotFound) => {}
                        Err(other) => return Err(Error::Zip(other)),
                    }
                }
                let path = join(root, name)?;
                let meta = fs::symlink_metadata(&path).map_err(|_| Error::NotFound(name.to_string()))?;
                if !meta.is_file() {
                    return Err(Error::NotFound(name.to_string()));
                }
                read_capped(fs::File::open(path)?, name)
            }
        }
    }
}

/// Add a ZIP archive's file entries to `parts`.
fn zip_parts(archive: &mut zip::ZipArchive<fs::File>, parts: &mut Vec<Part>) -> Result<(), Error> {
    if archive.len().saturating_add(parts.len()) > MAX_PARTS {
        return Err(Error::TooManyParts);
    }
    for i in 0..archive.len() {
        let entry = archive.by_index_raw(i)?;
        if entry.is_dir() {
            continue;
        }
        parts.push(Part {
            name: entry.name().to_string(),
            size: entry.size(),
            stored_size: Some(entry.compressed_size()),
        });
    }
    Ok(())
}

/// Read at most [`MAX_PART_BYTES`], whatever size the part claims to have.
fn read_capped(reader: impl Read, name: &str) -> Result<Vec<u8>, Error> {
    let mut bytes = Vec::new();
    reader.take(MAX_PART_BYTES.saturating_add(1)).read_to_end(&mut bytes)?;
    let size = bytes.len() as u64;
    if size > MAX_PART_BYTES {
        return Err(Error::TooLarge { name: name.to_string(), size });
    }
    Ok(bytes)
}

/// `root` joined with a `/`-separated part name that must stay inside it.
fn join(root: &Path, name: &str) -> Result<PathBuf, Error> {
    let mut path = root.to_path_buf();
    for piece in Path::new(name).components() {
        match piece {
            Component::Normal(p) => path.push(p),
            Component::CurDir => {}
            _ => return Err(Error::BadName(name.to_string())),
        }
    }
    Ok(path)
}

/// List the files under `dir`, skipping symbolic links so the walk stays inside the package.
fn walk(root: &Path, dir: &Path, depth: usize, parts: &mut Vec<Part>) -> Result<(), Error> {
    if depth > MAX_DEPTH {
        return Ok(());
    }
    for entry in fs::read_dir(dir)? {
        let entry = entry?;
        let meta = fs::symlink_metadata(entry.path())?;
        if meta.is_dir() {
            walk(root, &entry.path(), depth + 1, parts)?;
        } else if meta.is_file() {
            if parts.len() >= MAX_PARTS {
                return Err(Error::TooManyParts);
            }
            let path = entry.path();
            let relative = path.strip_prefix(root).unwrap_or(&path);
            let name: Vec<String> =
                relative.components().map(|c| c.as_os_str().to_string_lossy().into_owned()).collect();
            parts.push(Part { name: name.join("/"), size: meta.len(), stored_size: None });
        }
    }
    Ok(())
}

#[cfg(test)]
mod tests {
    use super::*;
    use std::io::Write;
    use std::sync::atomic::{AtomicUsize, Ordering};

    fn scratch() -> PathBuf {
        static NEXT: AtomicUsize = AtomicUsize::new(0);
        let n = NEXT.fetch_add(1, Ordering::Relaxed);
        let dir = std::env::temp_dir().join(format!("iwork-probe-test-{}-{n}", std::process::id()));
        let _ = fs::remove_dir_all(&dir);
        fs::create_dir_all(&dir).unwrap();
        dir
    }

    #[test]
    fn a_folder_package_lists_and_reads_its_files() {
        let dir = scratch();
        fs::create_dir_all(dir.join("Data")).unwrap();
        fs::write(dir.join("Data/a.bin"), [1, 2, 3]).unwrap();
        fs::write(dir.join("top.txt"), "hi").unwrap();
        let mut pkg = Package::open(&dir).unwrap();
        let parts = pkg.parts().unwrap();
        let names: Vec<_> = parts.iter().map(|p| (p.name.as_str(), p.size)).collect();
        assert_eq!(names, vec![("Data/a.bin", 3), ("top.txt", 2)]);
        assert_eq!(pkg.read("Data/a.bin").unwrap(), vec![1, 2, 3]);
        fs::remove_dir_all(dir).unwrap();
    }

    #[test]
    fn a_folder_package_refuses_names_that_leave_it() {
        let dir = scratch();
        let mut pkg = Package::open(&dir).unwrap();
        assert!(matches!(pkg.read("../secret"), Err(Error::BadName(_))));
        assert!(matches!(pkg.read("/etc/hosts"), Err(Error::BadName(_))));
        assert!(matches!(pkg.read("missing"), Err(Error::NotFound(_))));
        fs::remove_dir_all(dir).unwrap();
    }

    #[test]
    fn a_zip_package_lists_and_reads_its_entries() {
        let dir = scratch();
        let path = dir.join("doc.zip");
        {
            let mut zip = zip::ZipWriter::new(fs::File::create(&path).unwrap());
            let opts = zip::write::SimpleFileOptions::default().compression_method(zip::CompressionMethod::Deflated);
            zip.add_directory("Index/", opts).unwrap();
            zip.start_file("Index/one.bin", opts).unwrap();
            zip.write_all(&[7; 100]).unwrap();
            zip.finish().unwrap();
        }
        let mut pkg = Package::open(&path).unwrap();
        let parts = pkg.parts().unwrap();
        assert_eq!(parts.len(), 1);
        assert_eq!(parts[0].name, "Index/one.bin");
        assert_eq!(parts[0].size, 100);
        assert!(parts[0].stored_size.unwrap() < 100);
        assert_eq!(pkg.read("Index/one.bin").unwrap(), vec![7; 100]);
        assert!(matches!(pkg.read("nope"), Err(Error::NotFound(_))));
        fs::remove_dir_all(dir).unwrap();
    }

    #[test]
    fn a_folder_package_reads_parts_inside_its_index_zip() {
        let dir = scratch();
        fs::write(dir.join("preview.jpg"), [9]).unwrap();
        {
            let mut zip = zip::ZipWriter::new(fs::File::create(dir.join(INDEX_ZIP)).unwrap());
            let opts = zip::write::SimpleFileOptions::default().compression_method(zip::CompressionMethod::Stored);
            zip.start_file("Index/Document.iwa", opts).unwrap();
            zip.write_all(&[1, 2, 3]).unwrap();
            zip.finish().unwrap();
        }
        let mut pkg = Package::open(&dir).unwrap();
        let names: Vec<_> = pkg.parts().unwrap().into_iter().map(|p| p.name).collect();
        assert_eq!(names, vec!["Index.zip", "Index/Document.iwa", "preview.jpg"]);
        assert_eq!(pkg.read("Index/Document.iwa").unwrap(), vec![1, 2, 3]);
        assert_eq!(pkg.read("preview.jpg").unwrap(), vec![9]);
        fs::remove_dir_all(dir).unwrap();
    }

    #[test]
    fn a_file_that_is_not_a_zip_is_an_error() {
        let dir = scratch();
        let path = dir.join("junk.pages");
        fs::write(&path, b"not a zip at all").unwrap();
        assert!(matches!(Package::open(&path), Err(Error::Zip(_))));
        fs::remove_dir_all(dir).unwrap();
    }
}
