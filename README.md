# The Tech Space · Free Claude Starter Skills

Free starter skills and **every prompt** from The Tech Space's *Claude Skills* video series. Copy them, make them yours, and stop re-typing the same prompt.

> A skill is just a folder with one `SKILL.md` file: a **name**, a **description** that tells Claude *when* to use it, and the **steps** in plain English.

## What's inside

| Skill | What it does | From |
|---|---|---|
| [`weekly-report`](skills/weekly-report/SKILL.md) | Turns your notes into a one-page report: wins, risks, next steps | EP1 |
| [`brand-voice`](skills/brand-voice/SKILL.md) | Writes public text in your voice, with a checklist | EP2 |
| [`meeting-notes`](skills/meeting-notes/SKILL.md) | Transcript → summary, decisions, action items | EP1 |
| [`client-update`](skills/client-update/SKILL.md) | A short weekly client email from your project + connectors | EP2 |
| [`skill-safety-check`](skills/skill-safety-check/SKILL.md) | Reviews someone else's skill before you install it | EP3 |
| [`claude-code/weekly-report`](claude-code/weekly-report/SKILL.md) | Claude Code version: reads `work-notes/`, saves `reports/`, takes `$ARGUMENTS` | EP4 |
| [`template/my-skill`](template/my-skill/SKILL.md) | A blank template to write your own | EP1 |

- **[prompts/](prompts/README.md):** every prompt shown in the videos, by episode.
- **[examples/work-notes/](examples/work-notes):** a week of sample notes for trying the weekly-report skill.
- **[dist/](dist):** ready-to-upload ZIPs.

## Install in Claude (claude.ai / desktop)
1. **Settings › Capabilities** › turn on **Code execution and file creation** (called *Create and edit files* in the newer layout).
2. Download a ZIP from [`dist/`](dist) (for example `weekly-report.zip`).
3. Open **Customize › Skills › + › Create skill › Upload a skill** and choose the ZIP.
4. Make sure the skill is switched on, then just ask: *"Can you do my weekly report?"*

Edit before or after uploading. The steps are plain English. In Claude you can highlight a line and use **Edit with Claude**.

## Install in Claude Code
Copy a skill folder into your project's `.claude/skills/` (this folder only) or into `~/.claude/skills/` (every folder):
```text
your-project/
└── .claude/skills/weekly-report/SKILL.md
```
Run it with `/weekly-report`, or just ask for your weekly report.

## Write your own
Copy [`template/my-skill`](template/my-skill/SKILL.md), rename the folder and the `name` to match, and write the description like a trigger:
```text
Vague:    Helps with reports.
Specific: Use when I ask for my weekly report or my Friday update.
```
The name can be up to 64 characters and the description up to 200. Run `python scripts/build_zips.py` to check your skills and rebuild the ZIPs.

## Safety
Skills can include scripts that run code. Only install skills from sources you trust, and read every file first. Or run [`skill-safety-check`](skills/skill-safety-check/SKILL.md) on it.

## Watch the series
*Claude in 7 Minutes* on YouTube: [@TechSpaceInfo](https://www.youtube.com/@TechSpaceInfo)
1. Claude Skills Explained: Stop Re-Typing the Same Prompt
2. Claude Skills vs MCP vs Projects: Which One Do You Actually Need?
3. 10 Free Claude Skills Worth Turning On (and 1 Warning)
4. Claude Code for Non-Coders: Build a Skill That Writes Your Weekly Report
5. Claude Free vs Pro vs Max: What Do You Actually Get?

Claude features change often. Plan availability and menu names were checked against the Claude Help Center in October 2026.

---
MIT licensed. Claude is made by Anthropic. This project is independent and not affiliated with Anthropic.
