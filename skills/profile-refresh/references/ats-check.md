# ATS check

An applicant tracking system (ATS) is the software employers use to collect applications. It turns a resume file
into text and fields (name, contact, jobs, dates). If that conversion goes wrong, a strong resume can look empty or
scrambled to a recruiter. This check catches the usual causes. **Never tell the owner a resume is "guaranteed to
pass".** Each system is different. Say "no problems found by the check".

## Run it

- **If you can run code:**
  `uv run scripts/ats_check.py <file.pdf|file.docx> --name "First Last" [--pages 2] [--keywords keywords.txt] [--text]`
  It prints a PASS / WARN / FAIL table with a fix for each item and exits non-zero on any FAIL. Always check the PDF
  the owner will actually send. A Word file can't show pages, page fill or fonts, so if you only have the DOCX, ask
  the owner to export the PDF and check that too. `--text` shows the extracted text, so you can read it the way an ATS would.
- **If you can't:** ask the owner to open the PDF, select all (Cmd/Ctrl+A), copy, and paste the text to you. Then walk
  the checklist below by reading that text.

## What it checks

| Check | Fails or warns when |
|---|---|
| Text extracts, reading order | Little or no text (scanned or image resume), or the name isn't at the top |
| Letter-spaced text | Headings extract as "C o n t a c t" |
| Contact details | Email, phone, LinkedIn URL or "City, Country" missing, not near the top, or only in the page header |
| Section headings | Non-standard names ("Education Credentials" → "Education"), or no Experience section |
| Roles and dates | Mixed date formats, or role lines without dates |
| Layout | Multiple columns, tables, text boxes, or text that exists only inside images |
| Fonts | Fonts not embedded in the PDF |
| Links | Email, phone or URLs shown as text but not clickable, or links pointing to addresses not shown as text |
| Pages | Page count differs from the target; a one-page resume under ~70% full, or a longer one whose last page is under half full |
| File name | Spaces, "final", "v2", "copy", or no name in it |
| Keywords (optional) | Posting keywords missing from the text (whole words only; short all-caps acronyms must match case) |

## Second opinion (optional)

The open-source [OpenResume parser](https://open-resume.com/resume-parser) (AGPL-3.0) reads a PDF and shows the fields
it found. It says it runs entirely in the browser without uploading the file. Offer it, and let the owner decide
whether to use it, since it's a third-party website. Ask them to compare the fields it shows with the resume.

## Report

Show FAILs first, then WARNs, each with its fix, and say which ones you've already fixed. A WARN can be fine on purpose
(for example a photo for a market that expects one). Say so, and leave the choice to the owner.
