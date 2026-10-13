# canon

This folder holds the canonical source documents behind the `intel-*` agent team (`/intel-cell`) and the `staff-*` agent team (`/staff`).

| Role | Document | PDF | Markdown |
|---|---|---|---|
| Primary: analytic method | CIA, *A Tradecraft Primer: Structured Analytic Techniques* (Mar 2009) | `pdf/Tradecraft-Primer-2009.pdf` | `md/Tradecraft-Primer-2009.md` |
| Output standard | ODNI, *ICD 203: Analytic Standards* (2015, with technical amendment) | `pdf/ICD-203.pdf` | `md/ICD-203.md` |
| Tailoring standard | ODNI, *ICD 208: Maximizing the Utility of Analytic Products* (probably 9 Jan 2017) | `pdf/ICD-208.pdf` | `md/ICD-208.md` |
| Releasable versions | ODNI, *ICD 209: Tearline Production and Dissemination* (probably 6 Sep 2012) | `pdf/ICD-209.pdf` | `md/ICD-209.md` |
| Collection doctrine | Army, *ATP 2-22.9: Open-Source Intelligence* (10 Jul 2012, Unlimited Distribution) | `pdf/ATP-2-22.9-2012.pdf` | `md/ATP-2-22.9-2012.md` |
| Staff: command and control | Army, *ADP 6-0: Command and Control* (7 Jul 2026) | `pdf/ADP-6-0-2026.pdf` | `md/ADP-6-0-2026.md` |
| Staff: operations process | Army, *ADP 5-0: The Operations Process* (31 Jul 2019) | `pdf/ADP-5-0-2019.pdf` | `md/ADP-5-0-2019.md` |
| Staff: roles | Army, *FM 6-0: Commander and Staff Organization and Operations* (16 May 2022) | `pdf/FM-6-0-2022.pdf` | `md/FM-6-0-2022.md` |
| Staff: planning and orders | Army, *FM 5-0: Planning and Orders Production* (4 Nov 2024, incl. C1 Aug 2025) | `pdf/FM-5-0-2024-C1.pdf` | `md/FM-5-0-2024-C1.md` |

`sources.json` records where each document came from. `manifest.json` records the SHA-256 hash of every PDF and every Markdown file.

## Rules
1. **The PDFs are the originals, downloaded unmodified** (see `sources.json`). The Primer, ICDs 203, 208 and 209, and the four staff publications (armypubs.army.mil, public folder) come from the issuing agencies. The ATP comes from third-party mirrors, because its successor is behind an Army login; it was downloaded independently from two mirrors, which are byte-identical. A June 2017 edition exists only as a redacted FOIA release marked for U.S. Government distribution, so it isn't included.
2. **The Markdown files are mechanical conversions only.** `convert.py` runs pymupdf4llm on its rule-based path, with the ML layout model and OCR both turned off. No AI step is involved.
3. **Never hand-edit or AI-edit anything in `md/`.** To change the output, change `convert.py` and run it again: `python convert.py`.
4. **To verify integrity:** re-hash the files and compare them with `manifest.json`.

## Known conversion artifacts (faithful to the source, not errors to fix)
- **Missing "fi":** the Primer's text layer has no mapping for the "fi" ligature, so words appear as "fnished", "specifc", and so on. Read these as "finished", "specific".
- **Spaced-out section tabs:** the Primer's side tabs come through as spaced letters (**D** **I** **A** ...).
- **Stray headings:** font-size rules occasionally turn a body line into a heading (for example `## D. of this Directive.` in ICD 203).
- **ICD 208 and ICD 209 are scans** with the publisher's OCR text layer. Their signature dates are not legible in the text; `sources.json` gives the probable dates and says how each was inferred.
- **Stacked amendments:** the ICD 203 PDF puts two technical-amendment cover pages before the 2015 directive text. The Analytic Standards are in Section D.6.
