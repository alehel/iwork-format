// Experiments 0448 onward: compare images with a first one, pixel by pixel.
//
// Usage: swift recipes/0449-image-diff.swift BASE.png OTHER.png [OTHER.png ...]
//
// Counts, over every second pixel in each direction, the pixels of each OTHER whose red, green and
// blue differ from BASE's by more than 0.3 in total. Only macOS's own frameworks are used.
import AppKit
func rep(_ p: String) -> NSBitmapImageRep { NSBitmapImageRep(data: try! Data(contentsOf: URL(fileURLWithPath: p)))! }
let args = Array(CommandLine.arguments.dropFirst()); let base = rep(args[0])
for p in args.dropFirst() {
  let r = rep(p); var n = 0
  for y in stride(from: 0, to: r.pixelsHigh, by: 2) { for x in stride(from: 0, to: r.pixelsWide, by: 2) {
    let a = base.colorAt(x: x, y: y)!, b = r.colorAt(x: x, y: y)!
    if abs(a.redComponent - b.redComponent) + abs(a.greenComponent - b.greenComponent) + abs(a.blueComponent - b.blueComponent) > 0.3 { n += 1 } } }
  print(p.split(separator: "/").suffix(1).joined(), "differs from", args[0].split(separator: "/").suffix(1).joined(), "in", n, "sampled pixels")
}
