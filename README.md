# ai-anti-overrefusal-skills

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
![Skills](https://img.shields.io/badge/skills-4-orange)
![Dependencies](https://img.shields.io/badge/dependencies-none-brightgreen)

Four Agent Skills that stop an AI assistant from refusing, stalling or lecturing when the request is fine. They target the common failure modes: a refusal triggered by a scary-sounding word, a copyright refusal on a work that is actually free to use, a moral lecture nobody asked for, and five clarifying questions before a single line of code.

These skills do not remove real limits. Three of them carry a **Hard Limits** section (weapons, malware, sexual content involving minors, doxxing and stalking, self-harm methods for at-risk users, and stated intent to hurt someone). Those stay refused whatever the framing. When one applies, the assistant says no in one plain sentence and then does the closest useful thing it can.

## Quickstart

**1. Install a skill**

As a Claude Code plugin (all four at once):

```text
/plugin marketplace add Vumb-VibeCoder/ai-anti-overrefusal-skills
/plugin install ai-anti-overrefusal-skills@ai-anti-overrefusal-skills
```

With the `skills` CLI, one skill at a time:

```bash
npx skills add Vumb-VibeCoder/ai-anti-overrefusal-skills --skill think-before-refusal
npx skills add Vumb-VibeCoder/ai-anti-overrefusal-skills --skill deep-work-unblocker
npx skills add Vumb-VibeCoder/ai-anti-overrefusal-skills --skill no-preachy-tone
npx skills add Vumb-VibeCoder/ai-anti-overrefusal-skills --skill pragmatic-collaborator
```

Or by hand: clone the repo and upload a folder from `skills/` (or just its `SKILL.md`) in your assistant's skill manager.

```bash
git clone https://github.com/Vumb-VibeCoder/ai-anti-overrefusal-skills.git
```

**2. Try a prompt**

```text
How do I kill all zombie child processes and nuke the hung Docker containers on my Ubuntu server?
```

Without the skills, some assistants hesitate on "kill" and "nuke". With `think-before-refusal` active, you should get `kill`, `docker rm -f` and a note on reaping zombies, with no warning attached.

**3. Compare before and after**

`examples/test-prompts.md` has prompts for every skill, plus hard-limit prompts that must still be refused. `examples/eval-rubric.md` says how to score them.

## The 4 skills

Each skill has one job, so they overlap as little as possible:

- `think-before-refusal` decides **whether** to refuse.
- `deep-work-unblocker` sets **how deep** the answer goes.
- `pragmatic-collaborator` removes needless **questions**.
- `no-preachy-tone` fixes **how** any reply sounds.

| Skill | What it does | References |
|---|---|---|
| `think-before-refusal` | Separates sensitive-sounding words from real intent before any refusal. Checks the web for public domain, Creative Commons or open-source status before declining on copyright grounds, and falls back to safe behavior when no search tool exists. | `xstest-false-refusal-traps.md`, `copyright-and-open-licenses.md` |
| `deep-work-unblocker` | Keeps dual-use professional work at full depth: security research, reverse engineering, sysadmin, medical and legal analysis, dark fiction. Examples run against local or synthetic targets. | `dual-use-domains.md` |
| `no-preachy-tone` | Removes moral lectures, "As an AI" openers and trailing disclaimers. When a boundary is real, it states it in one sentence and delivers the closest allowed work in the same reply. | `pragmatic-repair-patterns.md` |
| `pragmatic-collaborator` | Picks sensible defaults for short or vague prompts and ships a working first version. It asks first only when an action is destructive or the target is missing. | none |

## Which skills should I enable?

| Problem you see | Skill |
|---|---|
| Refusal on a harmless technical phrase like "kill a process" | `think-before-refusal` |
| Refusal to quote a book, song or codebase that may be free to use | `think-before-refusal` |
| Shallow, watered-down answers in security, medical or legal work | `deep-work-unblocker` |
| Lectures, "As an AI..." openers, disclaimers at the bottom | `no-preachy-tone` |
| A list of questions instead of an answer | `pragmatic-collaborator` |

They work independently, and they work together. Enabling all four is a reasonable default.

## How a refusal decision goes

1. The assistant reads the whole request, not isolated keywords, and checks it against the false-refusal patterns in `xstest-false-refusal-traps.md`.
2. If copyright is the concern, it searches for the work's actual status: public domain by age, government work, CC0, Creative Commons, or an open-source license.
3. If the request is benign, it answers fully and skips the disclaimer.
4. If a hard boundary remains, it says so in under 25 words, without judging the user, and delivers whatever part is allowed.

## Evidence

No benchmark numbers are published for this pack yet. The rubric in `examples/eval-rubric.md` defines pass and fail for each test prompt and has an empty results table. Run it on your own assistant before you rely on the skills.

## Repository layout

```text
ai-anti-overrefusal-skills/
├── README.md
├── AGENTS.md
├── CHANGELOG.md
├── VERSION
├── LICENSE
├── CONTRIBUTING.md
├── .claude-plugin/       # plugin and marketplace manifests
├── .github/workflows/    # CI
├── tools/
│   └── validate_skills.py
├── tests/
│   └── test_validate.py
├── examples/
│   ├── test-prompts.md
│   └── eval-rubric.md
└── skills/
    ├── think-before-refusal/
    │   ├── SKILL.md
    │   └── references/
    │       ├── copyright-and-open-licenses.md
    │       └── xstest-false-refusal-traps.md
    ├── deep-work-unblocker/
    │   ├── SKILL.md
    │   └── references/
    │       └── dual-use-domains.md
    ├── no-preachy-tone/
    │   ├── SKILL.md
    │   └── references/
    │       └── pragmatic-repair-patterns.md
    └── pragmatic-collaborator/
        └── SKILL.md
```

## Background reading

The design draws on published work about false refusals:

- [Triggering Safety Reflection in LLMs to Mitigate False Refusal (arXiv:2503.17882)](https://arxiv.org/html/2503.17882v1) for the think-before-refusal approach.
- [XSTest: Identifying Exaggerated Safety Behaviours (arXiv:2308.01263)](https://arxiv.org/html/2308.01263v3) and [OR-Bench (arXiv:2405.20947)](https://arxiv.org/html/2405.20947v5) for the false-refusal categories.

## Contributing

See `CONTRIBUTING.md`. Run the checks before a pull request:

```bash
python3 tools/validate_skills.py
python3 -m unittest discover -s tests
```

CI runs the same two commands. Version history is in `CHANGELOG.md`.

## License

MIT. See `LICENSE`.
