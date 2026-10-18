# /// script
# requires-python = ">=3.9"
# dependencies = ["pypdf>=4.0", "python-docx>=1.1"]
# ///
"""Deterministic ATS parse check for a resume PDF or DOCX. Reports PASS / WARN / FAIL items with fixes.

Usage: uv run ats_check.py Name-Resume-2026-10-18.pdf [--name "Full Name"] [--keywords keywords.txt] [--pages 2]
       [--master]   (a master resume has no page target, so page count and fill are not checked)
No checker can guarantee how a particular applicant tracking system will read a resume; this catches the common
ways a file becomes unreadable to one.
"""
import argparse
import re
import sys
from pathlib import Path

STANDARD_HEADINGS = {
    "summary", "profile", "professional summary", "profile summary", "career summary", "objective", "about",
    "experience", "work experience", "professional experience", "employment history", "work history",
    "education", "skills", "technical skills", "core skills", "key skills", "core competencies",
    "certifications", "licenses", "licenses & certifications", "licenses and certifications", "certificates",
    "projects", "personal projects", "publications", "languages", "awards", "honors", "honors & awards",
    "volunteering", "volunteer experience", "training", "courses", "interests", "references", "achievements",
}
HEADING_STEMS = ("summary", "profile", "experience", "education", "skill", "certific", "licen", "project",
                 "publication", "language", "award", "volunteer", "training", "course", "achievement")
EMAIL_RE = re.compile(r"[\w.+-]+@[\w-]+\.[\w.-]+")
PHONE_RE = re.compile(r"(?<!\d)\+?\d[\d\s().-]{7,17}\d(?!\d)")
LINKEDIN_RE = re.compile(r"linkedin\.com/in/[\w-]+", re.I)
MONTH = r"(?:jan|feb|mar|apr|may|jun|jul|aug|sep|sept|oct|nov|dec)[a-z]*\.?"
DATE_FORMATS = {
    "Mon YYYY": re.compile(rf"\b{MONTH}\s+(?:19|20)\d{{2}}\b", re.I),
    "MM/YYYY": re.compile(r"\b(?:0?[1-9]|1[0-2])/(?:19|20)\d{2}\b"),
    "YYYY-MM": re.compile(r"\b(?:19|20)\d{2}-(?:0[1-9]|1[0-2])\b"),
}
RANGE_RE = re.compile(rf"((?:{MONTH}\s+)?(?:\d{{1,2}}/)?(?:19|20)\d{{2}})\s*(?:-|–|—|to)\s*"
                      rf"((?:{MONTH}\s+)?(?:\d{{1,2}}/)?(?:19|20)\d{{2}}|present|current|now)", re.I)
COUNTRIES = {
    "afghanistan", "algeria", "argentina", "australia", "austria", "bahrain", "bangladesh", "belgium", "brazil",
    "canada", "chile", "china", "colombia", "czechia", "denmark", "egypt", "england", "estonia", "ethiopia",
    "finland", "france", "germany", "ghana", "greece", "hong kong", "hungary", "india", "indonesia", "iran", "iraq",
    "ireland", "israel", "italy", "japan", "jordan", "kenya", "korea", "kuwait", "lebanon", "malaysia", "mexico",
    "morocco", "nepal", "netherlands", "new zealand", "nigeria", "norway", "oman", "pakistan", "palestine", "peru",
    "philippines", "poland", "portugal", "qatar", "romania", "russia", "saudi arabia", "scotland", "serbia",
    "singapore", "south africa", "south korea", "spain", "sri lanka", "sweden", "switzerland", "syria", "taiwan",
    "tanzania", "thailand", "tunisia", "turkey", "türkiye", "uganda", "ukraine", "united arab emirates",
    "united kingdom", "united states", "usa", "vietnam", "wales", "yemen",
}
REGION_CODES = {
    "UAE", "UK", "US", "USA", "KSA", "NZ",
    "AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "DC", "FL", "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA",
    "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND", "OH", "OK", "OR",
    "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY",
    "ON", "BC", "QC", "AB", "MB", "NS", "NB", "NL", "PE", "SK",
}
# "Abu Dhabi, UAE", "Austin, TX", "Leeds, United Kingdom"; the region must be a known country or code, so a skills
# headline like "Java, AWS" doesn't count as a location.
CITY_REGION_RE = re.compile(r"^[A-Z][\w'.-]*(?:\s[A-Z][\w'.-]*){0,3},\s*(?P<region>[A-Z]{2,3}|[A-Z][a-zA-Zü]+(?:\s[A-Z][a-z]+){0,2})$")
SPACED_RE = re.compile(r"(?<![A-Za-z])(?:[A-Za-z] ){3,}[A-Za-z](?![A-Za-z])")

URL_RE = re.compile(r"(?:https?://|www\.)[^\s|,;)]*[^\s|,;).!?:]|\b[a-z0-9-]+(?:\.[a-z0-9-]+)*\."
                    r"(?:com|org|net|io|dev|ai|me|co|app|page|site|uk|ae|in|edu|gov|info|bio)/[^\s|,;)]*[^\s|,;).!?:]",
                    re.I)

results = []
link_targets = []


def report(level, check, detail, fix=""):
    results.append((level, check, detail, fix))


def font_embedded(font):
    font = font.get_object()
    if font.get("/Subtype") == "/Type0":
        font = font["/DescendantFonts"][0].get_object()
    descriptor = font.get("/FontDescriptor")
    if descriptor is None:
        return False
    descriptor = descriptor.get_object()
    return any(key in descriptor for key in ("/FontFile", "/FontFile2", "/FontFile3"))


def read_pdf(path, args):
    from pypdf import PdfReader

    reader = PdfReader(path)
    pages_text, not_embedded, image_pages, split_lines, total_lines = [], set(), [], 0, 0
    last_page_fill = None
    for index, page in enumerate(reader.pages):
        runs = []

        def visit(text, cm, tm, font_dict, font_size):
            if text.strip():
                # Position in page space: the text matrix combined with the current transform (Chrome flips y).
                x = tm[4] * cm[0] + tm[5] * cm[2] + cm[4]
                y = tm[4] * cm[1] + tm[5] * cm[3] + cm[5]
                runs.append((round(y), x, text))

        text = page.extract_text(visitor_text=visit) or ""
        pages_text.append(text)
        rows = {}
        for y, x, _ in runs:
            rows.setdefault(y, []).append(x)
        for xs in rows.values():
            total_lines += 1
            xs.sort()
            # Two text starts far apart on the same baseline, both in the left 60% of the page, suggest columns.
            if len(xs) > 1 and xs[0] < page.mediabox.width * 0.6 and any(
                    b - a > page.mediabox.width * 0.3 and b < page.mediabox.width * 0.6 for a, b in zip(xs, xs[1:])):
                split_lines += 1
        if index == len(reader.pages) - 1 and runs:
            lowest = min(y for y, _, _ in runs)
            height = float(page.mediabox.height)
            last_page_fill = max(0.0, min(1.0, (height - lowest) / height))
        for annot in page.get("/Annots") or []:
            annot = annot.get_object()
            action = annot.get("/A")
            if annot.get("/Subtype") == "/Link" and action and "/URI" in action.get_object():
                link_targets.append(str(action.get_object()["/URI"]))
        resources = page.get("/Resources") or {}
        for font in (resources.get("/Font") or {}).values():
            if not font_embedded(font):
                not_embedded.add(str(font.get_object().get("/BaseFont")))
        xobjects = (resources.get("/XObject") or {})
        if any(x.get_object().get("/Subtype") == "/Image" for x in xobjects.values()):
            image_pages.append((index + 1, len(text.strip())))

    if not_embedded:
        report("WARN", "Fonts embedded", f"not embedded: {', '.join(sorted(not_embedded))}",
               "Export the PDF with 'embed fonts' on, or use a common font (Calibri, Arial).")
    else:
        report("PASS", "Fonts embedded", "all fonts are embedded")
    for page_no, chars in image_pages:
        if chars < 200:
            report("FAIL", "Text in images", f"page {page_no} is mostly an image ({chars} characters of text)",
                   "Rebuild the resume from a text document; a scanned or image resume can't be read.")
        else:
            report("WARN", "Images", f"page {page_no} has an image (photo, logo or icon)",
                   "Fine if it's decoration; make sure no information exists only inside the image.")
    if total_lines and split_lines / total_lines > 0.15:
        report("WARN", "Single column", f"{split_lines} of {total_lines} lines have text side by side",
               "Use one column; sidebars and tables can be read out of order.")
    else:
        report("PASS", "Single column", "no multi-column layout detected")
    pages = len(reader.pages)
    if args.master:
        report("PASS", "Page fill", f"{pages} page(s); not checked for a master resume")
        return "\n".join(pages_text)
    if args.pages and pages != args.pages:
        report("WARN", "Page count", f"{pages} pages, target {args.pages}",
               "Trim or add ledger-backed bullets to reach the target.")
    # A single page should look full; on longer resumes the last page should be at least half used.
    if last_page_fill is not None and last_page_fill < (0.7 if pages == 1 else 0.5):
        report("WARN", "Page fill", f"last page is about {last_page_fill:.0%} full",
               "Add 2–4 evidence-backed bullets to fill it" + (", or tighten to one page fewer." if pages > 1 else "."))
    else:
        report("PASS", "Page fill", f"{pages} page(s); last page about {last_page_fill or 0:.0%} full")
    return "\n".join(pages_text)


def qn_t():
    from docx.oxml.ns import qn

    return qn("w:t")


def check_links(text, lines):
    def norm(value):
        value = value.lower().strip()
        value = re.sub(r"^(mailto:|tel:|https?://)", "", value)
        return re.sub(r"^www\.", "", value).rstrip("/")

    wanted = {}
    for email in EMAIL_RE.findall(text):
        wanted[f"mailto:{email}"] = email
    for line in lines[:6]:
        for match in PHONE_RE.finditer(line):
            digits = re.sub(r"\D", "", match.group(0))
            if len(digits) >= 9:
                wanted[f"tel:{digits}"] = match.group(0)
    for url in URL_RE.findall(text) + LINKEDIN_RE.findall(text):
        wanted[url] = url
    targets = [norm(t) for t in link_targets]
    target_digits = [re.sub(r"\D", "", t) for t in link_targets if t.lower().startswith("tel:")]
    missing = []
    for key, shown in wanted.items():
        if key.startswith("tel:"):
            ok = re.sub(r"\D", "", key) in target_digits
        else:
            ok = norm(key) in targets
        if not ok:
            missing.append(shown)
    shown_norms = {norm(k) for k in wanted}
    unexpected = [t for t in link_targets if not t.lower().startswith("tel:") and norm(t) not in shown_norms]
    if not wanted:
        return
    if missing:
        report("WARN", "Clickable links", f"not clickable: {', '.join(sorted(set(missing)))}",
               "Make these real hyperlinks (mailto:, tel:, https://) and keep the full text visible.")
    else:
        report("PASS", "Clickable links", f"{len(wanted)} email/phone/URL item(s) are clickable and point to their text")
    if unexpected:
        report("WARN", "Link targets", f"links to addresses not shown as text: {', '.join(unexpected[:4])}",
               "Show the full address as text too; some systems drop hyperlinks.")


def read_docx(path, args):
    from docx import Document

    doc = Document(path)
    body = doc.element.body
    if doc.tables:
        report("WARN", "Tables", f"{len(doc.tables)} table(s) found",
               "Move table content into plain paragraphs; some systems read tables out of order or skip them.")
    else:
        report("PASS", "Tables", "no tables")
    if body.xpath(".//w:txbxContent"):
        report("FAIL", "Text boxes", "text inside text boxes or shapes",
               "Move it into normal paragraphs; many systems skip text boxes.")
    if body.xpath(".//w:drawing"):
        report("WARN", "Images", "the document contains images",
               "Fine if decoration; make sure no information exists only inside an image.")
    if doc.sections[0]._sectPr.xpath("./w:cols[@w:num>1]"):
        report("WARN", "Single column", "the page uses more than one column", "Use a single column.")
    else:
        report("PASS", "Single column", "single column")
    for rel in doc.part.rels.values():
        if rel.reltype.endswith("/hyperlink") and rel.is_external:
            link_targets.append(rel.target_ref)
    if not args.master:
        report("WARN", "Pages and fonts", "not checked for a Word file",
               "Export the PDF you will send and run this check on it too"
               + (f" (target {args.pages} pages)." if args.pages else "."))
    header_text = " ".join(p.text for s in doc.sections for p in s.header.paragraphs).strip()
    if EMAIL_RE.search(header_text) or PHONE_RE.search(header_text):
        report("WARN", "Contact in header", "contact details sit in the page header",
               "Put them in the document body; some systems ignore headers and footers.")
    # Hyperlink text lives inside w:hyperlink, which paragraph.text may skip in older python-docx versions.
    return "\n".join("".join(t.text or "" for t in p._p.iter(qn_t())) for p in doc.paragraphs)


def is_heading_line(line):
    words = line.lower().strip(": ")
    return (len(line.split()) <= 4 and len(line) < 40 and any(stem in words for stem in HEADING_STEMS)
            and (line.isupper() or line.istitle()))


def contact_block(lines):
    # The lines after the name and before the first section heading; role headers and bullets never count.
    block = []
    for line in lines[1:9]:
        if is_heading_line(line):
            break
        block.append(line)
    return block


def has_location(block):
    for line in block:
        for segment in re.split(r"\s*(?:[|·•;\t]|\s{2,}| - | – )\s*", line):
            segment = segment.strip()
            if re.match(r"(?i)location\s*:\s*\S", segment) or re.fullmatch(r"(?i)remote(\s*\(.*\))?", segment):
                return True
            match = CITY_REGION_RE.match(segment)
            if match:
                region = match.group("region")
                if region in REGION_CODES or region.lower() in COUNTRIES:
                    return True
    return False


def check_text(text, path, args):
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    if len(text.strip()) < 300:
        report("FAIL", "Text extracts", f"only {len(text.strip())} characters of text",
               "The file is probably an image or uses broken fonts; rebuild it from a text document.")
        return
    report("PASS", "Text extracts", f"{len(text.split())} words extracted")
    if args.name:
        if args.name.lower() in " ".join(lines[:3]).lower():
            report("PASS", "Reading order", "name appears at the top")
        else:
            report("WARN", "Reading order", "name is not in the first lines of the extracted text",
                   "Put the name as the first line of the document, not in a header, image or sidebar.")

    spaced = sorted(set(SPACED_RE.findall(text)))
    if spaced:
        report("FAIL", "Letter-spaced text", f"extracts as: {', '.join(repr(s) for s in spaced[:4])}",
               "Remove letter-spacing / tracking from headings; set it to normal.")
    else:
        report("PASS", "Letter-spaced text", "none")

    top = "\n".join(lines[:12])
    for label, pattern, fix in (
            ("Email", EMAIL_RE, "Add a plain-text email address near the top."),
            ("Phone", PHONE_RE, "Add a phone number with country code, digits and spaces only."),
            ("LinkedIn", LINKEDIN_RE, "Add linkedin.com/in/your-name as text, not just an icon.")):
        match = next((m for m in pattern.finditer(top) if label != "Phone" or len(re.sub(r"\D", "", m.group(0))) >= 9),
                     None) or next((m for m in pattern.finditer(text)
                                    if label != "Phone" or len(re.sub(r"\D", "", m.group(0))) >= 9), None)
        if match:
            where = "top" if match.group(0) in top else "found, but not near the top"
            report("PASS" if where == "top" else "WARN", f"Contact: {label}", f"{match.group(0)} ({where})",
                   "" if where == "top" else "Move contact details to the top.")
        else:
            report("FAIL" if label == "Email" else "WARN", f"Contact: {label}", "not found", fix)
    if has_location(contact_block(lines)):
        report("PASS", "Contact: Location", "a city/country appears in the contact lines")
    else:
        report("WARN", "Contact: Location", "no 'City, Country' in the contact lines",
               "Add 'City, Country' (or 'Remote') to the contact line under your name.")

    headings = [line for line in lines if len(line.split()) <= 4 and len(line) < 40 and not line.endswith(".")
                and any(stem in line.lower() for stem in HEADING_STEMS)
                and (line.isupper() or line.istitle())]
    def is_standard(heading):
        # "Open-Source Projects" is fine (qualifier + standard name); "Education Credentials" is not.
        heading = heading.lower().strip(": ")
        return heading in STANDARD_HEADINGS or any(heading.endswith(" " + s) for s in STANDARD_HEADINGS)

    odd = [h for h in headings if not is_standard(h)]
    if odd:
        report("WARN", "Section headings", f"non-standard: {', '.join(odd)}",
               "Use standard names: Summary, Experience, Education, Skills, Certifications, Projects.")
    found = {h.lower().strip(": ") for h in headings if is_standard(h)}
    if not any(h for h in found if "experience" in h or "history" in h):
        report("WARN", "Section headings", "no 'Experience' heading found", "Name the jobs section 'Experience'.")
    elif not odd:
        report("PASS", "Section headings", f"standard: {', '.join(sorted(found))}")

    ranges = RANGE_RE.findall(text)
    formats = {name for name, pattern in DATE_FORMATS.items() for start, end in ranges
               if pattern.search(start) or pattern.search(end)}
    year_only = [r for r in ranges if not any(p.search(r[0]) for p in DATE_FORMATS.values())]
    if not ranges:
        report("WARN", "Role dates", "no date ranges found", "Give every role a start and end date, e.g. 'Aug 2021 – Present'.")
    elif len(formats) > 1 or (formats and year_only):
        report("WARN", "Role dates", f"{len(ranges)} date ranges in mixed formats: {', '.join(sorted(formats))}"
               + (" and year-only" if year_only else ""), "Use one format everywhere, e.g. 'Aug 2021 – Present'.")
    else:
        report("PASS", "Role dates", f"{len(ranges)} date ranges, consistent format")
    experience_lines, inside = [], False
    for line in lines:
        if line in headings:
            inside = "experience" in line.lower() or "history" in line.lower()
        elif inside:
            experience_lines.append(line)
    undated = [line for line in experience_lines if re.match(r"^[A-Z][\w &/-]+ (\||,|at|–|—) [A-Z]", line)
               and not RANGE_RE.search(line) and len(line) < 90]
    if ranges and undated and len(undated) <= 6:
        report("WARN", "Role lines", f"possible role lines without dates: {'; '.join(undated[:3])}",
               "Check each role has title, company and dates on the same line or the line right after.")

    check_links(text, lines)

    name = Path(path).name
    if re.search(r"(final|v\d|copy|\(\d\)|untitled|document)", name, re.I) or " " in name:
        report("WARN", "File name", name, "Use First-Last-Resume-YYYY-MM-DD.pdf (or -Company- for a tailored copy).")
    elif args.name and not all(part.lower() in name.lower() for part in args.name.split()[:2]):
        report("WARN", "File name", name, "Include the person's name, e.g. First-Last-Resume-YYYY-MM-DD.pdf.")
    else:
        report("PASS", "File name", name)

    if args.keywords:
        wanted = [k.strip() for k in Path(args.keywords).read_text(encoding="utf-8").splitlines() if k.strip()]
        def present(keyword):
            # Whole words only; short acronyms (SAM, LMS) must match case so "same" doesn't count as "SAM".
            flags = 0 if keyword.isupper() and len(keyword) <= 5 else re.I
            return re.search(rf"(?<![\w]){re.escape(keyword)}(?![\w])", text, flags) is not None

        missing = [k for k in wanted if not present(k)]
        covered = len(wanted) - len(missing)
        report("PASS" if not missing else "WARN", "Keyword coverage", f"{covered}/{len(wanted)} found"
               + (f"; missing: {', '.join(missing)}" if missing else ""),
               "Add a missing keyword only where the evidence supports it." if missing else "")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("file")
    ap.add_argument("--name", help="the person's full name, to check reading order and file name")
    ap.add_argument("--keywords", help="text file with one keyword or phrase per line")
    ap.add_argument("--pages", type=int, help="target page count (PDF only)")
    ap.add_argument("--master", action="store_true", help="master resume: skip page count and page fill")
    ap.add_argument("--text", action="store_true", help="also print the extracted text")
    args = ap.parse_args()
    path = Path(args.file)
    if path.suffix.lower() == ".pdf":
        text = read_pdf(path, args)
    elif path.suffix.lower() == ".docx":
        text = read_docx(path, args)
    else:
        sys.exit("give a .pdf or .docx file")
    check_text(text, path, args)

    order = {"FAIL": 0, "WARN": 1, "PASS": 2}
    print(f"ATS parse check: {path.name}\n")
    print("| Result | Check | Detail | Fix |\n|---|---|---|---|")
    for level, check, detail, fix in sorted(results, key=lambda r: order[r[0]]):
        print(f"| {level} | {check} | {detail} | {fix} |")
    counts = {level: sum(1 for r in results if r[0] == level) for level in order}
    print(f"\n{counts['FAIL']} fail, {counts['WARN']} warn, {counts['PASS']} pass. "
          "No checker can guarantee how a particular applicant tracking system will read a resume.")
    if args.text:
        print("\n--- extracted text ---\n" + text)
    sys.exit(1 if counts["FAIL"] else 0)


if __name__ == "__main__":
    main()
