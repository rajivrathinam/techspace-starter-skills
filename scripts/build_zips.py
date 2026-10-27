"""Check every skill and build upload-ready ZIPs into dist/ (the skill folder is the ZIP root).

    python scripts/build_zips.py
"""
import re
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DIST = ROOT / "dist"
SOURCES = [("skills", ""), ("claude-code", "claude-code-"), ("template", "template-")]

def check(skill: Path) -> list[str]:
    text = (skill / "SKILL.md").read_text(encoding="utf-8")
    fm = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not fm:
        return ["SKILL.md must start with --- frontmatter ---"]
    fields = dict(re.findall(r"^([\w-]+):\s*(.+)$", fm.group(1), re.M))
    name, desc = fields.get("name", ""), fields.get("description", "").strip('"')
    errors = []
    if name != skill.name:
        errors.append(f"name '{name}' must match folder '{skill.name}'")
    if not re.fullmatch(r"[a-z0-9-]{1,64}", name):
        errors.append("name: lowercase letters, numbers and hyphens, max 64 chars")
    if not 0 < len(desc) <= 200:
        errors.append(f"description must be 1-200 chars (is {len(desc)})")
    return errors

DIST.mkdir(exist_ok=True)
failed = False
for folder, prefix in SOURCES:
    for skill in sorted(p for p in (ROOT / folder).iterdir() if (p / "SKILL.md").exists()):
        errors = check(skill)
        if errors:
            failed = True
            print(f"FAIL {folder}/{skill.name}: " + "; ".join(errors))
            continue
        out = DIST / f"{prefix}{skill.name}.zip"
        with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
            for f in sorted(skill.rglob("*")):
                if f.is_file():
                    z.write(f, f.relative_to(skill.parent).as_posix())
        print(f"ok   {folder}/{skill.name} -> dist/{out.name}")
sys.exit(1 if failed else 0)
