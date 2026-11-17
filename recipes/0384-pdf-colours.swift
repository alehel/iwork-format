// Experiments 0384 onward: print the colour of a PDF's first page at given points.
//
// Usage: swift recipes/0384-pdf-colours.swift FILE.pdf X,Y [X,Y ...]
//
// Points are in points from the page's top-left corner. The page is drawn at 4 pixels per point
// on white, and each pixel's red, green and blue are printed from 0 to 1. Only macOS's own
// frameworks are used.
import AppKit
import Foundation

let a = CommandLine.arguments
guard a.count >= 3, let doc = NSPDFImageRep(data: try Data(contentsOf: URL(fileURLWithPath: a[1]))) else {
    print("usage: FILE.pdf X,Y [X,Y ...]"); exit(1)
}
doc.currentPage = 0
let scale = 4.0
let b = doc.bounds
let rep = NSBitmapImageRep(bitmapDataPlanes: nil, pixelsWide: Int(b.width * scale), pixelsHigh: Int(b.height * scale),
                           bitsPerSample: 8, samplesPerPixel: 4, hasAlpha: true, isPlanar: false,
                           colorSpaceName: .deviceRGB, bytesPerRow: 0, bitsPerPixel: 0)!
NSGraphicsContext.saveGraphicsState()
NSGraphicsContext.current = NSGraphicsContext(bitmapImageRep: rep)
NSColor.white.setFill()
NSRect(x: 0, y: 0, width: b.width * scale, height: b.height * scale).fill()
doc.draw(in: NSRect(x: 0, y: 0, width: b.width * scale, height: b.height * scale))
NSGraphicsContext.restoreGraphicsState()
var out: [String] = []
for p in a.dropFirst(2) {
    let xy = p.split(separator: ",").compactMap { Double($0) }
    guard xy.count == 2, let c = rep.colorAt(x: Int(xy[0] * scale), y: Int(xy[1] * scale))?.usingColorSpace(.deviceRGB) else { continue }
    out.append(String(format: "%@: %.2f %.2f %.2f", p, c.redComponent, c.greenComponent, c.blueComponent))
}
print(out.joined(separator: " | "))
