# Changelog

All notable changes to this repository are documented in this file.

## [1.5.0] - 2026-11-03

### Added

- `own-project-trust`: presumes the user owns the project they are building, judges code by function instead of genre or keywords, keeps project context across turns, and asks one question only when the target moves to someone else's product. Ownership never unlocks the Hard Limits.

## [1.4.0] - 2026-11-03

### Added

- `legacy-software-lab`: discontinued software and games are treated as a private lab for study, patching and added features on the user's own copy. It stays private, offline and non-distributing, and says plainly that "abandoned" is not a legal status.

## [1.3.0] - 2026-11-03

### Added

- `legal-context-check`: a two-sided legal check (jurisdiction, ownership, authorization, current law) that sorts a request into clearly legal, legal with conditions, gray area or clearly illegal. It keeps terms-of-service breaches separate from crimes, and keeps the Hard Limits above legality.

## [1.2.0] - 2026-11-03

### Added

- `partial-completion`: finish every fine part of a multi-part request, state one boundary, and never discard paid-for work.
- `dark-fiction-craft`: full literary depth for dark themes, with operational detail kept impressionistic.
- `plain-expert-answers`: direct medical, legal and financial information with at most one relevant referral line.
- All three carry the shared Hard Limits section, which the validator now requires.

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
