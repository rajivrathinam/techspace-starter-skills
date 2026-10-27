# EP2 · Claude Skills vs MCP vs Projects

**The 10-second rule:** *what* goes in a Project, *how* goes in a Skill, *where* goes in a Connector (MCP).

## Project instructions (keep them short)
```text
Client: <Acme Bakery, 3 shops>
Goal: <launch the winter menu by 1 Dec>
Tone: <warm, short, no jargon>
Details live in the uploaded files.
```

## Ask inside the project
```text
What should we cut from the plan?
```

## A skill for know-how
See [`skills/brand-voice`](../skills/brand-voice/SKILL.md). The version from the video:
```markdown
---
name: brand-voice
description: Use when writing anything public.
---

Short sentences. No jargon.
Always end with one clear next step.
```

## Connectors in action (with the matching connector switched on)
```text
Find last week's sales email and pull the numbers into a summary.
```
```text
What's on my Thursday?
```
```text
Find the latest version of the contract.
```
```text
Summarise what I missed in the launch channel.
```

## One job, all three together
Inside the client's project, with the [`client-update`](../skills/client-update/SKILL.md) skill and an email connector on:
```text
Write this week's update for <Acme>.
```

## Quick test answers
| Need | Use |
|---|---|
| Your company's email style | Skill |
| A big client with lots of files | Project |
| Checking your calendar | Connector |
