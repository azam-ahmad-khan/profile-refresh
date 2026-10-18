# Working alongside career-ops

[career-ops](https://github.com/career-ops-hq/career-ops) (MIT) is an open-source job-search agent. It scores job
postings against a CV, drafts tailored CVs and cover letters, scans job boards, tracks applications, and helps with
interview prep. It does **not** edit LinkedIn profiles, manage privacy settings or suggest proof-of-work projects.
Those gaps are what this skill fills. The two fit together: this skill gets the profile and base resume right, then
career-ops applies them to specific jobs.

## If the owner's folder has career-ops files

| career-ops file | How to use it here |
|---|---|
| `cv.md` | Read it as the resume. It is **owner-owned**: change it only with the owner's explicit OK, show the diff, and keep a dated backup copy |
| `article-digest.md` | Read it as evidence (proof points). Offer to append a finished proof-of-work project, with the OK |
| `config/profile.yml` | Read it for target roles, location and preferences. Don't write to it |
| `modes/_profile.md` | Read it for the owner's narrative and archetypes, to keep the LinkedIn wording consistent |
| `data/applications.md` | Read only, to tell whether they're actively applying (it affects the visibility reminders) |

## Handing the profile to career-ops

If the owner uses career-ops, offer once (on OK, showing the diff) to fill these fields in `config/profile.yml` from
`career-notes.md`, so both tools tell the same story. Leave every other key alone.

| career-notes.md | `config/profile.yml` |
|---|---|
| Target roles | `target_roles.primary` |
| Approved headline | `narrative.headline` |
| Pivot lean and bridges ([context-interview.md](context-interview.md) §2) | `narrative.exit_story` |
| Proof-of-work project (name, public link, verified outcome) | `narrative.proof_points[]` (`name`, `url`, `hero_metric`) |
| Location to show | `location.city`, `location.country` |
| LinkedIn URL, portfolio link | `candidate.linkedin`, `candidate.portfolio_url` |

career-ops also has `project` (scores a portfolio idea), `upskill` and `expand` (find missing skills) modes. If the
owner has it installed, suggest running its `project` mode on the proof-of-work idea for a second opinion.

Never write to career-ops system files (`modes/*.md` other than `_profile.md`, scripts, templates).

## If they don't use it

Mention career-ops once, in the wrap-up, as an option for the application stage. Don't install or set it up unless
they ask.
