"""Tests for the site builder's Markdown subset and checks.

Usage: python3 -I site/test_build.py

Only the standard library is used. Each test renders a small piece of Markdown the way the spec and
experiments use it, and checks the HTML, or checks that Markdown the builder can't render faithfully
is reported instead of passing silently.
"""
import importlib.util
import os
import tempfile
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("build", os.path.join(HERE, "build.py"))
b = importlib.util.module_from_spec(spec)
spec.loader.exec_module(b)


class Case(unittest.TestCase):
    def setUp(self):
        b.PROBLEMS.clear()
        b.SITE_PAGES.clear()
        b.SITE_PAGES.update({"spec/text.md": "spec/text.html", "spec/container.md": "spec/container.html",
                             "experiments/0001-empty-document.md": "experiments/0001-empty-document.html"})

    def render(self, md, here="spec/text.md"):
        return b.render(md, here)

    def assertProblem(self, fragment):
        self.assertTrue(any(fragment in m for _, m in b.PROBLEMS), f"no problem mentioning {fragment!r}: {b.PROBLEMS}")


class Headings(Case):
    def test_anchor_and_name(self):
        out = self.render("## The body text")
        self.assertIn('<h2 id="the-body-text">', out)
        self.assertIn('aria-label="Link to this section: The body text"', out)

    def test_repeated_headings_get_their_own_ids(self):
        out = self.render("## Fields\n\ntext\n\n## Fields\n\n## Fields")
        for anchor in ("fields", "fields-2", "fields-3"):
            self.assertIn(f'id="{anchor}"', out)

    def test_contents_list_collects_level_two(self):
        toc = []
        b.render("# Title\n\n## One\n\n### Inner\n\n## Two", "spec/text.md", toc)
        self.assertEqual([a for a, _ in toc], ["one", "two"])

    def test_too_deep_is_reported(self):
        self.render("##### Five")
        self.assertProblem("deeper than ####")


class Tables(Case):
    def test_header_body_and_inline(self):
        out = self.render("| Field | Holds |\n| --- | --- |\n| 3 | The `text` *likely* |")
        self.assertIn('<thead><tr><th scope="col">Field</th><th scope="col">Holds</th></tr></thead>', out)
        self.assertIn("<td>The <code>text</code> <em>likely</em></td>", out)
        self.assertEqual(b.PROBLEMS, [])

    def test_empty_header_makes_row_headers(self):
        out = self.render("| | |\n| --- | --- |\n| Pages | 15.4 |")
        self.assertNotIn("<thead>", out)
        self.assertIn('<tr><th scope="row">Pages</th><td>15.4</td></tr>', out)

    def test_wrong_cell_count_is_reported(self):
        self.render("| A | B |\n| --- | --- |\n| 1 | 2 | 3 |")
        self.assertProblem("3 cells, its header 2")


class Lists(Case):
    def test_nested(self):
        out = self.render("- one\n  - inner\n- two")
        self.assertEqual(out.count("<ul>"), 2)
        self.assertIn("<li>two</li>", out)

    def test_ordered(self):
        out = self.render("1. first\n2. second")
        self.assertTrue(out.startswith("<ol>"))

    def test_item_with_code(self):
        out = self.render("- run this:\n\n   ```bash\n   echo hi\n   ```\n")
        self.assertIn("<pre", out)
        self.assertIn("echo hi", out)


class Code(Case):
    def test_escaped_and_kept(self):
        out = self.render("```python\nif a < b and c & d:\n    pass\n```")
        self.assertIn('<pre class="lang-python"><code>if a &lt; b and c &amp; d:\n    pass</code></pre>', out)

    def test_unclosed_is_reported(self):
        self.render("```\nnever closed")
        self.assertProblem("not closed")

    def test_markdown_inside_inline_code_is_left_alone(self):
        out = b.inline("`*not em* [x](y.md)`", "spec/text.md")
        self.assertEqual(out, "<code>*not em* [x](y.md)</code>")


class Inline(Case):
    def test_text_is_escaped(self):
        self.assertEqual(b.inline("a < b & c", "spec/text.md"), "a &lt; b &amp; c")

    def test_emphasis_and_strong(self):
        self.assertEqual(b.inline("**Confirmed** and *likely*", "spec/text.md"),
                         "<strong>Confirmed</strong> and <em>likely</em>")

    def test_stars_inside_words_stay(self):
        self.assertEqual(b.inline("2*3*4", "spec/text.md"), "2*3*4")

    def test_markdown_links_become_site_links(self):
        out = b.inline("[0001](../experiments/0001-empty-document.md)", "spec/text.md")
        self.assertEqual(out, '<a href="../experiments/0001-empty-document.html">0001</a>')

    def test_fragment_is_kept(self):
        out = b.inline("[styles](text.md#styles)", "spec/container.md")
        self.assertEqual(out, '<a href="text.html#styles">styles</a>')

    def test_other_files_go_to_github(self):
        out = b.inline("[recipe](../recipes/0372-in-app.sh)", "spec/text.md")
        self.assertIn(f'href="{b.REPO}/blob/main/recipes/0372-in-app.sh"', out)

    def test_missing_markdown_file_is_reported(self):
        b.inline("[gone](../experiments/9999-nothing.md)", "spec/text.md")
        self.assertProblem("missing file")

    def test_release_mark_becomes_a_badge(self):
        out = b.inline("[release: 15.4 only] The record", "spec/numbers.md")
        self.assertIn('<span class="release" title="Holds for some releases only">15.4 only</span>', out)


class Directives(Case):
    def test_excerpt_is_included_escaped(self):
        name = sorted(os.listdir(os.path.join(HERE, "examples")))[0]
        out = self.render(f"<!-- include: {name} -->")
        self.assertTrue(out.startswith('<pre class="excerpt"><code>'))
        self.assertEqual(b.PROBLEMS, [])

    def test_missing_excerpt_is_reported(self):
        out = self.render("<!-- include: no-such-excerpt.txt -->")
        self.assertIn("missing excerpt", out)
        self.assertProblem("doesn't exist")

    def test_raw_html_is_reported(self):
        self.render("<div>not supported</div>")
        self.assertProblem("raw HTML")

    def test_unknown_comment_is_reported(self):
        self.render("<!-- something-new -->")
        self.assertProblem("unknown directive")


class Experiments(Case):
    SETUP = "# 0999: x\n\n## Setup\n\n| | |\n| --- | --- |\n| Pages | 14.5 |\n\n## Observation\n\n| App | Copies |\n| --- | --- |\n| Keynote | 13.1 |\n"

    def test_releases_come_from_setup_only(self):
        self.assertEqual(b.experiment_releases(self.SETUP), ["14.5"])

    def test_several_apps_in_one_row(self):
        md = "## Setup\n\n| | |\n| --- | --- |\n| Pages, Keynote and Numbers | 15.4 |\n"
        self.assertEqual(b.experiment_releases(md), ["15.4"])


class RecordTypes(Case):
    def test_forms(self):
        text = "a type-2001 record, types 401, 2022 and 2023, and type 6001"
        self.assertEqual(list(b.record_types(text)), [2001, 401, 2022, 2023, 6001])

    def test_numbers_that_are_not_record_types(self):
        text = "node type 63, list type 4, a boolean (type 6), the table's list of type 9, the type-9 list"
        self.assertEqual(list(b.record_types(text)), [])

    def test_type_table_rows(self):
        md = "## Records\n\n| Type | Holds | Part |\n| --- | --- | --- |\n| 6001 | The table model | `X.iwa` |\n"
        found = list(b.type_mentions(md))
        self.assertEqual(found[0][0], 6001)
        self.assertEqual(found[0][2][1], "The table model")


class Search(Case):
    def setUp(self):
        super().setUp()
        b.SEARCH_ENTRIES.clear()

    def test_one_entry_per_section(self):
        body = self.render("# 4. Tables\n\nIntro & more.\n\n## Merged cells\n\nField 47.2.\n\n### Inner\n\nDeeper.")
        b.index_sections("spec", "spec/tables.html", "Tables", body)
        got = [(e["t"], e["u"], e["x"]) for e in b.SEARCH_ENTRIES]
        self.assertEqual(got, [("Tables", "spec/tables.html", "Intro & more."),
                               ("Tables › Merged cells", "spec/tables.html#merged-cells", "Field 47.2."),
                               ("Tables › Inner", "spec/tables.html#inner", "Deeper.")])

    def test_experiments_keep_only_named_sections(self):
        body = self.render("# 0999: x\n\nWhy.\n\n## Observation\n\nBytes.\n\n## Conclusion\n\nA rule.")
        b.index_sections("exp", "experiments/0999-x.html", "0999: x", body, only={"Conclusion"})
        self.assertEqual([e["t"] for e in b.SEARCH_ENTRIES], ["0999: x", "0999: x › Conclusion"])


class LinkCheck(Case):
    def test_reports_missing_files_fragments_and_repeated_ids(self):
        with tempfile.TemporaryDirectory() as d:
            with open(os.path.join(d, "a.html"), "w") as f:
                f.write('<h2 id="x"></h2><p id="x"></p><a href="b.html">b</a><a href="a.html#y">y</a>'
                        '<a href="#x">ok</a><a href="https://example.com/">ok</a>')
            problems = b.check_links(d)
        self.assertEqual(len(problems), 3, problems)
        self.assertTrue(any("used twice" in p for p in problems))
        self.assertTrue(any("no such file" in p for p in problems))
        self.assertTrue(any("no such section" in p for p in problems))


if __name__ == "__main__":
    unittest.main()
