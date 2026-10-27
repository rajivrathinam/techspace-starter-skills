---
name: skill-safety-check
description: Use when I share a third-party Claude skill (files or a ZIP) and ask whether it is safe to install. Reviews every file and flags risky behaviour.
---

# Skill safety check

Review a skill I did not write before I install it.

## Steps
1. List every file in the skill.
2. Read each file completely, including scripts in any language.
3. Flag anything that:
   - sends data to an external server, URL or API;
   - asks for passwords, API keys, tokens or personal details;
   - deletes, moves or overwrites files outside its own folder;
   - downloads and runs other code;
   - is obfuscated, encoded or hard to read;
   - does something the description does not mention.
4. Give a verdict: **Looks OK**, **Check with the author**, or **Don't install**.

## Output
```
Verdict: …
Files reviewed: …
Findings:
- <file>: <what it does> (<why it matters>)
What I'd change before installing: …
```

## Rules
- Do not run any of the skill's scripts. Only read them.
- If a file can't be read, say so, and treat the skill as "Check with the author".
- This check helps, but it does not replace your own judgement. Only install skills from sources you trust.
