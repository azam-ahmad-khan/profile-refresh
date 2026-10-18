> Simulated run of the profile-refresh skill (option 3, tailor to a job posting) with a fictional person, Layla Haddad.
> Her replies come from `owner-answers.md`; nothing here describes a real person, employer or job.
> Recorded before the builder made links clickable. Rebuilding this resume today also passes "Clickable links".

# Dry run: tailor Layla's resume to the Northwind posting (2026-10-18)

Mode: no browser, no LinkedIn changes, career-ops not installed. The AI can run code (`uv`), but LibreOffice is
missing, so no PDF was built. Working files went to a scratch `tailor-run/` folder, not the repo.

## 1. Opening

**AI:** What would you like to do today? (1) Refresh LinkedIn and resume, (2) update your resume, (3) tailor your
resume to a job posting, (4) check your resume for application systems (ATS), (5) a periodic check-up.
**Layla:** "Tailor my resume to this Northwind posting." (`job-posting-northwind.md`)

**AI:** Where do you keep your career files? If you have a `career-notes.md`, I'll pick up from it.
**Layla:** "Use this sample-profile folder." No `career-notes.md` yet.

→ No evidence ledger exists, so `tailor.md` step 1 says build one first (first run, step 2).

**AI:** Quick context: which roles are you aiming for, and is this search private from your school?
**Layla:** Instructional Designer, Learning Experience Designer, e-Learning Developer; leaning toward instructional
design and e-learning. Yes, quietly; still teaching at Crescent Bay.

## 2. Discover: evidence ledger

Read: the latest approved base resume (`Layla-Haddad-Resume-2026-10-18.md`), the original `resume.md`, the LinkedIn
snapshot, `evidence/appraisal-2025.md`, `evidence/certificate.md` and the posting. Open items, asked one or two at a time:

**AI:** Your resume says you ran a Storyline workshop in May 2026, and that you trained teachers on the learning
platform. Neither is in the appraisal. Can you confirm both?
**Layla:** "In May 2026 I ran a two-hour Storyline workshop for 12 colleagues." And yes, she trained teachers on the
platform; the rollout itself was led by the Head of Digital Learning.

**AI:** Your start date: the resume says Aug 2021, LinkedIn says Sep 2021. Which is right? And which grades do you teach?
**Layla:** August 2021, the contract start; LinkedIn is wrong. Grades: "I'm not sure."

**AI:** The Olympiad coaching: anything to add, and may I name the student?
**Layla:** She counts the Olympiad medal as recognition. "Please don't name students."

**AI:** What's your official job title?
**Layla:** The contract says "Teacher of Chemistry".

Ledger summary (full table in `career-notes.md`):

| Claim | Source | Status |
|---|---|---|
| 42 Storyline lab simulations, Grade 10, adopted by all 3 classes | appraisal 2024–25 | Verified |
| Storyline 360 Essentials, Mar 2025, ID ABC-123-EXAMPLE | certificate | Verified |
| Supported blended-learning rollout | appraisal | Verified |
| Mentored two newly qualified teachers | appraisal | Verified |
| Trained teachers on the learning platform | Layla | Owner-confirmed |
| Two-hour Storyline workshop for 12 colleagues, May 2026 | Layla (sent folder) | Owner-confirmed |
| Title "Teacher of Chemistry", Aug 2021 – Present | contract, per Layla | Owner-confirmed |
| Grades 9–12 | resume.md | Open (not sure) |
| IGCSE pass rate 90% | appraisal: a 2025–26 *goal*; 2025 actual was 78% | Never publish |
| "Improved results by 35%" (LinkedIn) | no source | Off |
| "Project Atlas", "Kitebridge Learning" | resume.md | Confidential, never publish |

## 3. Requirement table

| Requirement | Must / Nice | Keywords | Evidence (ledger) | Transferable from | Gap? |
|---|---|---|---|---|---|
| 2+ years designing learning experiences | Must | learning experiences, instructional design | Teaching since Sep 2017; 42 Storyline simulations (Verified) | Lesson and unit design (posting accepts classroom) | No |
| Articulate Storyline and Rise 360 | Must | Articulate Storyline, Rise 360 | Storyline: 42 simulations + certificate (Verified) | none | Rise 360: ask |
| Storyboarding and scripting interactive modules | Must | storyboarding, scripting, interactive modules | 42 interactive simulations (Verified); "storyboarding" only in base Skills line | Building the simulations | Storyboarding/scripting: ask |
| ID models (ADDIE, SAM) and learning objectives | Must | ADDIE, SAM, learning objectives | none yet | Unit planning | Ask |
| Assessment design and measuring learning outcomes | Must | assessment design, learning outcomes | "assessment design" in base Skills (owner's claim) | Classroom assessment | Measuring: ask |
| Publishing SCORM packages to an LMS | Must | SCORM, LMS | none yet | Uses the school learning platform | Ask |
| Train-the-trainer sessions | Nice | train-the-trainer | Workshop for 12 colleagues; trained teachers on the platform | Training teachers, who teach others | Partial |
| Video editing (Camtasia) | Nice | Camtasia | none | none | Ask |
| Adult learners | Nice | adult learners | Workshop; mentoring two new teachers | Colleagues are adult learners | No |

## 4. Gap questions

**AI:** The posting asks for Rise 360. Have you used it, even briefly?
**Layla:** "No, only Storyline."

**AI:** It also asks for storyboarding and scripting interactive modules. Did you plan the simulations on paper or in a
document before building them?
**Layla:** "I'm not sure." → stays Open; "storyboarding" comes **off** the resume (it was only a Skills-line claim).

**AI:** Have you used a design model such as ADDIE or SAM, or written learning objectives?
**Layla:** "I'm not sure. I write learning objectives for every unit, but I've never used those names."

**AI:** Have you measured whether the simulations improved learning?
**Layla:** "I compare quiz scores before and after the simulations, informally. No report."

**AI:** Did you upload your Storyline work to a learning platform, for example as SCORM packages?
**Layla:** "Yes, I published my simulations to the school LMS as SCORM packages."

**AI:** Camtasia or other video editing? And have you trained adults or trainers?
**Layla:** Camtasia: "No." Adults / train-the-trainer: the May 2026 workshop for 12 colleagues.

Honest ways to address the remaining gaps (not on the resume):
- **Rise 360, storyboarding, scripting:** a small proof-of-work project: one Rise 360 module with its storyboard and
  script, published as SCORM to a free LMS sandbox. Rise has a free trial.
- **ADDIE / SAM:** in the cover letter, say she writes objectives per unit and checks results with before/after
  quizzes, without claiming the model names. A short ADDIE course would let her use the term truthfully.
- **Camtasia:** nice-to-have only; skip unless she wants it.

## 5. Draft: diff against the base resume

| Change | Line |
|---|---|
| Reworded | Headline → "Teacher of Chemistry \| E-learning & instructional design \| Articulate Storyline, SCORM" |
| Reworded | Summary → 9 years designing learning experiences (from Sep 2017 start), Storyline, objectives, SCORM, training colleagues |
| Reworded | Title → "Teacher of Chemistry" (contract); "(Grades 9–12)" dropped as unconfirmed |
| Reworded | "42 interactive lab simulations" → "42 interactive modules (lab simulations)" |
| Added from ledger | LMS publishing: SCORM packages to the school LMS (Owner-confirmed) |
| Added from ledger | Learning design: objectives for every unit; before/after quiz comparison (Owner-confirmed, no numbers) |
| Added from ledger | Workshop: "for 12 colleagues" (Owner-confirmed) |
| Moved | Training and rollout bullets now follow the must-have bullets |
| Removed | Olympiad coaching (not relevant to this role); "storyboarding" and "lab safety" from Skills |

Confidentiality check: no internal system or vendor names ("the school LMS", not "Project Atlas"); no student or
colleague named; the rollout is "supported", since the Head of Digital Learning led it; no exam-result numbers.
Kept off on purpose: "both new teachers passed induction" (an HR outcome about two identifiable colleagues).

**AI:** Here's the Northwind draft. It keeps "Teacher of Chemistry" in the headline and doesn't mention a job search.
OK to build the Word file?
**Layla:** Yes (her rule: yes, unless it announces a job search or a move away from teaching).

## 6. Final resume (Markdown)

```markdown
# Layla Haddad
Teacher of Chemistry | E-learning & instructional design | Articulate Storyline, SCORM
Dubai, UAE | layla.example@example.com | +971 50 000 0000 | linkedin.com/in/layla-haddad-example

## Summary
Chemistry teacher with 9 years of designing learning experiences, in the classroom and online. Builds interactive e-learning in Articulate Storyline, writes learning objectives for every unit, publishes modules to the school LMS as SCORM packages, and has trained colleagues in Storyline.

## Experience
### Teacher of Chemistry | Crescent Bay International School, Dubai | Aug 2021 – Present
- **E-learning:** Built 42 interactive modules (lab simulations) in Articulate Storyline for the Grade 10 curriculum, adopted by all three Grade 10 chemistry classes.
- **LMS publishing:** Published the simulations to the school LMS as SCORM packages.
- **Learning design:** Write learning objectives for every unit, and compare quiz scores before and after the simulations to check learning outcomes.
- **Training adults:** Ran a two-hour Articulate Storyline workshop for 12 colleagues (May 2026).
- **Digital rollout:** Supported the school's blended-learning rollout and trained teachers to use the learning platform.
- **Mentoring:** Mentored two newly qualified teachers through their induction year.
### Science Teacher | Al Noor Academy, Sharjah | Sep 2017 – Jul 2021
- Taught integrated science to Grades 7–9.
- Ran the after-school robotics club.

## Education
- PGCE (Secondary Science), University of Nottingham, 2017
- BSc Chemistry, American University of Sharjah, 2016

## Certifications
- Articulate Storyline 360 Essentials, Articulate, Mar 2025 (Credential ID ABC-123-EXAMPLE)

## Skills
- **E-learning:** Articulate Storyline 360, SCORM, LMS publishing, Google Classroom
- **Learning design:** learning objectives, assessment design, curriculum design
- **Training:** staff workshops, mentoring new teachers
```

## 7. Build and ATS check

Style: plain ATS, one page (Layla). Paper: she wasn't sure, so A4 (outside North America). Keywords file
`northwind-keywords.txt`, the posting's must-haves, one per line: learning experiences, instructional design,
Articulate Storyline, Rise 360, storyboarding, scripting, interactive modules, ADDIE, SAM, learning objectives,
assessment design, learning outcomes, SCORM, LMS.

```
uv run scripts/resume_docx.py Layla-Haddad-Resume-2026-10-18.md -o Layla-Haddad-Resume-2026-10-18.docx --style plain --paper a4 --pdf
uv run scripts/resume_docx.py Layla-Haddad-Resume-Northwind-2026-10-18.md -o Layla-Haddad-Resume-Northwind-2026-10-18.docx --style plain --paper a4 --pdf
→ wrote …docx
→ PDF: no LibreOffice found. Open the .docx in Word, Pages or Google Docs and export it as PDF …
uv run scripts/ats_check.py <file>.docx --name "Layla Haddad" --pages 1 --keywords northwind-keywords.txt
```

**Before** (base resume DOCX): 0 fail, 1 warn, 12 pass.

| Result | Check | Detail |
|---|---|---|
| WARN | Keyword coverage | 3/14 found; missing: learning experiences, instructional design, Rise 360, scripting, interactive modules, ADDIE, SAM, learning objectives, learning outcomes, SCORM, LMS |
| PASS | Tables, single column, text (193 words), reading order, letter-spacing, email, phone, LinkedIn, location, headings, role dates (2, consistent), file name | |

**After** (Northwind DOCX): 0 fail, 1 warn, 12 pass.

| Result | Check | Detail |
|---|---|---|
| WARN | Keyword coverage | 9/14 found; missing: Rise 360, storyboarding, scripting, ADDIE, SAM |
| PASS | Tables, single column, text (248 words), reading order, letter-spacing, email, phone, LinkedIn, location, headings, role dates (2, consistent), file name | |

**Keyword coverage before → after: 3/14 → 9/14.**

Remaining gaps:
- **Honest, no evidence:** Rise 360 (no), ADDIE and SAM (never used the names). Address in the cover letter or with
  the proof-of-work project; don't add them.
- **Could become fixable:** storyboarding and scripting, if Layla finds a storyboard or script she wrote. Note that
  "storyboarding" was *in* the base resume and was removed because she couldn't confirm it, so coverage of that
  keyword went down on purpose.

Not checked, because there's no PDF: page count (`--pages` is ignored for DOCX), page fill, embedded fonts. Layla
should export the DOCX to PDF in Word and the check should be rerun on the PDF she will send. No problems found by
the check so far; that is not a guarantee for any particular system.

## 8. Log

`career-notes.md` → *Tailored versions*: 2026-10-18 · Northwind Learning, Instructional Designer ·
`Layla-Haddad-Resume-Northwind-2026-10-18.docx` (PDF pending) · 3/14 → 9/14 · open gaps: Rise 360, ADDIE, SAM
(honest), storyboarding, scripting (open). Open questions: storyboarding evidence; grades taught.

## Notes from the run (for the skill author)

- The keyword check is a plain substring match: in a probe, a line "Made the same short films" counted as **both**
  "SAM" and "LMS" found. Coverage for short acronyms can be a false PASS.
- Location also passed with "Dubai, UAE" removed from the contact line; the regex matched a "Word, Word" pair elsewhere
  near the top (e.g. "School, Dubai").
- The base resume was "approved", yet it carried "storyboarding" (unconfirmed) and "(Grades 9–12)" (unconfirmed).
  The skill doesn't say whether an approved base counts as Owner-confirmed; this run kept unasked base claims and
  dropped the ones Layla couldn't confirm when asked.
