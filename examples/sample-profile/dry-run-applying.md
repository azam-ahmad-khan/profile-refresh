> Simulated run: Layla Haddad is a fictional person, and every answer comes from `owner-answers.md`.
> The Northwind portal is the text stand-in `application-form-northwind.md`; LinkedIn steps are written actions, not a real browser.
> Recorded before "Reach out" moved ahead of "Apply" (a referral has to come before Submit). The steps are otherwise current.

# Dry run: applying to jobs (profile-refresh, option 6)

Date: 2026-10-18 (Sunday), with time moving forward as the answers say. Working files went to a scratch `apply-run/`
folder: master resume, Northwind resume (.md + .docx), `keywords-northwind.txt` and `career-notes.md`.

## 1. Opening menu and set-up

**AI:** Hi Layla. What would you like to do today? Refresh LinkedIn, update your resume, tailor it to a job, check it
for application systems, a check-up, or apply to a job from start to finish?
**Layla:** Apply to jobs. I found three postings (Northwind, BrightPath, Fabrikam).

**AI:** Where do you keep your career files and notes?
**Layla:** Use this sample-profile folder. *(No `career-notes.md` there, so this is a first run: short set-up first.)*

**AI:** Do you have a master resume? That's the full version with everything in it, which you never send out.
**Layla:** I only have the resume we made last time (`Layla-Haddad-Resume-2026-10-18.md`).

Mode: browser mode for the Northwind portal; LinkedIn changes are described as written actions.

## 2. Short set-up: goal and evidence

| Asked | Layla |
|---|---|
| Target roles | Instructional Designer, Learning Experience Designer, e-Learning Developer |
| Which way should the profile lean? | Toward instructional design / e-learning |
| Job-hunting? Employed? | Yes, quietly. Still teaching at Crescent Bay |
| May your employer know? | "No. My principal follows me on LinkedIn." |
| Location / remote | Dubai; open to remote or hybrid |
| Evidence besides the resume | The appraisal and the certificate in `evidence/`. Nothing else written down |
| Work-extraction prompt (an AI tool at work)? | School doesn't allow AI on school email. From her sent folder: "In May 2026 I ran a two-hour Storyline workshop for 12 colleagues." |
| A normal week / what people come to you for | 22 periods; colleagues come for "anything Storyline or simulations" |
| A problem you're proud of solving | Students couldn't do some labs safely at home during revision, so she built simulations |
| Recognition | The appraisal comments; the Olympiad medal |

Open items from the evidence, asked one or two at a time:

| Item | Layla | Ledger |
|---|---|---|
| "90% pass rate" (original resume) | "That was my goal." Happened? "No. 81% in 2026." | Open: a goal, and employer data. Off everywhere |
| "35%" on LinkedIn | "I don't remember where that came from." | Open: remove from LinkedIn |
| "Project Atlas" / Kitebridge | Internal LMS name; contract not public | Confidential: write "the school LMS" |
| Who led blended learning? | Mr. Mensah, Head of Digital Learning; she trained teachers | Verified, her part only |
| Name the Olympiad student? | "Please don't name students." | Keep "coached students for the UAE Chemistry Olympiad" |
| Start date | August 2021 (contract). LinkedIn is wrong | Fix LinkedIn |
| Official title | "Teacher of Chemistry" | Fix LinkedIn |
| Certificate issuer | Articulate | Verified with credential ID |

`career-notes.md` started from the template, with the evidence ledger and an empty *Applications* table.

## 3. Foundation check (applying.md)

| Item | Status found | Action |
|---|---|---|
| Privacy pass | Not done | Do it now |
| Public visibility on | "Visible to everyone" already | Ask |
| LinkedIn matches the master on facts | No: "Chemistry Teacher", Sep 2021, "35%" claim, no certificate, old headline | Sync |
| Master resume | Missing | Build from the ledger |
| `career-notes.md` + Applications table | Started in step 2 | Done |

**Privacy pass**
- *Share profile updates with network:* On → recommend Off, so edits don't ping her network (her principal included).
  **Layla:** Yes. *(Settings → Visibility → toggled Off → reloaded: Off.)*
- *Public profile visibility:* **AI:** Since you're applying, being visible helps recruiters find you on Google. Keep it on?
  **Layla:** "Fine to turn it on. I've decided to apply openly now, and I've told my principal."
  → No change needed (already visible). **Note:** this contradicts "quietly" an hour earlier; the newest answer wins
  and is logged under *Decisions*. Drafts still avoid "aspiring" or "→" wording, because she said she'd reject any draft
  that announces a move.
- *Per-form "Notify network":* checked Off on every form below.
- *Open to Work:* **AI:** Recruiters only, or all members (the green photo frame)? **Layla:** I'm not sure.
  → Default while employed: **Recruiters only**, switched on with the titles below.

**LinkedIn sync** (one draft, one yes, one save each; positions first because adding one can overwrite the headline)

```
Section: Experience · Crescent Bay        (change)
Current:  Chemistry Teacher · Sep 2021 – Present · "Passionate educator who improved student results by 35%."
Proposed: Teacher of Chemistry · Aug 2021 – Present · bullets as in the master (42 simulations, workshop for
          12 colleagues, blended-learning support, mentoring, Olympiad coaching)
Evidence: contract title + date (owner-confirmed); appraisal (verified); sent folder (owner-confirmed)
Confidentiality: removed "35%" (no source); LMS not named; rollout leader not named
Save this to LinkedIn?
```
**Layla:** Yes. *(Saved, Notify network off; reloaded: title, Aug 2021 and bullets shown; headline unchanged.)*

| Change | Proposed | Layla | Verified after reload |
|---|---|---|---|
| Experience · Al Noor | Sep 2017 – Jul 2021; 2 bullets (integrated science 7–9, robotics club) | Yes | dates + bullets |
| Certification (add) | Articulate Storyline 360 Essentials · Articulate · Mar 2025 · ABC-123-EXAMPLE | Yes | shown, notify off |
| Headline | Teacher of Chemistry \| E-learning & instructional design \| Articulate Storyline lab simulations (95/220) | Yes | saved |
| About | 3 short paragraphs: who she is; 42 simulations + workshop; why (safe practice, colleagues building their own); Skills line. No "looking for" line | Yes | 3 paragraphs kept |
| Top skills | Articulate Storyline, E-Learning, Storyboarding, Assessment Design, Curriculum Design | Yes | saved |
| Open to Work | 3 titles above, Recruiters only, Dubai + remote/hybrid | Yes | saved as typed *(simulated; a real run reads back LinkedIn's mapped names)* |

**Master resume** built as `Layla-Haddad-Master-Resume.md/.docx` from the ledger (the approved resume's facts, plus
the 12-colleague workshop and the reason the simulations exist). Style asked: **Layla:** Plain ATS. One page.
Paper? **Layla:** I'm not sure → A4 (outside North America). ATS check (`--master`): 0 FAIL.

## 4. Find

**AI:** Want me to set LinkedIn job alerts for your three titles in Dubai + remote? Your field also has sector job
boards (for example professional bodies for learning and development). **Layla:** I'm not sure. → Left as a reminder.

## 5. Decide (before any tailoring)

| Posting | Fit (1–5) | Live | Genuine | Verdict |
|---|---|---|---|---|
| Northwind · Instructional Designer | **3**: covers 2+ yrs designing learning (classroom counts), Storyline, assessment design; partial on objectives/outcomes; SCORM unknown; **no** Rise 360, ADDIE/SAM | No posted date; the form is on Northwind's own careers portal | Company portal, no fees, no ID requests | **Go** |
| BrightPath · e-Learning Content Developer | n/a | n/a | **No.** AED 750 fee, passport and bank details to a Gmail address, "no interview", AED 45,000/month | **Don't apply.** Don't send anything; if you're curious, check BrightPath's own website for the role |
| Fabrikam · Senior Data Scientist | **1**: no data-science years, Python/SQL/ML, causal inference or quantitative MSc in the ledger | – | Looks genuine | **Skip.** A core gap, and not one of your target roles |

**Layla** agreed. Both skips were logged under *Decisions*, not in *Applications*.

## 6. Tailor (Northwind)

| Requirement | Must/Nice | Evidence (ledger) | Transferable from | Gap? |
|---|---|---|---|---|
| 2+ yrs designing learning | Must | 9 yrs teaching (Sep 2017 – now) | lesson and unit design | no |
| Storyline and Rise 360 | Must | Storyline: 42 sims + certificate | – | **Rise** |
| Storyboarding, scripting interactive modules | Must | storyboarding (skill, approved resume) | – | scripting? |
| ADDIE/SAM, learning objectives | Must | asked below | objectives per unit | ADDIE/SAM? |
| Assessment design, measuring outcomes | Must | assessment design (skill) | quiz comparison (asked) | partly |
| SCORM to an LMS | Must | asked below | – | ? |
| Train-the-trainer; adult learners | Nice | workshop, 12 colleagues | – | no |
| Camtasia | Nice | asked below | – | ? |

Gap questions, two at a time:
- **AI:** Have you uploaded Storyline work to a learning platform, as SCORM? **Layla:** Yes, to the school LMS as SCORM packages.
- **AI:** Rise 360? **Layla:** No, only Storyline.
- **AI:** ADDIE, SAM or other design models? **Layla:** I'm not sure. I write learning objectives for every unit, but I've never used those names.
- **AI:** Do you measure what students learned? **Layla:** I compare quiz scores before and after the simulations, informally. No report.
- **AI:** Camtasia or video editing? **Layla:** No.
- **AI:** Do you write scripts for the simulations (on-screen text, narration)? **Layla:** I'm not sure. → Stays off.

New answers (SCORM, objectives, quiz comparison) added to the ledger **and** the master; the LinkedIn Crescent Bay
role got one matching bullet (draft → Yes → saved → verified).

Diff, master → `Layla-Haddad-Resume-Northwind-2026-10-18.md`:
- **Headline line:** "…| Articulate Storyline, SCORM, assessment design"
- **Summary:** "nine years of teaching and designing classroom learning" (derived: Sep 2017 – Jul 2021 = 47 months +
  Aug 2021 – Oct 2026 = 63 months = 110 months, about 9 years)
- **Moved up:** 42 simulations; **added from ledger:** SCORM bullet; objectives + "informal check on learning outcomes"
- **Reworded:** "Training" → "Train-the-trainer" (the posting's words; same facts)
- **Removed:** Olympiad coaching (not relevant; one page). Al Noor's two bullets merged into one
- **Caught in my own draft and removed:** "Storyboarded and built 42…" (she lists storyboarding as a skill but never
  said she storyboarded these), "design the assessments" for every unit, "Designed and ran" the workshop (she said
  "ran"), and "led by the Head of Digital Learning" (identifies a colleague)

**Layla:** Yes. Built the DOCX (plain, Arial, A4). PDF: no LibreOffice here. **AI:** Could you export the PDF from Word?
**Layla:** I'm not sure. → The DOCX is the file to upload (the portal accepts it); page count stays unverified.

**ATS check** with `keywords-northwind.txt` (13 must-have keywords): 0 FAIL. WARN: pages not checkable on a DOCX.
Keyword coverage **5/13 (master before) → 9/13 (targeted)**. Missing: Rise 360, ADDIE, SAM (no evidence, honest
gaps) and scripting (open question). Logged under *Tailored versions*.

## 7. Apply (Northwind careers portal)

**AI:** Two ways to apply: Easy Apply (inside LinkedIn, quick) or the company's own site (slower, often needs an
account). This one is on Northwind's own site. OK for me to fill it in? **Layla:** OK to fill.

- **Step 0, "Create an account":** stopped. **Layla** created the account and typed the password herself.
- **Knock-out questions:** worked out with her before typing anything.
  - Visa: **Layla:** My residence visa is sponsored by my school; a new employer would have to sponsor a new one. → **No**.
  - Years of instructional design. Two honest sums: e-learning design evidenced from the 2024–25 appraisal year
    (Sep 2024 – Oct 2026) = **2 years**; all teaching = about 9 years. **AI:** Which do you want to give?
    **Layla:** I'm not sure. → Filled **2** (the evidenced minimum; meets "2+"), flagged on the review page.
  - Salary: **Layla:** I'm not sure. Around AED 18,000 a month? What's normal? **AI:** I won't guess. I haven't checked
    any public salary source in this run, so I can't tell you what's normal. Check a recent UAE salary guide from a
    recruiter and LinkedIn's salary insights for "Instructional Designer, Dubai" before submitting. → Her own figure
    filled, flagged.
  - Notice: **Layla:** Two months, per my contract.
- **Cover letter?** **Layla:** Yes, short.

**Review page, stopped before [Submit application]:**

| Field | Filled | Source / note |
|---|---|---|
| First name / Last name | Layla / Haddad | resume |
| Email / Phone | layla.example@example.com / +971 50 000 0000 | resume |
| City | Dubai | resume |
| LinkedIn URL | linkedin.com/in/layla-haddad-example | resume |
| Resume upload | Layla-Haddad-Resume-Northwind-2026-10-18.docx | DOCX because no PDF yet |
| Current title (auto-filled) | was "Teacher of Chemistry \| E-learning & instructional" (cut off) → **fixed to "Teacher of Chemistry"** | contract title |
| a. Authorized without sponsorship? | **No** | her visa answer |
| b. Years of instructional design | **2** ⚑ | evidenced minimum; change to 9 only if you count classroom design |
| c. Rise 360 proficiency | **None** | "No, only Storyline" |
| d. Expected monthly salary (AED) | **18000** ⚑ | your figure; confirm after checking sources |
| e. Notice period | **Two months (per current contract)** | her answer |
| Cover letter | below | requirement table only |

> Dear Northwind Learning hiring team,
> I'm applying for the Instructional Designer role. I teach chemistry at Crescent Bay International School in Dubai,
> where I built 42 interactive lab simulations in Articulate Storyline, published them to the school LMS as SCORM
> packages, and saw them adopted by all three Grade 10 chemistry classes.
> I write learning objectives for every unit and compare quiz scores before and after the simulations as an informal
> check on learning. In May 2026 I ran a two-hour Storyline workshop for 12 colleagues. I haven't used Rise 360 yet
> and would be glad to learn it with your team.
> I'd welcome a conversation about turning subject expertise into e-learning for your clients. Layla Haddad

**AI:** Everything is filled. Please check the two ⚑ fields and the letter, then press **Submit** yourself.
**Layla** (later): Applied 2026-10-18.

## 8. Reach out

**AI:** Do you know anyone at Northwind? **Layla:** No one directly; Priya, a former colleague, is a 1st-degree
connection and works there as a learning designer. → A referral beats a cold note. Draft (274/300 chars), **for her to send**:

> Hi Priya, hope you're well! I'm applying for the Instructional Designer role at Northwind. I've built 42 Storyline
> lab simulations, published to our school LMS as SCORM. Would you be open to a quick chat about the team, or to
> referring me if you think I'd fit? Thanks, Layla

## 9. Track

| Date | Company | Role | Posting | Resume sent | Channel | Contact | Status | Next action + date |
|---|---|---|---|---|---|---|---|---|
| 2026-10-18 | Northwind Learning | Instructional Designer | job-posting-northwind.md | …-Northwind-2026-10-18.docx | company site (+ referral ask) | Priya | applied | Follow up if no reply by 2026-10-27 (7 business days) |

## 10. Follow up (2026-10-28, no reply)

**AI:** Anything new since you applied that we could mention? **Layla:** I'm not sure. → The draft keeps a placeholder
rather than invent one. One follow-up to Priya only, then let it rest (213 chars):

> Hi Priya, a quick follow-up on the Instructional Designer role at Northwind: I'm still very keen. [One new detail
> since 18 Oct, if there is one; otherwise leave this line out.] Thanks again for any pointers, Layla

| Date | Company | Status | Next action + date |
|---|---|---|---|
| 2026-10-28 | Northwind Learning | applied, follow-up drafted (Layla sends) | No more nudges; wait |
| 2026-11-03 | Northwind Learning | **interview** (first interview 2026-11-03) | Prep below |

## 11. Interview prep (results only from the ledger)

| # | Posting requirement | Situation → Task → Action → Result |
|---|---|---|
| 1 | Storyline; interactive modules | Students couldn't do some labs safely at home during revision → give them a safe way to practise → built 42 Storyline lab simulations for Grade 10 → adopted by all three Grade 10 chemistry classes |
| 2 | SCORM to an LMS | The simulations had to reach every class → make them available on the school platform → published them as SCORM packages to the school LMS → (no usage figures; say so if asked) |
| 3 | Train-the-trainer; adult learners | Colleagues kept coming to her for "anything Storyline" → help them build their own → ran a two-hour Storyline workshop for 12 colleagues, May 2026 → delivered the CPD session set as a goal in her appraisal |
| 4 | Learning objectives; measuring outcomes | Each unit needs clear aims → write objectives for every unit → compares quiz scores before and after simulations → informal check only, no report (be upfront; offer how she'd formalize it) |
| 5 | Facilitation; change support | School rolled out blended learning (led by the Head of Digital Learning) → support it → trained teachers on the platform → her part only; no numbers |
| 6 | Experience with adult learners (supporting) | Two newly qualified teachers in their induction year → mentor them → regular mentoring → both passed their induction year |

Honest gap answers: Rise 360 ("only Storyline so far; here's how quickly I learned Storyline: certified Mar 2025"),
ADDIE/SAM ("I haven't used the names; my process is objectives → build → check with quizzes"), Camtasia ("not yet").

Questions for her to ask: (1) What does a typical project look like from client brief to launch? (2) Which authoring
tools and LMSs do your clients use most? (3) How do you measure whether a course worked? (4) How would my first
90 days look? (5) How do designers and subject-matter experts split the work?

**AI:** Want a practice round? **Layla:** I'm not sure. → Offered again before 2026-11-03.

## 12. Close (2026-11-20: offer received, accepted, start 2027-01-05)

| Date | Company | Status | Next action + date |
|---|---|---|---|
| 2026-11-20 | Northwind Learning | **offer → accepted** | 2027-01-05: add role on LinkedIn, headline re-check, master update |

```
Section: Open to Work        (remove)
Current:  On · Recruiters only · Instructional Designer, Learning Experience Designer, e-Learning Developer
Proposed: Off
Evidence: offer accepted 2026-11-20 (owner)
Confidentiality: clear
Save this to LinkedIn?
```
**Layla:** Yes. *(Turned off; reloaded: no Open to Work.)*

- **AI:** What's your official title in the offer letter, and your last day at Crescent Bay? **Layla:** I'm not sure.
  → Reminders, not guesses: on 2027-01-05 add the Northwind role with the title from the offer letter, **Notify network
  off**, never click "share your new position"; end-date Crescent Bay on her last day; reload and check the headline
  (adding a position can overwrite it); update the master resume.
- Rejections: none. Proof-of-work for Rise/ADDIE not needed now; noted as an idea.
- `career-notes.md` updated: *What is live*, *Applications*, *Decisions*, reminders, next check-up **2027-02-20**.

**Never pressed Submit and never sent a message:** Layla submitted the application and sends both Priya notes herself.
