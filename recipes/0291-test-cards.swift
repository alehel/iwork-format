// Experiment 0291: draw the test cards that replace Apple's images in the project's test theme.
//
// Usage: swift recipes/0291-test-cards.swift OUTDIR
//
// Each card states its own name, size and format, so wherever it turns up (a slide, a master, a
// file in Data/) it says what it is. The cards are released under CC0 with the rest of the
// test theme. Only macOS's own frameworks are used.
import AppKit
import Foundation
import UniformTypeIdentifiers

struct Card {
    let name: String
    let width: Int
    let height: Int
    let format: String      // "png", "png-alpha" or "jpeg"
    let hue: CGFloat        // 0...1, so cards are told apart at a glance
    let role: String
}

// Six photo cards with the proportions of the six photos in Basic White's placeholders
// (experiment 0291), plus cards for backgrounds and formats Keynote treats differently.
// Photo cards are drawn at most 1024 pixels on the longer side, keeping the proportions, so that
// presentations made with the theme stay small enough to publish as fixtures.
let photoMax = 1024.0
func fit(_ w: Int, _ h: Int) -> (Int, Int) {
    let k = min(1.0, photoMax / Double(max(w, h)))
    return (Int((Double(w) * k).rounded()), Int((Double(h) * k).rounded()))
}
func photo(_ name: String, _ w: Int, _ h: Int, _ hue: CGFloat) -> Card {
    let (fw, fh) = fit(w, h)
    return Card(name: name, width: fw, height: fh, format: "jpeg", hue: hue, role: "Photo placeholder, \(w):\(h)")
}

let cards: [Card] = [
    photo("photo-a", 1434, 1669, 0.00),
    photo("photo-b", 1290, 1720, 0.10),
    photo("photo-c", 1964, 1473, 0.20),
    photo("photo-d", 1858, 1486, 0.35),
    photo("photo-e", 3195, 2556, 0.50),
    photo("photo-f", 3159, 1892, 0.65),
    Card(name: "background", width: 1920, height: 1080, format: "png", hue: 0.80, role: "Slide background"),
    Card(name: "alpha", width: 800, height: 800, format: "png-alpha", hue: 0.90, role: "Transparent PNG"),
    Card(name: "small", width: 64, height: 48, format: "png", hue: 0.05, role: "Tiny image"),
]

func draw(_ card: Card) -> NSBitmapImageRep {
    let rep = NSBitmapImageRep(bitmapDataPlanes: nil, pixelsWide: card.width, pixelsHigh: card.height,
                               bitsPerSample: 8, samplesPerPixel: 4, hasAlpha: true, isPlanar: false,
                               colorSpaceName: .deviceRGB, bytesPerRow: 0, bitsPerPixel: 0)!
    NSGraphicsContext.saveGraphicsState()
    NSGraphicsContext.current = NSGraphicsContext(bitmapImageRep: rep)
    let w = CGFloat(card.width), h = CGFloat(card.height)
    let rect = NSRect(x: 0, y: 0, width: w, height: h)
    let alpha = card.format == "png-alpha"

    // Background: a soft colour, or transparent with a translucent disc for the alpha card.
    if alpha {
        NSColor.clear.setFill()
        rect.fill()
        NSColor(calibratedHue: card.hue, saturation: 0.6, brightness: 0.9, alpha: 0.5).setFill()
        NSBezierPath(ovalIn: rect.insetBy(dx: w * 0.05, dy: h * 0.05)).fill()
    } else {
        NSColor(calibratedHue: card.hue, saturation: 0.25, brightness: 0.95, alpha: 1).setFill()
        rect.fill()
    }

    // A grid every tenth of the shorter side, to show scaling and cropping.
    let step = min(w, h) / 10
    NSColor(calibratedWhite: 0, alpha: 0.12).setStroke()
    let grid = NSBezierPath()
    grid.lineWidth = max(1, step / 40)
    var x: CGFloat = 0
    while x <= w { grid.move(to: NSPoint(x: x, y: 0)); grid.line(to: NSPoint(x: x, y: h)); x += step }
    var y: CGFloat = 0
    while y <= h { grid.move(to: NSPoint(x: 0, y: y)); grid.line(to: NSPoint(x: w, y: y)); y += step }
    grid.stroke()

    // Diagonals and a centre circle, to show crops and flips.
    NSColor(calibratedHue: card.hue, saturation: 0.8, brightness: 0.6, alpha: 0.6).setStroke()
    let marks = NSBezierPath()
    marks.lineWidth = max(1, step / 15)
    marks.move(to: .zero); marks.line(to: NSPoint(x: w, y: h))
    marks.move(to: NSPoint(x: 0, y: h)); marks.line(to: NSPoint(x: w, y: 0))
    marks.appendOval(in: NSRect(x: w / 2 - step * 2, y: h / 2 - step * 2, width: step * 4, height: step * 4))
    marks.stroke()

    // Corner tags, so a flip or rotation is visible: TL, TR, BL, BR.
    let tagFont = NSFont.boldSystemFont(ofSize: max(6, step * 0.6))
    let tagAttrs: [NSAttributedString.Key: Any] = [.font: tagFont, .foregroundColor: NSColor(calibratedWhite: 0.15, alpha: 1)]
    let pad = step * 0.3
    for (tag, px, py) in [("TL", pad, h - pad - tagFont.pointSize * 1.2), ("TR", w - pad - tagFont.pointSize * 1.6, h - pad - tagFont.pointSize * 1.2),
                          ("BL", pad, pad), ("BR", w - pad - tagFont.pointSize * 1.6, pad)] {
        (tag as NSString).draw(at: NSPoint(x: px, y: py), withAttributes: tagAttrs)
    }

    // The label: what the card is.
    if min(w, h) >= 200 {
        let lines = [card.name, card.role, "\(card.width) × \(card.height) \(card.format.uppercased())", "iwork-format test card · CC0"]
        let sizes: [CGFloat] = [step * 1.4, step * 0.6, step * 0.6, step * 0.4]
        var top = h / 2 + step * 1.6
        for (line, size) in zip(lines, sizes) {
            let font = line == card.name ? NSFont.boldSystemFont(ofSize: size) : NSFont.systemFont(ofSize: size)
            let attrs: [NSAttributedString.Key: Any] = [.font: font, .foregroundColor: NSColor(calibratedWhite: 0.1, alpha: 1)]
            let s = line as NSString
            let sz = s.size(withAttributes: attrs)
            top -= sz.height
            NSColor(calibratedWhite: 1, alpha: 0.75).setFill()
            NSRect(x: (w - sz.width) / 2 - size * 0.3, y: top, width: sz.width + size * 0.6, height: sz.height).fill()
            s.draw(at: NSPoint(x: (w - sz.width) / 2, y: top), withAttributes: attrs)
            top -= size * 0.25
        }
    }
    NSGraphicsContext.restoreGraphicsState()
    return rep
}

let out = CommandLine.arguments.count > 1 ? CommandLine.arguments[1] : "."
try FileManager.default.createDirectory(atPath: out, withIntermediateDirectories: true)
for card in cards {
    let rep = draw(card)
    let jpeg = card.format == "jpeg"
    let data = jpeg ? rep.representation(using: .jpeg, properties: [.compressionFactor: 0.6])!
                    : rep.representation(using: .png, properties: [:])!
    let path = "\(out)/\(card.name).\(jpeg ? "jpg" : "png")"
    try data.write(to: URL(fileURLWithPath: path))
    print(path)
}
