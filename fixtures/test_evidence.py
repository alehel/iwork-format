"""Tests for the evidence checker, with documents made up here rather than samples.

Usage: python3 -I fixtures/test_evidence.py
"""
import importlib.util
import os
import struct
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("evidence", os.path.join(HERE, "evidence.py"))
e = importlib.util.module_from_spec(spec)
spec.loader.exec_module(e)
w = e.w


def message(*fields):
    out = []
    for f, v in fields:
        if isinstance(v, int):
            out.append((f, 0, w.write_varint(v)))
        elif isinstance(v, float):
            out.append((f, 5, struct.pack("<f", v)))
        else:
            out.append((f, 2, v.encode() if isinstance(v, str) else v))
    return w.serialize_message(out)


def document(records, parts=(), sha="x"):
    d = object.__new__(e.Document)
    d.rel, d.sha, d.parts = "made/up", sha, {p: b"" for p in parts}
    d.records = {(i, 0): (k, p) for i, k, p in records}
    d.headers = {(i, 0): (k, message((1, k))) for i, k, p in records}
    d.order, d.error = {"Index/Document.iwa": [(i, 0) for i, _, _ in records]}, None
    return d


BASE = document([(1, 2021, message((11, message((1, 1))))), (2, 2001, message((3, "one"))), (3, 10000, message((30, 595.28), (42, 0)))], ["preview.jpg"])
SAME = document([(i, k, p) for (i, _), (k, p) in BASE.records.items()], ["preview.jpg"])
CHANGED = document([(1, 2021, message((11, message((11, 1))))), (2, 2001, message((3, "two"))), (3, 10000, message((30, 595.28), (42, 1)))], [".iwph"], "y")


class Statements(unittest.TestCase):
    def holds(self, s, base=BASE, doc=CHANGED):
        self.assertIsNone(e.check(s, base, doc))

    def fails(self, s, base=BASE, doc=CHANGED):
        self.assertIsNotNone(e.check(s, base, doc))

    def test_value(self):
        self.holds("2021 11.11 = 1")
        self.holds('2001 3 = "two"')
        self.holds("10000 30 = 595.28")
        self.fails("2021 11.1 = 1")
        self.fails("10000 30 = 595")  # a float isn't an integer
        self.holds("2021 11.1 = absent")

    def test_change(self):
        self.holds("2021 11.11: absent → 1")
        self.holds("2021 11.1: 1 → absent")
        self.holds('2001#2 3: "one" → "two"')
        self.fails('2001#3 3: "one" → "two"')  # another record
        self.fails('2001 3: "two" → "one"')
        self.fails("2021 11.11: absent → 1", doc=SAME)
        self.fails("10000#3 42: absent → 1")  # the record held a value already

    def test_records_and_parts(self):
        self.holds("records 2021: 1 → 1")
        self.fails("records 2021: 0 → 1")
        self.holds("part .iwph: absent → present")
        self.holds("part preview*: present → absent")
        self.fails("part .iwph: present → present")

    def test_counts_and_bytes(self):
        self.holds("2021 11: ×1 → ×1")
        self.fails("2021 11: ×1 → ×2")
        self.holds('2001 3 ~ "w"')
        self.holds('2001 3 = x"74776f"')
        self.fails('2001 3 ~ "x"')
        self.holds("2021 11.1 ≠ present")
        self.fails("2021 11.11 ≠ 1")
        self.fails("99 1 ≠ 1")  # there is no such record
        self.holds("2001 3: changed")
        self.fails("2001 3: changed", doc=SAME)

    def test_header_and_order(self):
        other = document([(i, k, p) for (i, _), (k, p) in reversed(BASE.records.items())], ["preview.jpg"])
        other.headers[(1, 0)] = (2021, message((1, 2021), (5, 7)))
        self.holds("header 2021#1 5: absent → 7", doc=other)
        self.holds("order Index/Document.iwa: changed", doc=other)
        self.fails("order Index/Document.iwa: changed", doc=SAME)
        self.assertEqual(len(e.uncovered([], BASE, other)), 2)
        self.assertEqual(e.uncovered(["header 2021#1 5: absent → 7", "order Index/Document.iwa: changed"], BASE, other), [])

    def test_unreadable(self):
        bad = document([], sha="z")
        bad.error = "Index/Document.iwa: no"
        self.holds("unreadable", doc=bad)
        self.fails("unreadable")
        self.fails("2021 11.1 = 1", doc=bad)

    def test_float_precision(self):
        self.fails("10000 30 = 595.4")
        self.fails("10000 30 = 595.281")

    def test_same(self):
        self.holds("same records", doc=SAME)
        self.fails("same records")
        self.holds("same bytes", doc=SAME)
        self.fails("same bytes")

    def test_anything_else_is_an_error(self):
        for s in ("2021 11.11", "2021 11.11 = maybe", "nothing"):
            with self.assertRaises(SystemExit):
                e.check(s, BASE, CHANGED)


class Only(unittest.TestCase):
    def test_everything_must_be_named(self):
        named = ["2021 11.1: 1 → absent", "2021 11.11: absent → 1", '2001#2 3: "one" → "two"', "10000 42: 0 → 1", "part .iwph: absent → present"]
        self.assertEqual(e.uncovered(named, BASE, CHANGED), [])
        for i in range(len(named)):
            self.assertTrue(e.uncovered(named[:i] + named[i + 1:], BASE, CHANGED), named[i])

    def test_previews_dont_count(self):
        self.assertEqual(e.uncovered([], BASE, document([(i, k, p) for (i, _), (k, p) in BASE.records.items()])), [])

    def test_a_new_record_counts(self):
        more = document([(i, k, p) for (i, _), (k, p) in BASE.records.items()] + [(9, 212, b"")])
        self.assertEqual(e.uncovered([], BASE, more), [("record", 212, 9, 1)])
        self.assertEqual(e.uncovered(["records 212: 0 → 1"], BASE, more), [])

    def test_text_isnt_taken_for_a_message(self):
        self.assertEqual(e.leaf_paths(message((2, "1")), message((2, "9"))), [(2,)])


class Tables(unittest.TestCase):
    def test_rows(self):
        md = "# x\n\n## Evidence\n\n| File | Compared with | Difference | Shows |\n| --- | --- | --- | --- |\n| `a.pages` | `0008/b.pages` | x | y |\n\n## Confidence\n"
        (row,) = e.evidence_rows(md)
        self.assertEqual([e.sample(c, "0012") for c in row[:3]], ["samples/0012/a.pages", "samples/0008/b.pages", None])
        self.assertIsNone(e.evidence_rows("# x\n"))
        self.assertEqual(e.evidence_rows("## Evidence\n\nNo documents of its own: x.\n"), [])

    def test_wrong_columns(self):
        with self.assertRaises(SystemExit):
            e.evidence_rows("## Evidence\n\n| File | Shows |\n| --- | --- |\n| a | b |\n")


if __name__ == "__main__":
    unittest.main()
