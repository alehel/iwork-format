// Experiments 0482 onward: say on which pages of a PDF red ink is drawn, and where.
//
// Usage: swift recipes/0482-red-per-page.swift FILE.pdf [FILE.pdf ...]
//
// Draws every page at 4 pixels per point and prints, for each, its first words of text and each
// band of red pixels (red above 0.8, green and blue below 0.3), then of blue ones (the other way
// round), as a box in points from the page's top-left corner, with the colour's area in square points
// (so that where two patches overlap, the one drawn on top keeps its whole area). Only macOS's own frameworks are used.
import AppKit
import Foundation
import PDFKit

for path in CommandLine.arguments.dropFirst() {
    guard let doc = PDFDocument(url: URL(fileURLWithPath: path)) else { print("\(path): not a PDF"); continue }
    print("\(path): \(doc.pageCount) pages")
    for i in 0..<doc.pageCount {
        guard let page = doc.page(at: i) else { continue }
        let b = page.bounds(for: .mediaBox)
        let scale = 4.0
        let w = Int(b.width * scale), h = Int(b.height * scale)
        guard let rep = NSBitmapImageRep(bitmapDataPlanes: nil, pixelsWide: w, pixelsHigh: h, bitsPerSample: 8,
                                         samplesPerPixel: 4, hasAlpha: true, isPlanar: false, colorSpaceName: .deviceRGB,
                                         bytesPerRow: w * 4, bitsPerPixel: 32),
              let ctx = NSGraphicsContext(bitmapImageRep: rep) else { continue }
        let cg = ctx.cgContext
        cg.setFillColor(NSColor.white.cgColor)
        cg.fill(CGRect(x: 0, y: 0, width: w, height: h))
        cg.scaleBy(x: scale, y: scale)
        page.draw(with: .mediaBox, to: cg)
        guard let data = rep.bitmapData else { continue }
        func bands(_ hit: (UInt8, UInt8, UInt8) -> Bool) -> [String] {
        // Rows with the colour, grouped into bands; within each band, the horizontal extent.
        var boxes: [(Int, Int, Int, Int)] = []  // x0, y0, x1, y1 in pixels, y from top
        var current: (Int, Int, Int, Int)? = nil
        var count = 0
        for y in 0..<h {
            var minX = Int.max, maxX = -1
            for x in 0..<w {
                let o = y * w * 4 + x * 4
                if hit(data[o], data[o + 1], data[o + 2]) { count += 1; minX = min(minX, x); maxX = max(maxX, x) }
            }
            if maxX >= 0 {
                if let c = current { current = (min(c.0, minX), c.1, max(c.2, maxX), y) } else { current = (minX, y, maxX, y) }
            } else if let c = current { boxes.append(c); current = nil }
        }
        if let c = current { boxes.append(c) }
        if boxes.isEmpty { return [] }
        return boxes.map { b in
            String(format: "(%.1f, %.1f)–(%.1f, %.1f)", Double(b.0) / scale, Double(b.1) / scale,
                   Double(b.2 + 1) / scale, Double(b.3 + 1) / scale)
        } + [String(format: "area %.1f", Double(count) / (scale * scale))]
        }
        let red = bands { r, g, b in r > 204 && g < 77 && b < 77 }
        let blue = bands { r, g, b in b > 204 && r < 77 && g < 77 }
        let text = (page.string ?? "").replacingOccurrences(of: "\n", with: " ").prefix(30)
        var line = "  page \(i + 1): text \"\(text)\"; red: \(red.isEmpty ? "none" : red.joined(separator: ", "))"
        if !blue.isEmpty { line += "; blue: " + blue.joined(separator: ", ") }
        print(line)
    }
}
