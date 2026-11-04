# Mikrodenetleyici — Sayı Sistemleri ve Mantık Kapıları

**Kaynak:** *Mikrodenetleyici*, PDF 1–40. PDF 1–17 kapak, ön bilgiler ve bölüm tanıtımıdır. Sayı sistemleri PDF 18'de, temel lojik kapı tanıtımı PDF 37'de başlar. İlk 40 sayfada özellikle ikilik sayılar, taban dönüşümleri, AND/OR kapıları ve uygulamalar yer alır.

## Konu haritası

| PDF sayfaları | Kaynak konusu | Bu rehber |
|---:|---|---|
| 18–19 | Sayı sistemi, onluk/ikilik/sekizlik/onaltılık | [İkili sayı sistemi](01-ikili-sayi-sistemi.md) |
| 20–27 | İkili, sekizlik, onaltılık sayılarda işlemler | [İkili sayı sistemi](01-ikili-sayi-sistemi.md) |
| 28–36 | Tabanlar arasında dönüşüm ve değerlendirme | [İkili sayı sistemi](01-ikili-sayi-sistemi.md), [alıştırmalar](05-alistirmalar.md) |
| 37–39 | Temel kapılar; AND kapısı, 4081/7408 uygulaması | [VE ve VEYA kapıları](02-lojik-kapilar.md) |
| 39–40 | OR kapısı tanımı ve uygulaması | [VE ve VEYA kapıları](02-lojik-kapilar.md) |

## Önerilen sıra

1. Bit, basamak ve sayı değerinin farkını öğren.
2. `00, 01, 10, 11` dizisinin ikili sayma olduğunu gör.
3. Onluk ↔ ikilik dönüşümü ve 3 bit / 4 bit sayıların kapsamını çalış.
4. Doğruluk tablosu satırlarını üret: n girişte `2ⁿ` durum.
5. Önce AND, sonra OR için her satırın çıkışını kendin hesapla.
6. Boş tabloları [alıştırmalarda](05-alistirmalar.md) doldur, ardından cevap anahtarını aç.

## Kaynak ile ek bilginin ayrımı

- **Kaynakta (PDF 18–40):** sayı sistemleri ve taban dönüşümleri; temel lojik kapılar tanıtımı; VE (AND), VEYA (OR) ve 4081/7408 ile uygulama.
- **Kısa tamamlayıcı anlatım:** NOT kapısı, aynı PDF'de PDF 37'de temel kapı olarak sayılır.
- **Bu sayfa aralığının dışında, ek bilgi:** NAND, NOR, XOR, XNOR'un ayrıntılı doğruluk tabloları; mikrodenetleyicinin portları ve Arduino benzeri kartla buton/LED örneği.

Ek konuları, kaynakta öğretilmiş gibi göstermemek için ilgili bölümde ayrıca etiketledim.
