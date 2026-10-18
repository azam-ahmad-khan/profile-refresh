# Using profile-refresh with any AI

The skill is plain instructions, so any capable AI can follow it. Pick the row that matches what you have.

| You have | Mode | How to start |
|---|---|---|
| An AI that installs **skills** (Claude app or Claude Code, OpenAI Codex, Gemini CLI, Cursor, GitHub Copilot, …) | Browser mode if it can drive a browser, otherwise copy-paste | Install from the repo (see the main [README](../README.md)) and say "refresh my LinkedIn profile" |
| A **cloud agent with its own browser** (e.g. ChatGPT dots or agent mode, Grok Bot) | Browser mode | Give it this message: *"Read https://github.com/azam-ahmad-khan/profile-refresh/blob/main/skills/profile-refresh/SKILL.md and the files it links, then follow it to refresh my LinkedIn profile. My resume is attached."* |
| A **chat-only AI** (ChatGPT, Gemini, Grok, Claude chat, Copilot chat, …) | Copy-paste mode | Upload [profile-refresh-full.md](profile-refresh-full.md) and your resume, then say: *"Follow the attached profile-refresh instructions in copy-paste mode."* |

**Use it again later:** in ChatGPT make a Custom GPT, in Gemini a Gem, in Claude a Project. Put
`profile-refresh-full.md` in its knowledge/files and use "Follow profile-refresh-full.md" as the instructions.

## Copy-paste mode in one paragraph

The AI interviews you, drafts each change and tells you exactly where to paste it on LinkedIn and which setting to
switch. You do the clicking. After each save, paste back what LinkedIn now shows (or a screenshot) so the AI can check
it. At the end it gives you an updated `career-notes.md`. Save that file and upload it next time, so the check-up
picks up where you left off.

## Safety, whichever AI you use

- Sign in to LinkedIn yourself. Never give an AI your password or verification codes.
- Cloud agents keep a browser on their own computer, so sign out of LinkedIn there when you're done.
- If your AI can see your work email or documents, check your employer's AI policy before using the work-extraction
  prompt.
