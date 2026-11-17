// Experiments 0374 onward: print a PDF's text, page by page, and its annotations.
//
// Usage: swift recipes/0374-pdf-text.swift FILE.pdf [FILE.pdf ...]
//
// For each page, prints its text as PDFKit extracts it, then one line per annotation: its type,
// the box in points from the page's bottom-left corner, its author, its colour as RGBA, its
// contents, and for a link its address or the page (from 1) and point it goes to. Only macOS's own frameworks are used.
import AppKit
import Foundation
import PDFKit

func target(_ a: PDFAnnotation, _ doc: PDFDocument) -> String {
    if let u = a.url { return u.absoluteString }
    let dest = a.destination ?? (a.action as? PDFActionGoTo)?.destination
    if let d = dest, let p = d.page {
        return String(format: "page %d at %.0f,%.0f", doc.index(for: p) + 1, d.point.x, d.point.y)
    }
    if let u = (a.action as? PDFActionURL)?.url { return u.absoluteString }
    return "-"
}

for path in CommandLine.arguments.dropFirst() {
    guard let doc = PDFDocument(url: URL(fileURLWithPath: path)) else { print("\(path): not a PDF"); continue }
    print("== \(path): \(doc.pageCount) page(s)")
    for i in 0..<doc.pageCount {
        guard let page = doc.page(at: i) else { continue }
        print("-- page \(i + 1)")
        print(page.string ?? "")
        for a in page.annotations {
            let b = a.bounds
            let c = a.color.usingColorSpace(.deviceRGB)
            let rgba = c.map { String(format: "%.2f %.2f %.2f %.2f", $0.redComponent, $0.greenComponent, $0.blueComponent, $0.alphaComponent) } ?? "?"
            print(String(format: "annotation %@ at %.0f,%.0f %.0f×%.0f", a.type ?? "?", b.minX, b.minY, b.width, b.height),
                  "author:", a.userName ?? "-", "colour:", rgba, "contents:", (a.contents ?? "-").replacingOccurrences(of: "\n", with: "\\n"),
                  "target:", target(a, doc))
        }
    }
}
