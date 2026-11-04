import os
import re
import gc
from pathlib import Path

import markdown
import pymupdf

from build_book import CHAPTERS, ROOT, rewrite_links_for_book


def find_font_directory():
    candidates = []
    windows_directory = os.environ.get("WINDIR")
    if windows_directory:
        candidates.append(Path(windows_directory) / "Fonts")
    candidates.extend(
        [
            Path("/usr/share/fonts/truetype/dejavu"),
            Path("/usr/share/fonts/truetype/liberation2"),
            Path("/Library/Fonts"),
        ]
    )
    for directory in candidates:
        for font_file in ("arial.ttf", "DejaVuSans.ttf", "LiberationSans-Regular.ttf"):
            if (directory / font_file).is_file():
                return directory, font_file
    raise FileNotFoundError(
        "A Turkish-capable TrueType font was not found. Install Arial, DejaVu Sans, "
        "or Liberation Sans and rerun the PDF builder."
    )


def chapter_html(index, relative_path):
    source = (ROOT / relative_path).read_text(encoding="utf-8").rstrip()
    source = rewrite_links_for_book(source, relative_path)
    source = re.sub(
        r"^# (.+)$",
        lambda match: f'<h1 id="chapter-{index:02}">{match.group(1)}</h1>',
        source,
        count=1,
        flags=re.MULTILINE,
    )
    return markdown.markdown(source, extensions=["tables", "fenced_code"])


def build_html():
    contents = []
    rendered_chapters = []
    for index, (_, relative_path) in enumerate(CHAPTERS, start=1):
        body = chapter_html(index, relative_path)
        first_heading = re.search(r"<h1[^>]*>(.*?)</h1>", body, flags=re.DOTALL)
        title = first_heading.group(1) if first_heading else relative_path
        contents.append(f'<li><a href="#chapter-{index:02}">{title}</a></li>')
        rendered_chapters.append(body)

    return f"""<!doctype html>
<html lang="tr">
<head><meta charset="utf-8"><title>Görsel Destekli Elektronik Ders Kitabı</title></head>
<body>
<section class="cover">
  <p class="eyebrow">BAŞLANGIÇ SEVİYESİ • GÖRSEL DERS REHBERİ</p>
  <h1>Görsel Destekli Elektronik ve Mikrodenetleyici Ders Kitabı</h1>
  <p>Elektrik devreleri, ölçüm, sayı sistemleri ve temel lojik kapılar için adım adım çalışma kaynağı.</p>
  <div class="scope">Elektronik Uygulamaları PDF 1–72 • Mikrodenetleyici PDF 1–40</div>
  <p class="note">Kaynak kitap görsellerinin yerine özgün şemalar çizilmiştir. Kaynak PDF dosyaları bu çıktıya eklenmemiştir.</p>
</section>
<section class="contents"><h1>İçindekiler</h1><ol>{''.join(contents)}</ol></section>
{''.join(rendered_chapters)}
</body></html>"""


def main():
    font_directory, font_file = find_font_directory()
    css = f"""
    @font-face {{ font-family: LessonSans; src: url(fonts/{font_file}) format("truetype"); }}
    body {{ font-family: LessonSans, sans-serif; font-size: 10.5pt; color: #23384a; line-height: 1.42; }}
    h1 {{ color: #173c59; font-size: 23pt; border-bottom: 2px solid #7bb4cf; padding-bottom: 7pt; page-break-before: always; }}
    .cover h1, .contents h1 {{ page-break-before: avoid; }}
    h2 {{ color: #226b87; font-size: 16pt; margin-top: 20pt; }}
    h3 {{ color: #286f79; font-size: 12.5pt; margin-top: 15pt; }}
    p, li {{ margin-bottom: 6pt; }}
    table {{ border-collapse: collapse; width: 100%; margin: 10pt 0 15pt 0; font-size: 9pt; }}
    th {{ background: #e7f2f7; color: #173c59; }}
    th, td {{ border: 1px solid #b9ccd7; padding: 5pt; }}
    blockquote {{ border-left: 4px solid #e6aa45; padding: 5pt 10pt; background: #fff8e9; }}
    code {{ font-family: LessonSans, monospace; background: #eef3f6; }}
    pre {{ background: #eff4f7; padding: 10pt; white-space: pre-wrap; }}
    img {{ max-width: 100%; max-height: 330pt; object-fit: contain; }}
    .cover {{ padding-top: 120pt; }}
    .cover h1 {{ font-size: 31pt; }}
    .eyebrow {{ color: #287c91; font-weight: bold; }}
    .scope {{ margin-top: 30pt; padding: 12pt; background: #e7f2f7; }}
    .note {{ color: #5c6e7a; margin-top: 45pt; }}
    .contents {{ page-break-before: always; page-break-after: always; }}
    a {{ color: #176f96; text-decoration: none; }}
    """
    archive = pymupdf.Archive(str(ROOT))
    archive.add(str(font_directory), path="fonts")
    story = pymupdf.Story(html=build_html(), user_css=css, archive=archive)
    output = ROOT / "KITAP.pdf"
    uncompressed_output = ROOT / "KITAP.uncompressed.pdf"
    page_rect = pymupdf.paper_rect("a4")
    content_rect = pymupdf.Rect(48, 48, page_rect.width - 48, page_rect.height - 48)
    writer = pymupdf.DocumentWriter(str(uncompressed_output))
    try:
        while True:
            page = writer.begin_page(page_rect)
            more, _ = story.place(content_rect)
            story.draw(page)
            writer.end_page()
            if not more:
                break
    finally:
        writer.close()
    del page, writer, story
    gc.collect()

    document = pymupdf.open(uncompressed_output)
    document.save(
        str(output),
        garbage=4,
        deflate=1,
        deflate_images=1,
        deflate_fonts=1,
        compression_effort=100,
    )
    pages = len(document)
    text = "\n".join(page.get_text() for page in document)
    image_count = sum(len(page.get_images()) for page in document)
    document.close()
    del document
    gc.collect()
    uncompressed_output.unlink(missing_ok=True)
    required_text = ("Mikrodenetleyici", "Elektriksel Büyüklükler", "öğrenci", "İçindekiler")
    normalized_text = text.replace("\u0d88", "i").replace("\xa0", " ")
    if (
        pages < len(CHAPTERS)
        or image_count == 0
        or any(term not in normalized_text for term in required_text)
        or "\ufffd" in text
    ):
        output.unlink(missing_ok=True)
        raise RuntimeError(
            "The PDF output did not pass its page, text, or embedded-diagram checks."
        )
    print(f"Generated {output.name}: {pages} A4 pages, {output.stat().st_size:,} bytes.")


if __name__ == "__main__":
    main()
