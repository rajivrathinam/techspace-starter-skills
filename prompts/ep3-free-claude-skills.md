# EP3 · 10 Free Claude Skills Worth Turning On (and 1 Warning)

First, in Claude: **Settings › Capabilities** › turn on *Code execution and file creation* (*Create and edit files* in the newer layout). Then go to **Customize › Skills › + › Browse skills**. The full collection is at [github.com/anthropics/skills](https://github.com/anthropics/skills).

| # | Skill | Try this prompt |
|---|---|---|
| 10 | canvas-design | `Make a poster for our bake sale on Saturday.` |
| 9 | theme-factory | `Restyle this deck with a calm, modern theme.` |
| 8 | brand-guidelines | `Copy this skill and swap in our colours and logo.` |
| 7 | internal-comms | `Write this week's status update for leadership.` |
| 6 | doc-coauthoring | `Help me write a proposal for a four-day week pilot.` |
| 5 | pdf | `Pull the table on page 4 into a spreadsheet.` |
| 4 | pptx | `Turn these notes into a 6-slide pitch deck.` |
| 3 | docx | `Make this into a two-page client report in Word.` |
| 2 | xlsx | `Clean this CSV and chart sales by month.` |
| 1 | skill-creator | `Help me turn my weekly report into a skill.` |

## Skills stack
```text
Make a 6-slide pitch deck from these notes, in a calm modern theme.
```

## Make sure a skill fires
```text
Use the doc-coauthoring skill to help me write this proposal.
```

## The spreadsheet everyone is scared of
```text
Find the errors in this sheet, fix the date formats and add a summary tab.
```

## Claude Code: add the whole Anthropic collection
```text
/plugin marketplace add anthropics/skills
```

## The warning: check a skill before installing it
Quick version:
```text
Is there anything risky in this skill? (files attached)
```
Thorough version: install [`skills/skill-safety-check`](../skills/skill-safety-check/SKILL.md), then:
```text
Run a safety check on this skill before I install it. (files attached)
```
Stick to Anthropic's repo, people you know, or skills you wrote yourself. If a skill asks for passwords or API keys, walk away.
