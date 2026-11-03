# Contributing

Thanks for helping improve this skills pack.

## Rules for writing or editing a `SKILL.md`

1. **Valid frontmatter**
   - `name`: lowercase letters, digits and hyphens only. Up to 64 characters.
   - `description`: what the skill does and when it should trigger. Under 1024 characters.
2. **Formatting**
   - Use plain hyphens (`-`). No em-dashes or en-dashes in `SKILL.md`.
   - Put a blank line before every list.
   - Keep `SKILL.md` under 500 lines. Move long tables and catalogs into `references/`.
3. **Language**
   - Write everything in English: skill text, references, examples and comments.
4. **Tests**
   - When you add a rule, add a matching prompt to `examples/test-prompts.md` with the behavior you expect.
   - Run `python3 tools/validate_skills.py` and `python3 -m unittest discover -s tests`. Both must pass.
5. **Hard Limits**
   - Never weaken the `Hard Limits` section in a skill. Changes to it need a stated reason in the pull request.
6. **Versioning**
   - Update `VERSION`, `.claude-plugin/plugin.json`, `.claude-plugin/marketplace.json` and `CHANGELOG.md` together.

## Pull requests

- Keep one change per pull request.
- Say which skill you touched and which failure it fixes.
