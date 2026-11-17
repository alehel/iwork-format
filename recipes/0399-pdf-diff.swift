// Experiments 0399 onward: compare the first pages of two PDFs, pixel by pixel.
//
// Usage: swift recipes/0399-pdf-diff.swift [--box X Y W H] A.pdf B.pdf [B.pdf ...]
//
// Draws each first page at 2 pixels per point on white and counts the pixels of each B that differ
// from A's by more than 0.1 in any of red, green or blue. Prints the count and the box around them,
// in points from the page's top-left corner. With --box, only that part of the page (in points) is
// compared. Only macOS's own frameworks are used.
import AppKit
import Foundation

func draw(_ path: String) -> NSBitmapImageRep? {
    guard let doc = NSPDFImageRep(data: (try? Data(contentsOf: URL(fileURLWithPath: path))) ?? Data()) else { return nil }
    doc.currentPage = 0
    let s = 2.0, b = doc.bounds
    let rep = NSBitmapImageRep(bitmapDataPlanes: nil, pixelsWide: Int(b.width * s), pixelsHigh: Int(b.height * s),
                               bitsPerSample: 8, samplesPerPixel: 4, hasAlpha: true, isPlanar: false,
                               colorSpaceName: .deviceRGB, bytesPerRow: 0, bitsPerPixel: 0)!
    NSGraphicsContext.saveGraphicsState()
    NSGraphicsContext.current = NSGraphicsContext(bitmapImageRep: rep)
    NSColor.white.setFill()
    NSRect(x: 0, y: 0, width: b.width * s, height: b.height * s).fill()
    doc.draw(in: NSRect(x: 0, y: 0, width: b.width * s, height: b.height * s))
    NSGraphicsContext.restoreGraphicsState()
    return rep
}

var args = Array(CommandLine.arguments)
var box: (Int, Int, Int, Int)? = nil
if args.count > 5, args[1] == "--box", let x = Double(args[2]), let y = Double(args[3]), let w = Double(args[4]), let h = Double(args[5]) {
    box = (Int(x * 2), Int(y * 2), Int((x + w) * 2), Int((y + h) * 2))
    args.removeSubrange(1...5)
}
guard args.count >= 3, let a = draw(args[1]) else { print("usage: A.pdf B.pdf ..."); exit(1) }
for path in args.dropFirst(2) {
    guard let b = draw(path), b.pixelsWide == a.pixelsWide, b.pixelsHigh == a.pixelsHigh else {
        print("\(path): not comparable"); continue
    }
    var n = 0, x0 = Int.max, y0 = Int.max, x1 = -1, y1 = -1
    let pa = a.bitmapData!, pb = b.bitmapData!, row = a.bytesPerRow
    let (bx0, by0, bx1, by1) = box ?? (0, 0, a.pixelsWide, a.pixelsHigh)
    for y in max(0, by0)..<min(a.pixelsHigh, by1) {
        for x in max(0, bx0)..<min(a.pixelsWide, bx1) {
            let i = y * row + x * 4
            if abs(Int(pa[i]) - Int(pb[i])) > 25 || abs(Int(pa[i + 1]) - Int(pb[i + 1])) > 25 || abs(Int(pa[i + 2]) - Int(pb[i + 2])) > 25 {
                n += 1; x0 = min(x0, x); y0 = min(y0, y); x1 = max(x1, x); y1 = max(y1, y)
            }
        }
    }
    if n == 0 { print("\(path): same as \(args[1])") }
    else { print(String(format: "%@: %d pixels differ, in %.1f,%.1f – %.1f,%.1f", path, n, Double(x0) / 2, Double(y0) / 2, Double(x1 + 1) / 2, Double(y1 + 1) / 2)) }
}
