# Mission-Template

Your own AI research and planning team for any big goal: a job hunt, a move, a launch, a dispute. It finds and checks the facts, pokes holes in your thinking, weighs your options and drafts the plan. You make every decision; it never acts for you.

## What it does
You write down what you're trying to achieve, by when, and what you won't risk. Then a team of AI helpers in Claude Code goes to work:

- **Research.** They find information, check how reliable it is, and tell you plainly what's known, what's assumed and what's still a guess.
- **Pushback.** Some helpers exist only to argue the other side, test your assumptions, and ask "what if we're wrong?"
- **Options and a plan.** They lay out a few ways to get there, compare them on time, money and risk, and turn the one you choose into a step-by-step plan.
- **Drafts, not actions.** They write the emails, posts and messages, and you decide whether to send them. Nothing goes out without you.
- **A paper trail.** Research, options and decisions are saved as files, so you can pick up next week where you left off and see why each call was made.

It's worth the setup when a decision is costly to get wrong and worth a few hours of careful thinking. For quick questions, just ask Claude.

## Why it's built this way
The helpers follow methods that professionals already rely on: the CIA's guide to structured analysis, the U.S. intelligence community's standards for honest, clearly labeled judgments, and the Army's process for planning and running operations. They work from the original documents, kept in `canon/`, not from summaries.

That's where the vocabulary comes from. You are the **Commander**, Claude is your **Chief of Staff**, and there are two teams:

- **Intelligence cell** (`/intel-cell`, 11 `intel-*` agents) finds, vets and analyzes information. It's built on the CIA *Tradecraft Primer* (2009), Army ATP 2-22.9 (open-source intelligence), and ODNI ICDs 203, 208 and 209.
- **Staff** (`/staff`, 7 `staff-*` agents) turns that into plans, orders, execution and assessment. It's built on Army ADP 6-0, ADP 5-0, FM 6-0 and FM 5-0.

Duplicate this repository once per goal, fill in `MISSION.md`, and run it.

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
