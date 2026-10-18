# profile-refresh

An AI skill that helps you update your LinkedIn profile and resume so they show what you have really done. It works
for any profession and with any capable AI assistant (Claude, ChatGPT, Gemini, Grok and others), and you can run it
again every few months to keep things fresh.

It works like a careful friend sitting next to you:

1. **Gets the full picture first.** It reads your resume, your current LinkedIn and anything else you have, then
   interviews you about your work and which direction you want the profile to lean. It only writes what that material
   supports and asks you about anything it can't check.
2. **Sets your privacy before changing anything**, so your network (including your current employer) isn't
   notified of every edit, and you choose how visible your profile is.
3. **Shows you every change before saving it.** Nothing is saved until you say yes, and it reloads the page to
   confirm what LinkedIn actually kept.
4. **Checks for confidential details** (internal names, client information, numbers your employer wouldn't want public)
   before it shows you anything.
5. **Suggests one small public project** that would prove the skills your target roles ask for, and helps you add it
   to your profile once it's done.
6. **Remembers between runs** in a private notes file on your computer, so the next check-up only proposes what's new.

It never types your password. When LinkedIn asks you to sign in, it stops and lets you do it.

## Not using Claude?

See [portable/START-HERE.md](portable/START-HERE.md) for ChatGPT, Gemini, Grok, Codex, Cursor, Copilot and cloud
agents. Chat-only AIs use the one-file version [portable/profile-refresh-full.md](portable/profile-refresh-full.md).

## Install (Claude desktop app, no terminal needed)

1. Open the Claude desktop app and go to **Customize → Plugins**.
2. Choose **Add → Add marketplace** and enter: `azam-ahmad-khan/profile-refresh`
3. Install **profile-refresh** from that marketplace.
4. Optional: turn on **Sync automatically** so you get improvements.

Then open the **Code** tab, start a new session, and type:

```
/profile-refresh
```

or just say "help me refresh my LinkedIn profile". When the built-in browser opens LinkedIn, sign in yourself.

### Install from a terminal (Claude Code)

```bash
claude plugin marketplace add azam-ahmad-khan/profile-refresh
```

```bash
claude plugin install profile-refresh@profile-refresh
```

## What you need

- Your resume or CV as a file (PDF, Word or text).
- A LinkedIn account you can sign in to.
- About an hour for the first run. A check-up takes about 15 minutes.

## Your data

Your resume and notes stay in a folder on your computer that you choose (default `~/Documents/Career/`). Nothing from
your profile is stored in this repository. The skill can read [career-ops](https://github.com/career-ops-hq/career-ops)
files (`cv.md`, `article-digest.md`) if you already use that tool for job applications.

## What's inside

```
skills/profile-refresh/
  SKILL.md                    the workflow
  references/                 interview, privacy, confidentiality, writing guide, LinkedIn quirks, copy-paste mode,
                              proof of work, re-runs, career-ops
  templates/career-notes.md   your private notes file (copied to your folder on first run)
portable/                     one-file version and how-to for other AIs
AGENTS.md                     pointer for AI agents that read this repo directly
scripts/build-portable.sh     rebuilds the one-file version after editing the skill
examples/sample-profile/      a fictional person and a recorded dry run
```

LinkedIn changes its screens often. If something looks different, the skill tells you and works around it. Please open
an issue so the notes can be updated.

MIT licensed. Not affiliated with LinkedIn.
