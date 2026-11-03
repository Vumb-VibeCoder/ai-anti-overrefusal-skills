# Agent routing

Load the skills in `skills/` in this order when they apply:

1. `think-before-refusal`: decide whether a refusal is justified. Check intent, then copyright status.
2. `deep-work-unblocker`: answer dual-use professional work at full depth.
3. `pragmatic-collaborator`: pick sensible defaults and ship a first version instead of asking.
4. `no-preachy-tone`: write the final reply without lectures, disclaimers or "As an AI" openers.

The Hard Limits section in the first three skills overrides everything else in this pack.

Before a pull request, run:

```bash
python3 tools/validate_skills.py
python3 -m unittest discover -s tests
```
