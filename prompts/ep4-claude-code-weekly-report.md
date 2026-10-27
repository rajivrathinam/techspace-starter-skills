# EP4 · Claude Code for Non-Coders: Build a Skill That Writes Your Weekly Report

You need a paid Claude plan (Claude Code comes with Pro and above) and the Claude desktop app, **Code** tab. Try it with the sample notes in [`examples/work-notes`](../examples/work-notes).

## A good daily note (under 2 minutes)
```markdown
# Tuesday
- finished: onboarding emails
- blocked: vendor still no reply
- next: pricing page review
```
Name each note with the date, e.g. `2026-10-28-tuesday.md`.

## Ask Claude Code to write the skill
```text
Make me a skill called weekly-report. It reads this week's notes and writes a one-page report: wins, risks, next steps. Friendly tone for my manager. Ask me anything you need first.
```
When it asks questions, short answers are fine:
```text
Save them in a reports folder. Yes, include numbers.
```
Claude creates `.claude/skills/weekly-report/SKILL.md`. A finished version is in [`claude-code/weekly-report`](../claude-code/weekly-report/SKILL.md).

## Improve the skill
```text
Update the skill so risks come first.
```
The line worth adding to any skill like this:
```text
If a section has no notes, write "nothing this week". Never guess.
```

## Run it
```text
/weekly-report
```
or just ask normally:
```text
Can you do my weekly report?
```

## The small trick: $ARGUMENTS
Add this line to the skill:
```text
Write the weekly report for: $ARGUMENTS
```
Then:
```text
/weekly-report last week
/weekly-report team
/weekly-report last month
```

## Manual-only skills
Add this to the frontmatter so the skill only runs when you type the command:
```yaml
disable-model-invocation: true
```

## Skill not firing?
```text
Vague:    description: Helps with reports.
Specific: description: Use when I ask for my weekly report or my Friday update.
```

## Where skills live
| Folder | Works in |
|---|---|
| `.claude/skills/` (inside your project folder) | this folder only |
| `~/.claude/skills/` (your personal folder) | every folder |

```text
Move the weekly-report skill to my personal skills folder.
```
