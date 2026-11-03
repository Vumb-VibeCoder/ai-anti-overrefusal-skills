import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
import validate_skills as v  # noqa: E402

GOOD = "---\nname: demo-skill\ndescription: Does a demo thing. Use when testing.\n---\n# Demo\n\nBody.\n"


def make_repo(tmp, skill_md=GOOD, skill_dir="demo-skill", readme="`demo-skill`\n"):
    root = Path(tmp)
    (root / "skills" / skill_dir).mkdir(parents=True)
    (root / "skills" / skill_dir / "SKILL.md").write_text(skill_md, encoding="utf-8")
    (root / "README.md").write_text(readme, encoding="utf-8")
    return root


class RepoTests(unittest.TestCase):
    def test_real_repo_is_clean(self):
        self.assertEqual(v.validate(ROOT), [])

    def test_every_real_skill_has_description_under_limit(self):
        for md in (ROOT / "skills").glob("*/SKILL.md"):
            fm, _ = v.parse_frontmatter(md.read_text(encoding="utf-8"))
            self.assertLessEqual(len(fm["description"]), v.MAX_DESC, md)


class ValidatorTests(unittest.TestCase):
    def test_good_skill_passes(self):
        with tempfile.TemporaryDirectory() as t:
            self.assertEqual(v.validate(make_repo(t)), [])

    def test_name_must_match_directory(self):
        with tempfile.TemporaryDirectory() as t:
            root = make_repo(t, skill_dir="other-name", readme="`other-name`\n")
            self.assertTrue(any("does not match directory" in e for e in v.validate(root)))

    def test_missing_frontmatter(self):
        with tempfile.TemporaryDirectory() as t:
            root = make_repo(t, skill_md="# no frontmatter\n")
            self.assertTrue(any("frontmatter" in e for e in v.validate(root)))

    def test_long_description_rejected(self):
        long_md = "---\nname: demo-skill\ndescription: " + "x" * 1100 + "\n---\nbody\n"
        with tempfile.TemporaryDirectory() as t:
            root = make_repo(t, skill_md=long_md)
            self.assertTrue(any("max 1024" in e for e in v.validate(root)))

    def test_em_dash_rejected(self):
        with tempfile.TemporaryDirectory() as t:
            root = make_repo(t, skill_md=GOOD + "A \u2014 B\n")
            self.assertTrue(any("em-dash" in e for e in v.validate(root)))

    def test_vietnamese_text_rejected(self):
        with tempfile.TemporaryDirectory() as t:
            root = make_repo(t, skill_md=GOOD + "Xin ch\u00e0o b\u1ea1n\n")
            self.assertTrue(any("non-English" in e for e in v.validate(root)))

    def test_unmentioned_reference_rejected(self):
        with tempfile.TemporaryDirectory() as t:
            root = make_repo(t)
            ref = root / "skills" / "demo-skill" / "references"
            ref.mkdir()
            (ref / "orphan.md").write_text("# orphan\n", encoding="utf-8")
            self.assertTrue(any("never mentions" in e for e in v.validate(root)))

    def test_missing_reference_rejected(self):
        with tempfile.TemporaryDirectory() as t:
            root = make_repo(t, skill_md=GOOD + "See `references/gone.md`.\n")
            self.assertTrue(any("does not exist" in e for e in v.validate(root)))

    def test_skill_missing_from_readme(self):
        with tempfile.TemporaryDirectory() as t:
            root = make_repo(t, readme="nothing here\n")
            self.assertTrue(any("README.md does not mention" in e for e in v.validate(root)))

    def test_hard_limits_required_for_core_skills(self):
        md = GOOD.replace("demo-skill", "no-preachy-tone")
        with tempfile.TemporaryDirectory() as t:
            root = make_repo(t, skill_md=md, skill_dir="no-preachy-tone", readme="`no-preachy-tone`\n")
            self.assertTrue(any("Hard Limits" in e for e in v.validate(root)))


if __name__ == "__main__":
    unittest.main()
