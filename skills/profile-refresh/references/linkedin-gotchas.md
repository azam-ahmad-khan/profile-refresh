# LinkedIn gotchas

These were seen while editing real profiles (first written October 2026). LinkedIn changes often. When something here no
longer matches, tell the owner and add a note under *LinkedIn changes seen* in `career-notes.md`.

## Headline and intro

- **Adding a current position can silently overwrite the headline** with "<title> at <company>". Save positions
  before the headline. After saving any position, reload the profile and check the headline. If it changed, put the
  already-approved headline back (no new yes needed) and tell the owner you did.
- The **company/school line under the headline** comes from Edit intro → *Organization* (and *Education*). The
  dropdown lists only positions already on the profile, so add the position first and then pick it there.
- Headline limit: 220 characters. Only the first ~60–70 show in search results and comments, so put the most useful
  words first.

## Companies, positions and dates

- **Several companies share a name.** In the company picker, check the company page (location, follower count, logo,
  website) before you select it. Choosing the plain-text entry without a page leaves a grey placeholder logo.
- After adding a role, LinkedIn shows **"share your new position" / "Notify network"**. Never click it, and keep the
  per-form toggle off.
- Projects (and roles) without an end date show **"– Present"**. Set an end date if the project is finished.
- Position description limit: 2,000 characters. About: 2,600.

## Open to Work

- At most **5 job titles**. LinkedIn maps what you type to its own title list, in every field. Seen examples (from a
  software profile):
  "Backend Engineer" → "Back End Developer", "AI Engineer" → "Artificial Intelligence Engineer",
  "Java Developer" → "Java Software Engineer". Titles that map to the same entry **merge on save**, so you can end
  up with fewer than you picked. Some titles don't exist (e.g. "Forward Deployed Engineer"; "Solutions Engineer" was
  the closest). Type each title, pick from the suggestion list, save, reload, and show the owner the saved list.
- Visibility choice: see [privacy.md](privacy.md) step 4.

## Rich-text boxes (About, descriptions)

- **Type the text with the keyboard tool.** A typed blank line (`\n\n`) becomes a separate paragraph. Setting the
  value with a script collapses everything into one paragraph.
- After saving, reload and check the paragraph breaks. If they collapsed, clear the box and type the text again.
- Bullets: type "• " (or "- ") at the start of the line. LinkedIn has no bullet formatting.

## Featured and media

- **Link previews fail now and then.** Remove the link and add it again, or wait a minute and retry.
- After a site rename (for example a GitHub username change), the preview thumbnail can stay blank. Edit the item's
  title and description by hand and tell the owner the image may stay empty.
- Featured is the visual shop window. Put the strongest proof of work (portfolio project, article, certificate) first.

## Browser automation

- The browser shares the owner's sign-in. If LinkedIn asks for a password, code or CAPTCHA, stop and ask the owner to
  handle it.
- LinkedIn throttles fast automated clicking. Work at human pace, one section at a time, and reload to verify.
- Read the page (text or accessibility tree) to verify. Use screenshots only for layout checks such as photo frames
  and Featured thumbnails.
