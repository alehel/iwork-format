//! Hex dumps: 16 bytes a line, with the offset and the bytes as ASCII.

/// Format `bytes` as a hex dump whose offsets start at `base`.
pub fn dump(bytes: &[u8], base: usize) -> String {
    let mut out = String::new();
    for (i, line) in bytes.chunks(16).enumerate() {
        let offset = base.saturating_add(i.saturating_mul(16));
        let hex: Vec<String> = line.iter().map(|b| format!("{b:02x}")).collect();
        let ascii: String =
            line.iter().map(|&b| if b.is_ascii_graphic() || b == b' ' { b as char } else { '.' }).collect();
        out.push_str(&format!("{offset:08x}  {:<47}  |{ascii}|\n", hex.join(" ")));
    }
    out
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn lines_show_offset_hex_and_ascii() {
        let text = dump(b"PK\x03\x04hello, world!!!xyz", 0x20);
        let lines: Vec<&str> = text.lines().collect();
        assert_eq!(lines[0], "00000020  50 4b 03 04 68 65 6c 6c 6f 2c 20 77 6f 72 6c 64  |PK..hello, world|");
        assert_eq!(lines[1], "00000030  21 21 21 78 79 7a                                |!!!xyz|");
    }

    #[test]
    fn empty_input_prints_nothing() {
        assert_eq!(dump(&[], 0), "");
    }
}
