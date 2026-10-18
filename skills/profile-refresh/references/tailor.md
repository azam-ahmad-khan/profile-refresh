# Tailor the resume to one job posting

Tailoring means retelling real work in the employer's language: reorder, re-emphasize, and use the posting's words
where they're truthful. It never means adding skills or results the owner doesn't have. Anything the posting wants
that the evidence doesn't show becomes a **question**, never invented text.

## If career-ops is installed

[career-ops](https://github.com/career-ops-hq/career-ops) already tailors a CV PDF per job, extracts the posting's
keywords, and has a fact-check that blocks numbers missing from the owner's sources. Tell the owner that plainly and
offer two options: hand the tailoring to career-ops (it reads the same `cv.md`), or do it here and keep its outputs in
the career-ops folders. What this skill adds either way is the evidence table in step 2, the owner questions in step 3,
and the [ATS check](ats-check.md) with keyword coverage.

## Steps

1. **Read the posting** (link or pasted text) and the **master resume** ([resume.md](resume.md)). Always start from the
   master, never from an earlier targeted copy. If there's no master yet, build it first from the evidence ledger. If
   there's no ledger either, do the short setup in SKILL.md.
2. **Requirement table.** One row per requirement:

   | Requirement | Must / Nice | Keywords | Evidence (ledger) | Transferable from | Gap? |
   |---|---|---|---|---|---|

   "Transferable from" is real work that shows the same skill under another name. For example, a teacher's
   "differentiated lesson plans" maps to an instructional designer's "learner personas". Name the source each time.
3. **Ask about the gaps**, one or two at a time: "The posting asks for X. Have you done anything like it, even
   small?" Add confirmed answers to the ledger. If the answer is no, it stays off the resume. Suggest how to address
   it honestly instead (cover letter, proof-of-work project, a course).
4. **Select and rewrite** in the resume Markdown format ([resume.md](resume.md)): pick master bullets that serve the
   must-haves and put them first, echo the posting's words where the evidence supports them, adjust the summary and
   headline line to this role, and fit the page target with the page-fit loop (usually 2 pages). Facts must stay
   identical to the master and LinkedIn. Run the [confidentiality check](confidentiality.md), then show a
   diff-style draft (moved / reworded / added from ledger / removed) and get the OK. Derived facts (e.g. "9 years"
   worked out from dates) are fine, but say how you worked them out. List the master bullets you dropped and why.
5. **Save a new set per company** next to the base resume: `<First>-<Last>-Resume-<Company>-<YYYY-MM-DD>` as `.md`
   (the source), `.docx` and `.pdf`. Never overwrite the base resume.
6. **ATS check with keyword coverage.** Put the posting's must-have keywords in a text file (one per line) and run the
   check on the master (with `--master`, the "before") and on the new file (with `--pages`, the "after"). Report
   "keyword coverage before → after" and the remaining gaps, and say which gaps are honest (no evidence) and which
   can be fixed. If a new answer from the owner added evidence, add it to the master too.
7. **Log it** in `career-notes.md` → *Tailored versions*: company, role, date, file, coverage, open gaps.
