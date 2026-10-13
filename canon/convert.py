"""Mechanical PDF -> Markdown conversion for the intel-canon library.

Deterministic and rule-based only:
  * pymupdf4llm with the ML layout engine DISABLED (use_layout(False)), so
    headings come from font-size rules, not a trained model.
  * OCR disabled; text comes only from the PDF's embedded text layer.
  * No LLM or AI step anywhere. Output is written byte-for-byte as returned.

Re-run:  python convert.py
Writes md/<name>.md and manifest.json (SHA-256 of every input and output).
"""
import datetime
import hashlib
import json
import pathlib

import pymupdf
import pymupdf4llm

pymupdf4llm.use_layout(False)

ROOT = pathlib.Path(__file__).parent
SOURCES = json.loads((ROOT / "sources.json").read_text(encoding="utf-8"))


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


manifest = {
    "converted_at": datetime.datetime.now().astimezone().isoformat(timespec="seconds"),
    "converter": f"pymupdf4llm {pymupdf4llm.__version__} (rule-based path, layout model off, OCR off) on PyMuPDF {pymupdf.VersionBind}",
    "documents": [],
}

for src in SOURCES:
    pdf = ROOT / "pdf" / src["file"]
    md = ROOT / "md" / (pdf.stem + ".md")
    if not pdf.exists():
        print(f"SKIP {pdf.name}: not downloaded")
        continue
    text = pymupdf4llm.to_markdown(str(pdf), show_progress=False)
    md.write_text(text, encoding="utf-8", newline="\n")
    doc = pymupdf.open(pdf)
    manifest["documents"].append({
        **src,
        "pdf_sha256": sha256(pdf),
        "pdf_pages": doc.page_count,
        "md_file": f"md/{md.name}",
        "md_sha256": sha256(md),
        "md_chars": len(text),
    })
    print(f"{pdf.name}: {doc.page_count} pages -> {md.name} ({len(text)} chars)")

(ROOT / "manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")
