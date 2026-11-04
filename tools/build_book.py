from pathlib import Path
import re
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[1]
CHAPTERS = [
    ("Elektronik Uygulamaları", "docs/elektronik/00-ders-haritasi.md"),
    ("Elektronik Uygulamaları", "docs/elektronik/01-buyuklukler-birimler.md"),
    ("Elektronik Uygulamaları", "docs/elektronik/02-devre-elemanlari.md"),
    ("Elektronik Uygulamaları", "docs/elektronik/03-ohm-kanunu-ve-guc.md"),
    ("Elektronik Uygulamaları", "docs/elektronik/04-seri-paralel-karisik.md"),
    ("Elektronik Uygulamaları", "docs/elektronik/05-kopru-yildiz-ucgen.md"),
    ("Elektronik Uygulamaları", "docs/elektronik/06-olcum-ve-guvenlik.md"),
    ("Elektronik Uygulamaları", "docs/elektronik/07-frekans-periyot.md"),
    ("Elektronik Uygulamaları", "docs/elektronik/08-alistirmalar.md"),
    ("Mikrodenetleyici", "docs/mikrodenetleyici/00-ders-haritasi.md"),
    ("Mikrodenetleyici", "docs/mikrodenetleyici/01-ikili-sayi-sistemi.md"),
    ("Mikrodenetleyici", "docs/mikrodenetleyici/02-lojik-kapilar.md"),
    ("Mikrodenetleyici", "docs/mikrodenetleyici/03-diger-kapilar.md"),
    ("Mikrodenetleyici", "docs/mikrodenetleyici/04-mikrodenetleyici-uygulama.md"),
    ("Mikrodenetleyici", "docs/mikrodenetleyici/05-alistirmalar.md"),
    ("Sınava Odaklı Çalışma", "docs/sinav/00-sinav-haritasi.md"),
    ("Sınava Odaklı Çalışma", "docs/sinav/01-elektronik-sinav-calismasi.md"),
    ("Sınava Odaklı Çalışma", "docs/sinav/02-mikro-sayi-sistemleri-sinav.md"),
    ("Sınava Odaklı Çalışma", "docs/sinav/03-mikro-lojik-entegre-sinav.md"),
    ("Sınava Odaklı Çalışma", "docs/sinav/04-deneme-sinavi-ve-cevaplar.md"),
]
LINK_PATTERN = re.compile(r"(!?\[[^\]]*\]\()([^)]+)(\))")


def rewrite_links_for_book(markdown, source_path):
    source_directory = (ROOT / source_path).parent

    def replace(match):
        target = match.group(2).strip()
        parsed = urlparse(target)
        if parsed.scheme or target.startswith(("#", "//")):
            return match.group(0)

        target_path, separator, fragment = target.partition("#")
        resolved = (source_directory / target_path).resolve()
        normalized = resolved.relative_to(ROOT).as_posix()
        if separator:
            normalized += f"#{fragment}"
        return f"{match.group(1)}{normalized}{match.group(3)}"

    return LINK_PATTERN.sub(replace, markdown)


def main():
    parts = [
        "# Görsel Destekli Elektronik ve Mikrodenetleyici Ders Kitabı",
        "",
        "> Bu dosya `tools/build_book.py` ile bölüm Markdown dosyalarından üretilir. "
        "Bölümleri düzenledikten sonra aynı komutu yeniden çalıştırın.",
        "",
        "## İçindekiler",
        "",
    ]
    for index, (section, relative_path) in enumerate(CHAPTERS, start=1):
        title = next(
            line.removeprefix("# ").strip()
            for line in (ROOT / relative_path).read_text(encoding="utf-8").splitlines()
            if line.startswith("# ")
        )
        parts.append(f"- [{section}: {title}](#chapter-{index:02})")

    for index, (_, relative_path) in enumerate(CHAPTERS, start=1):
        parts.extend(
            [
                "",
                "\n---\n",
                f'<a id="chapter-{index:02}"></a>',
                "",
                rewrite_links_for_book(
                    (ROOT / relative_path).read_text(encoding="utf-8").rstrip(),
                    relative_path,
                ),
            ]
        )

    (ROOT / "KITAP.md").write_text("\n".join(parts) + "\n", encoding="utf-8")
    print(f"Generated KITAP.md from {len(CHAPTERS)} chapters.")


if __name__ == "__main__":
    main()
