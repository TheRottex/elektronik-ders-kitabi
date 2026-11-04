import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[1]
LINK_PATTERN = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")


def main():
    failures = []
    markdown_files = list(ROOT.rglob("*.md"))
    for markdown_file in markdown_files:
        text = markdown_file.read_text(encoding="utf-8")
        text = re.sub(r"(?ms)^[ \t]*```.*?^[ \t]*```[ \t]*", "", text)
        for target in LINK_PATTERN.findall(text):
            target = target.strip().split()[0].strip("<>")
            if not target or target.startswith("#"):
                continue
            parsed = urlparse(target)
            if parsed.scheme or target.startswith("//"):
                continue
            local_target = target.split("#", 1)[0].split("?", 1)[0]
            if not local_target:
                continue
            resolved = (markdown_file.parent / local_target).resolve()
            if not resolved.is_file():
                failures.append(f"Broken Markdown link: {markdown_file.relative_to(ROOT)} -> {target}")

    for svg_file in ROOT.rglob("*.svg"):
        try:
            ET.parse(svg_file)
        except ET.ParseError as error:
            failures.append(f"Invalid SVG: {svg_file.relative_to(ROOT)}: {error}")

    included_pdfs = [
        path for path in ROOT.rglob("*.pdf") if path.name.casefold() != "kitap.pdf"
    ]
    if included_pdfs:
        failures.extend(f"Unexpected source PDF: {path.relative_to(ROOT)}" for path in included_pdfs)

    expected = [
        "docs/elektronik/04-seri-paralel-karisik.md",
        "docs/elektronik/05-kopru-yildiz-ucgen.md",
        "docs/mikrodenetleyici/02-lojik-kapilar.md",
        "docs/mikrodenetleyici/05-alistirmalar.md",
        "assets/diagrams/lojik-kapilar.svg",
    ]
    for relative_path in expected:
        if not (ROOT / relative_path).is_file():
            failures.append(f"Missing required course asset: {relative_path}")

    if failures:
        print("\n".join(failures))
        return 1

    print(
        f"Validated {len(markdown_files)} Markdown files and "
        f"{len(list(ROOT.rglob('*.svg')))} SVG diagrams; no source PDFs included."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
