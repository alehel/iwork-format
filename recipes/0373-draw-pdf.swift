// Experiments 0373 onward: draw part of a PDF's first page as text, to compare shapes by eye.
//
// Usage: swift recipes/0373-draw-pdf.swift FILE.pdf X Y WIDTH HEIGHT [STEP]
//
// X, Y, WIDTH and HEIGHT are a box in points from the page's top-left corner. Every STEP points
// (default 5) across and down, prints `#` where the page is dark (brightness below 0.5), `o` where
// it is coloured (saturation above 0.4) and `.` elsewhere. Only macOS's own frameworks are used.
import AppKit
import Foundation

let a = CommandLine.arguments
guard a.count >= 6, let x0 = Double(a[2]), let y0 = Double(a[3]), let w = Double(a[4]), let h = Double(a[5]) else {
    print("usage: FILE.pdf X Y WIDTH HEIGHT [STEP]"); exit(1)
}
let step = a.count > 6 ? Double(a[6]) ?? 5 : 5
guard let doc = NSPDFImageRep(data: try Data(contentsOf: URL(fileURLWithPath: a[1]))) else { print("not a PDF"); exit(1) }
doc.currentPage = 0
let scale = 4.0
let page = doc.bounds
let rep = NSBitmapImageRep(bitmapDataPlanes: nil, pixelsWide: Int(page.width * scale), pixelsHigh: Int(page.height * scale),
                           bitsPerSample: 8, samplesPerPixel: 4, hasAlpha: true, isPlanar: false,
                           colorSpaceName: .deviceRGB, bytesPerRow: 0, bitsPerPixel: 0)!
NSGraphicsContext.saveGraphicsState()
NSGraphicsContext.current = NSGraphicsContext(bitmapImageRep: rep)
NSColor.white.setFill()
NSRect(x: 0, y: 0, width: page.width * scale, height: page.height * scale).fill()
doc.draw(in: NSRect(x: 0, y: 0, width: page.width * scale, height: page.height * scale))
NSGraphicsContext.restoreGraphicsState()
var y = y0 + step / 2
while y < y0 + h {
    var line = ""
    var x = x0 + step / 2
    while x < x0 + w {
        let c = rep.colorAt(x: Int(x * scale), y: Int(y * scale))?.usingColorSpace(.deviceRGB)
        if (c?.brightnessComponent ?? 1) < 0.5 { line += "#" }
        else if (c?.saturationComponent ?? 0) > 0.4 { line += "o" }
        else { line += "." }
        x += step
    }
    print(line)
    y += step
}
