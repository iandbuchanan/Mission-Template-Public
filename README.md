# Mission-Template

I designed a reusable mission system that turns the U.S. government's own intelligence and planning doctrine (CIA analytic tradecraft, ODNI analytic standards, and Army staff manuals) into a team of AI analysts and staff officers who work from the original documents, not summaries, and advise a human commander who makes every decision.

It's a mission-agnostic **intelligence cell and staff** for Claude Code. Duplicate this repository once per mission, fill in `MISSION.md`, and run it.

- **Intelligence cell** (`/intel-cell`, 11 `intel-*` agents): finds, vets and analyzes information. Built on the CIA *Tradecraft Primer* (2009), Army ATP 2-22.9 (OSINT), and ODNI ICDs 203, 208 and 209.
- **Staff** (`/staff`, 7 `staff-*` agents): turns intelligence into plans, orders, execution and assessment. Built on Army ADP 6-0, ADP 5-0, FM 6-0 and FM 5-0.

You are the Commander. Claude is the Chief of Staff. The agents advise and draft; you decide and act.

## Start a new mission
```powershell
.\New-Mission.ps1 -Name "My-Mission"
```
The script copies this template to a sibling folder (`..\My-Mission`) and leaves out the template's git history. It then starts a fresh git repository there and makes the first commit. After that:
1. Open the new folder in Claude Code.
2. Fill in `MISSION.md`, or ask Claude to help you.
3. Run `/staff` to plan, or `/intel-cell` to investigate.

**Mission copies stay local.** Don't create them on GitHub or push them anywhere. They hold the mission's real people, targets and sensitivities. Only the template belongs on GitHub.

## Updating the template
Improve agents, playbooks or canon **here**, in the template, not in a mission copy. New missions pick the changes up automatically. Existing missions don't; copy `.claude/` and `canon/` into them by hand if you want the update there.

## Contents
| Path | What |
|---|---|
| `CLAUDE.md` | Standing rules every session follows |
| `MISSION.md` | The Commander's brief (blank in the template) |
| `.claude/agents/` | 18 subagents (`intel-*`, `staff-*`) |
| `.claude/skills/` | Playbooks: `intel-cell` (chief of analysis) and `staff` (Chief of Staff) |
| `canon/` | 9 source documents: original PDFs, mechanical Markdown conversions, provenance and SHA-256 hashes |
| `intel/` `staff/` `orders/` `logs/` | Mission products (empty in the template) |

## Provenance
All canon documents are US Government publications, not subject to copyright in the United States, obtained from public sources; see `canon/sources.json`. A few reproduce quotations from copyrighted works with their owners' permission, and those quotations remain their owners'. The Markdown is produced by `canon/convert.py` with no AI step. The agent and playbook instructions summarize that doctrine and point back to it; where they differ, the canon wins.

`canon/convert.py` uses PyMuPDF and pymupdf4llm, which are licensed under the GNU AGPL 3.0 (or a commercial license from Artifex). They aren't included here; install them yourself if you want to rerun the conversion.

## License
MIT for everything written for this project; see [LICENSE](LICENSE). The canon documents aren't covered; see [NOTICE.md](NOTICE.md).
