#!/usr/bin/env python3
"""Validate the skills pack. Standard library only.

Usage:
    python3 tools/validate_skills.py            # validate the repo root
    python3 tools/validate_skills.py PATH       # validate another checkout
Exit code is 1 when any error is found.
"""
import json
import re
import sys
from pathlib import Path

NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
ALLOWED_KEYS = {"name", "description", "license", "compatibility", "metadata", "allowed-tools"}
MAX_LINES = 500
MAX_DESC = 1024
# Skills that must carry the shared Hard Limits section.
NEEDS_HARD_LIMITS = {
    "think-before-refusal",
    "deep-work-unblocker",
    "no-preachy-tone",
    "partial-completion",
    "dark-fiction-craft",
    "plain-expert-answers",
    "legal-context-check",
    "legacy-software-lab",
    "own-project-trust",
}
# Latin letters with diacritics beyond Latin-1, used by Vietnamese and similar scripts.
NON_ENGLISH_RE = re.compile(r"[\u00c0-\u024f\u1e00-\u1eff]")
DASH_RE = re.compile(r"[\u2013\u2014]")


def parse_frontmatter(text):
    if not text.startswith("---\n"):
        return None, text
    end = text.find("\n---\n", 4)
    if end == -1:
        return None, text
    block = text[4:end]
    body = text[end + 5:]
    data = {}
    for line in block.splitlines():
        if not line.strip() or line.startswith(" "):
            continue
        if ":" not in line:
            return None, text
        key, _, value = line.partition(":")
        data[key.strip()] = value.strip()
    return data, body


def validate(root):
    root = Path(root)
    errors = []
    skills_dir = root / "skills"
    skill_dirs = sorted(p for p in skills_dir.iterdir() if p.is_dir()) if skills_dir.is_dir() else []
    if not skill_dirs:
        errors.append("no skills found under skills/")

    for sd in skill_dirs:
        name = sd.name
        md = sd / "SKILL.md"
        if not md.is_file():
            errors.append(f"{name}: missing SKILL.md")
            continue
        text = md.read_text(encoding="utf-8")
        fm, _ = parse_frontmatter(text)
        if fm is None:
            errors.append(f"{name}: missing or malformed frontmatter")
            continue
        if fm.get("name") != name:
            errors.append(f"{name}: frontmatter name {fm.get('name')!r} does not match directory")
        if not NAME_RE.match(fm.get("name", "")) or len(fm.get("name", "")) > 64:
            errors.append(f"{name}: invalid name format")
        desc = fm.get("description", "")
        if not desc:
            errors.append(f"{name}: empty description")
        elif len(desc) > MAX_DESC:
            errors.append(f"{name}: description is {len(desc)} characters (max {MAX_DESC})")
        extra = set(fm) - ALLOWED_KEYS
        if extra:
            errors.append(f"{name}: unknown frontmatter keys {sorted(extra)}")
        if len(text.splitlines()) > MAX_LINES:
            errors.append(f"{name}: SKILL.md is longer than {MAX_LINES} lines")
        if DASH_RE.search(text):
            errors.append(f"{name}: em-dash or en-dash found in SKILL.md")
        if name in NEEDS_HARD_LIMITS and "## Hard Limits" not in text:
            errors.append(f"{name}: missing '## Hard Limits' section")

        refs_dir = sd / "references"
        on_disk = {p.name for p in refs_dir.glob("*.md")} if refs_dir.is_dir() else set()
        mentioned = set(re.findall(r"references/([A-Za-z0-9_.-]+\.md)", text))
        for ref in sorted(mentioned - on_disk):
            errors.append(f"{name}: references/{ref} is mentioned but does not exist")
        for ref in sorted(on_disk - mentioned):
            errors.append(f"{name}: references/{ref} exists but SKILL.md never mentions it")

    # English only, across every markdown file outside .git.
    for md in root.rglob("*.md"):
        if ".git" in md.parts:
            continue
        for i, line in enumerate(md.read_text(encoding="utf-8").splitlines(), 1):
            if NON_ENGLISH_RE.search(line):
                errors.append(f"{md.relative_to(root)}:{i}: non-English text")

    # Every skill appears in the README.
    readme = root / "README.md"
    if readme.is_file():
        rtext = readme.read_text(encoding="utf-8")
        for sd in skill_dirs:
            if f"`{sd.name}`" not in rtext:
                errors.append(f"README.md does not mention skill `{sd.name}`")
    else:
        errors.append("README.md is missing")

    # Version consistency.
    version_file = root / "VERSION"
    plugin = root / ".claude-plugin" / "plugin.json"
    if version_file.is_file() and plugin.is_file():
        v = version_file.read_text(encoding="utf-8").strip()
        pv = json.loads(plugin.read_text(encoding="utf-8")).get("version")
        if v != pv:
            errors.append(f"VERSION ({v}) does not match plugin.json ({pv})")
        changelog = root / "CHANGELOG.md"
        if changelog.is_file() and f"[{v}]" not in changelog.read_text(encoding="utf-8"):
            errors.append(f"CHANGELOG.md has no entry for {v}")
    return errors


def main(argv):
    root = Path(argv[1]) if len(argv) > 1 else Path(__file__).resolve().parent.parent
    errors = validate(root)
    for e in errors:
        print(f"ERROR: {e}")
    if errors:
        print(f"{len(errors)} problem(s) found.")
        return 1
    print("OK: all checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
