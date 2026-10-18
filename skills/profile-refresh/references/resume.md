# Resume

There are two kinds, and the order matters:

- **Master resume.** Every evidence-backed bullet, in the long, detailed wording. No page limit, and **never sent to
  employers**. It's the single source of truth: LinkedIn mirrors it (same facts, same detailed wording), and every
  run updates it first. File: `<First>-<Last>-Master-Resume.md/.docx/.pdf`. If the owner uses career-ops, its `cv.md`
  plays this role (see [career-ops.md](career-ops.md)).
- **Targeted resume.** Built *from the master*, never from an earlier targeted copy. Choose the bullets for one
  purpose (a posting, or a general version for a job type), aim for a page target, then run the ATS check. File:
  `<First>-<Last>-Resume-<Company or purpose>-<YYYY-MM-DD>.md/.docx/.pdf`. For a specific posting, follow
  [tailor.md](tailor.md).

**Resume and LinkedIn must match on facts**: titles, employers, dates and claims. Wording and level of detail can
differ. Content comes only from the evidence ledger. Layout never decides content: if a page looks empty, add
*evidence-backed* bullets from the master; never pad.

## 1. Ask (one or two at a time)

1. **Style.** Offer three choices:
   - **(a) Polished, keeping your look.** Keep the owner's current fonts, colours and section order, and tidy
     spacing, alignment and consistency.
   - **(b) Plain ATS.** Single column, one font, black text, simple headings with a rule under them, no colour bands.
     This is the safest for online application systems.
   - **(c) Match a sample.** The owner provides a resume whose *layout* they like. Copy only its layout: fonts,
     colours, heading style, order and margins. Never copy its wording or content.
2. **Length** (targeted resumes only). Ask for a target page count (usually 1 page for under ~5 years of
   experience, 2 for more). Then fit it with the loop below.
3. **Paper.** US Letter or A4 (A4 outside North America, unless they apply mainly to US companies).

## Page-fit loop (targeted resumes)

1. Start from the master and rank its bullets for this purpose: relevance to the target first, then recency.
2. Build, export the PDF, and run the ATS check with `--pages <target>`.
3. **Too long?** Drop the lowest-ranked bullet (usually the oldest and least relevant), rebuild and re-check. Repeat
   one bullet at a time. Never shrink the font below 9.5 pt or the margins below 0.5 in to make it fit.
4. **Last page under half full** (or a single page under ~70%)? Add back the highest-ranked dropped bullet and re-check.
5. Tell the owner which master bullets were dropped and why ("older, not relevant to this posting").

## 2. Write it as Markdown first

Write the resume in this simple format. It's easy to show as a draft, and the builder script turns it into Word:

```markdown
# Full Name
Headline (same as LinkedIn; a tailored copy may adjust it to the role)
City, Country | email@example.com | +00 00 000 0000 | linkedin.com/in/name

## Summary
Two or three lines.

## Experience
### Job Title | Employer, City | Mon YYYY – Mon YYYY
- **Label:** action + what + verified outcome.

## Education
- Degree, School, YYYY

## Skills
- **Group:** skill, skill, skill
```

Use standard section names (Summary, Experience, Education, Skills, Certifications, Projects), one date format
everywhere ("Aug 2021 – Present"), and contact details as plain text in the body. Show the draft and get the OK.

## 3. Build the files (DOCX + PDF)

The output is a **Word file** (safest for application systems, and the owner can edit it) plus a **PDF** to send.
Name them `<First>-<Last>-Resume-<YYYY-MM-DD>.docx/.pdf`, saved next to the original. Never overwrite the original.

- **If you can run code:** use `scripts/resume_docx.py` from this skill's folder:
  `uv run scripts/resume_docx.py resume.md -o <name>.docx --style plain|polished [--font Arial] [--accent C55A11]
  [--band EDEDED] --paper letter|a4 [--pdf]`. Always pass `--paper` (the default is Letter). Set `--font`, `--accent`
  and `--band` to match style (a) or (c).
  `--pdf` uses LibreOffice if it's installed. Otherwise ask the owner to open the .docx in Word, Pages or Google
  Docs and export it as PDF under the same name. If `uv` is missing, ask the owner before installing anything; the
  alternative is `python3 -m pip install --user python-docx` and then `python3 scripts/resume_docx.py …`.
- **If you can't run code:** give the owner the Markdown and these steps: paste it into Word or Google Docs, use
  Heading styles for the name and section titles, bullets for the lists, one font, then export to PDF.

Then run the [ATS check](ats-check.md) on the PDF (and the DOCX) and fix any FAIL before showing the result. For the
master, add `--master` (no page target).

## Layout rules (any tool)

- One column, no tables, text boxes, icons for contact details, or text inside images.
- Keep each **role header** (title, employer, dates) together with its first bullet, but let bullet lists flow across
  pages. Never keep a whole role block or section (Skills included) together: three overflowing lines then push the
  whole block onto a new page, leaving a gap and adding a page.
  In HTML/CSS: `break-inside: avoid; break-after: avoid` on headers only, never on a whole role or section.
- **Links are clickable** in both the DOCX and the PDF: email (`mailto:`), phone (`tel:`), LinkedIn, GitHub or
  portfolio, and project URLs. Still show the full address as text (`linkedin.com/in/name`, not "LinkedIn"),
  because some parsers drop hyperlinks. The builder does both. In HTML, use `<a href>` with the full URL as the
  link text. Word, Pages and Google Docs keep links when exporting to PDF.
- Letter-spacing (tracking) on headings is off, or text extracts as "C o n t a c t".
- Colour bands and coloured titles are fine as long as the text is real text. Keep the text-on-band contrast high.
