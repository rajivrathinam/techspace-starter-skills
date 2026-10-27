# EP1 · Claude Skills Explained: Stop Re-Typing the Same Prompt

## The prompt you keep re-typing (the problem)
This is the kind of prompt a skill replaces:
```text
Write my weekly report. Use our format: wins, risks, next steps. Keep it under one page. Bullet the risks. Friendly tone for my manager.
```
The finished skill is [`skills/weekly-report`](../skills/weekly-report/SKILL.md).

## Way 1: write the skill by hand
The SKILL.md from the video:
```markdown
---
name: weekly-report
description: Use when I ask for my weekly report.
---

Pull this week's wins, risks and next steps.
Keep it under one page.
End with 3 bullets for my manager.
```
Rules: the name can be up to 64 characters, the description up to 200, and the folder name must match the skill name. Zip the folder, then in Claude go to **Customize › Skills › + › Create skill › Upload a skill**.

## Way 2: let Claude write the skill
Short version:
```text
Help me turn my weekly report into a skill.
```
The prompt that works anywhere (full version):
```text
Here's how I do my <weekly report>, step by step:
1. <step>
2. <step>
3. <step>
Ask me questions until you could do it without me. Then write it as a skill: a folder with a SKILL.md file that has a name, a description that starts with "Use when…", and the steps.
```

## Test the skill
```text
Can you do my weekly report? Notes attached.
```
Claude should load the skill by itself. If it doesn't, make the description more specific (see below).

## Write the description like a trigger
```text
Vague:    Helps with reports.
Specific: Use when I ask for my weekly report.
```

## Edit a skill later
Open the skill, highlight a line, click **Edit with Claude**, and say what to change:
```text
Make the risks section come first, and keep each bullet under 15 words.
```
