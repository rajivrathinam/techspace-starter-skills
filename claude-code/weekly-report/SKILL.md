---
name: weekly-report
description: Use when I ask for my weekly report or my Friday update. Reads this week's notes in work-notes/ and saves a one-page report in reports/.
argument-hint: "[who or what period, e.g. team, last week, last month]"
---

# Weekly report (Claude Code)

Write the weekly report for: $ARGUMENTS
(If nothing is given, write my own report for this week.)

## Steps
1. Read the notes in `work-notes/` for the period asked for (default: this week). Note files are named by date, e.g. `2026-10-27-monday.md`.
2. Write a one-page report with these sections, **risks first**:
   - Risks (bullets)
   - Wins
   - Next steps
3. End with 3 bullets for my manager.
4. Save it as `reports/week-of-<YYYY-MM-DD>.md` (create `reports/` if needed). Never overwrite an existing report. Add `-v2` instead.
5. Tell me the file name and show a short preview.

## Rules
- If a section has no notes, write "Nothing this week". Never guess.
- Keep numbers exactly as written in the notes.
- Friendly tone for my manager. Short sentences.

<!--
Want this skill to run ONLY when you type /weekly-report (never automatically)?
Add this line to the frontmatter above:
disable-model-invocation: true
-->
