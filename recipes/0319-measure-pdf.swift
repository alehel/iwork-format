// Experiments 0319 onward: measure where the ink is on the first page of a PDF, in points.
//
// Usage: swift recipes/0319-measure-pdf.swift FILE.pdf [FILE.pdf ...]
//
// Draws the first page at 4 pixels per point, then prints the box around all dark pixels and each
// band of rows that holds ink (a line of text), with its left and right ends. Coordinates are in
// points from the page's top-left corner. Only macOS's own frameworks are used.
import AppKit
import Foundation

for path in CommandLine.arguments.dropFirst() {
    guard let doc = NSPDFImageRep(data: try Data(contentsOf: URL(fileURLWithPath: path))) else {
        print("\(path): not a PDF"); continue
    }
    doc.currentPage = 0
    let scale = 4.0
    let page = doc.bounds
    let w = Int(page.width * scale), h = Int(page.height * scale)
    let rep = NSBitmapImageRep(bitmapDataPlanes: nil, pixelsWide: w, pixelsHigh: h, bitsPerSample: 8,
                               samplesPerPixel: 4, hasAlpha: true, isPlanar: false, colorSpaceName: .deviceRGB,
                               bytesPerRow: 0, bitsPerPixel: 0)!
    NSGraphicsContext.saveGraphicsState()
    NSGraphicsContext.current = NSGraphicsContext(bitmapImageRep: rep)
    NSColor.white.setFill()
    NSRect(x: 0, y: 0, width: w, height: h).fill()
    doc.draw(in: NSRect(x: 0, y: 0, width: w, height: h))
    NSGraphicsContext.restoreGraphicsState()

    var rows: [(Int, Int)?] = Array(repeating: nil, count: h)  // per pixel row: leftmost, rightmost ink
    for y in 0..<h {
        var lo = -1, hi = -1
        for x in 0..<w {
            if let c = rep.colorAt(x: x, y: y), c.brightnessComponent < 0.6 {
                if lo < 0 { lo = x }
                hi = x
            }
        }
        if lo >= 0 { rows[y] = (lo, hi) }
    }
    func pt(_ v: Int) -> String { String(format: "%.1f", Double(v) / scale) }
    print("\(path): page \(pt(w)) × \(pt(h))")
    var y = 0
    var bands: [(Int, Int, Int, Int)] = []
    while y < h {
        if rows[y] == nil { y += 1; continue }
        let top = y
        var lo = Int.max, hi = 0
        while y < h, let r = rows[y] { lo = min(lo, r.0); hi = max(hi, r.1); y += 1 }
        bands.append((top, y - 1, lo, hi))
    }
    if bands.isEmpty { print("  no ink"); continue }
    let left = bands.map { $0.2 }.min()!, right = bands.map { $0.3 }.max()!
    print("  ink box: left \(pt(left)), top \(pt(bands.first!.0)), right \(pt(right)), bottom \(pt(bands.last!.1))")
    for b in bands {
        print("  band: top \(pt(b.0)), bottom \(pt(b.1)), left \(pt(b.2)), right \(pt(b.3))")
    }
}
