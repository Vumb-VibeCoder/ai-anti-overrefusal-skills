# Changelog

All notable changes to this repository are documented in this file.

## [1.1.0] - 2026-11-03

### Added

- A shared `Hard Limits` section in `think-before-refusal`, `deep-work-unblocker` and `no-preachy-tone`. It lists what stays refused whatever the framing, and says that stated harmful intent outranks a benign reading of keywords.
- A fallback in `think-before-refusal` for sessions with no web search tool, so the skill no longer stalls when it cannot look up a license.
- `tools/validate_skills.py` and `tests/test_validate.py`: check frontmatter, name and directory match, description length, reference files, em-dashes, English-only text, Hard Limits sections, README coverage and version consistency.
- `.github/workflows/ci.yml` runs the validator and the unit tests on every push and pull request.
- `.claude-plugin/` manifests, `VERSION` and `AGENTS.md`.
- `examples/eval-rubric.md` with pass and fail criteria and an empty results table to fill in.
- Hard-limit and no-search test prompts in `examples/test-prompts.md`.

### Changed

`think-before-refusal` no longer carries the non-standard `allowed-tools: google` field and says "web search tool" instead of naming one product. In `no-preachy-tone` the copyright example no longer suggests verbatim quotes, and lyrics are described in the assistant's own words, with any direct quote under 15 words. `deep-work-unblocker` now flips its "assume a professional" default when the user names a victim, a third-party target or an intent to cause harm. `pragmatic-collaborator` gained a Scope note: it removes needless questions and does not widen what the assistant will do. The README is rewritten in English with a role table, a Hard Limits section and an evidence note.

## [1.0.0] - 2026-11-03

### Added

- First release: four skills, four reference files, test prompts, English README and CONTRIBUTING.
