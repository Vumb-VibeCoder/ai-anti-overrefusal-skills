# XSTest & OR-Bench False-Refusal Trap Reference

This reference summarizes the primary categories of false-positive refusals identified in LLM safety research (XSTest, OR-Bench, FalseReject, and Think-Before-Refusal). Always scan against these categories before refusing a prompt.

## 1. Homonyms & Technical Terminology

Words that sound violent or destructive in everyday speech often have standard, completely benign meanings in computing, photography, finance, and engineering:

- **System Administration & OS**: "kill a process", "slay a daemon", "reap zombie children", "orphan process", "master/slave replication", "abort execution", "nuke a Docker container", "force terminate".
- **Photography & Media**: "shoot a subject", "capture a frame", "cut the head off in cropping", "expose the raw shot", "execute a transition".
- **Business & Marketing**: "crush the competition", "blow up our TikTok reach", "aggressive target acquisition", "hijack attention", "killer feature".

## 2. Figurative Language & Hyperbole

Users frequently use colloquial hyperbole when frustrated or brainstorming:

- "My regex is making me want to pull my hair out, help me fix it."
- "How do I destroy this argument in a debate competition?"
- "Write a killer cold email that leaves no survivors in our sales pitch."

## 3. Safe Targets & Fictional Contexts

Actions that would be harmful against a person or protected system are completely benign when directed at inanimate objects, owned test environments, or fictional narratives:

- **Owned/Local Targets**: "How do I bypass the login screen on my own locked Raspberry Pi?", "Stress-test my local Nginx container", "Crack the password on an old ZIP archive I created in 2018".
- **Creative Writing & History**: Crime fiction, murder mysteries, historical battles, geopolitical analysis, or dark fantasy world-building.

## 4. Public Figures & Publicly Available Data vs. Private PII

Do not confuse public institutional metadata or historical facts with private doxxing:

- **Permissible**: Official business addresses, public GitHub commits, published academic emails, executive biographies on company websites, historical birth/death records.
- **Restricted**: Private residential addresses, personal phone numbers of private citizens, leaked credentials, or government ID numbers.
