"""Tests for skills/profile-refresh/scripts/ats_check.py.

Run: uv run --with pypdf --with python-docx python -m unittest discover tests
"""
import importlib.util
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "skills/profile-refresh/scripts/ats_check.py"
spec = importlib.util.spec_from_file_location("ats_check", SCRIPT)
ats = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ats)

FILLER = "Built interactive lab simulations for Grade 10 classes and trained colleagues to use them. " * 8


class Args:
    name = None
    keywords = None
    pages = None
    master = False


def run(text, keywords_file=None):
    ats.results.clear()
    ats.link_targets.clear()
    args = Args()
    args.keywords = keywords_file
    ats.check_text(text, "Layla-Haddad-Resume-2026-10-18.pdf", args)
    return {check: (level, detail) for level, check, detail, _ in ats.results}


def resume(contact_line, header="Teacher of Chemistry | Crescent Bay International School, Dubai | Aug 2021 – Present"):
    return f"Layla Haddad\nTeacher of Chemistry\n{contact_line}\nEXPERIENCE\n{header}\n{FILLER}"


class LocationCheck(unittest.TestCase):
    def test_role_header_city_does_not_count_as_location(self):
        # Regression: "School, Dubai" in a role header used to pass as the contact location.
        result = run(resume("layla.example@example.com | +971 50 000 0000 | linkedin.com/in/layla-haddad-example"))
        self.assertEqual(result["Contact: Location"][0], "WARN")

    def test_city_country_in_contact_line_passes(self):
        result = run(resume("Abu Dhabi, UAE | layla.example@example.com | +971 50 000 0000"))
        self.assertEqual(result["Contact: Location"][0], "PASS")

    def test_location_label_passes(self):
        result = run(resume("Contact: +971 50 000 0000 | E-mail: layla.example@example.com | Location: Abu Dhabi, UAE"))
        self.assertEqual(result["Contact: Location"][0], "PASS")

    def test_full_country_name_and_us_state_pass(self):
        self.assertEqual(run(resume("Leeds, United Kingdom | a@example.com"))["Contact: Location"][0], "PASS")
        self.assertEqual(run(resume("Austin, TX | a@example.com"))["Contact: Location"][0], "PASS")

    def test_remote_passes(self):
        self.assertEqual(run(resume("Remote | layla.example@example.com"))["Contact: Location"][0], "PASS")

    def test_skills_pair_in_headline_is_not_a_location(self):
        text = "Sam Example\nBackend Engineer | Java, AWS\nsam@example.com | +971 50 000 0000\nEXPERIENCE\n" + FILLER
        self.assertEqual(run(text)["Contact: Location"][0], "WARN")


class OtherChecks(unittest.TestCase):
    def test_short_acronyms_match_whole_words_only(self):
        keywords = Path(__file__).with_name("_keywords.txt")
        keywords.write_text("SAM\nLMS\n", encoding="utf-8")
        try:
            result = run(resume("Dubai, UAE | a@example.com") + "\nMade the same short films.", str(keywords))
        finally:
            keywords.unlink()
        self.assertIn("0/2", result["Keyword coverage"][1])

    def test_letter_spaced_heading_fails(self):
        result = run(resume("Dubai, UAE | a@example.com") + "\nC O N T A C T")
        self.assertEqual(result["Letter-spaced text"][0], "FAIL")

    def test_year_range_is_not_a_phone_number(self):
        text = "Sam Example\nAnalyst\nsam@example.com | Dubai, UAE\nEXPERIENCE\nAnalyst | Beta Ltd | 2017 - 2019\n" + FILLER
        self.assertEqual(run(text)["Contact: Phone"][0], "WARN")


if __name__ == "__main__":
    unittest.main()
