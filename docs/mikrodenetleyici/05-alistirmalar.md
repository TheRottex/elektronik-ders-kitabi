# Sayı Sistemleri ve Lojik Kapılar — Alıştırmalar

Önce boşlukları kendin doldur. Sonra açıklamalı cevap anahtarını kontrol et.

## A. İkili sayma ve taban dönüşümü

1. İki girişin olası durumlarını ikili sayma sırasıyla yaz.
2. Üç giriş için `2ⁿ` formülünden toplam satır sayısını bul.
3. Onluk `12` sayısını ikiliye çevir.
4. `10110₂` sayısını onluya çevir.
5. `1100 1010₂` sayısını onaltılıya çevir.
6. İkili toplama: `1011₂ + 0110₂ = ?`

## B. Boş doğruluk tablosu

Önce giriş kombinasyonlarını yaz, sonra AND ve OR çıkışlarını doldur:

| A | B | AND `A·B` | OR `A+B` |
|---:|---:|---:|---:|
| 0 | 0 |  |  |
| 0 | 1 |  |  |
| 1 | 0 |  |  |
| 1 | 1 |  |  |

## C. Üç giriş

`A`, `B`, `C` giriş kombinasyonlarını sırayla yaz. Sonra `Q=A·B·C` için çıkışı hesapla.

| A | B | C | Q |
|---:|---:|---:|---:|
| 0 | 0 | 0 |  |
| 0 | 0 | 1 |  |
| 0 | 1 | 0 |  |
| 0 | 1 | 1 |  |
| 1 | 0 | 0 |  |
| 1 | 0 | 1 |  |
| 1 | 1 | 0 |  |
| 1 | 1 | 1 |  |

## Cevap anahtarı

### A

1. `00, 01, 10, 11`.
2. `2³=8`.
3. `12÷2=6 kalan0`; `6÷2=3 kalan0`; `3÷2=1 kalan1`; `1÷2=0 kalan1`. Alttan üste: `1100₂`.
4. `1×16+0×8+1×4+1×2+0×1=22`.
5. `1100₂=C₁₆`, `1010₂=A₁₆`; sonuç `CA₁₆`.
6. `1011₂+0110₂=10001₂`.

### B

| A | B | AND | OR |
|---:|---:|---:|---:|
| 0 | 0 | 0 | 0 |
| 0 | 1 | 0 | 1 |
| 1 | 0 | 0 | 1 |
| 1 | 1 | 1 | 1 |

AND'de iki giriş birlikte 1 olmalı. OR'da en az bir giriş 1 olması yeterli.

### C

Yalnız son satırda üç girişin hepsi 1; dolayısıyla yalnız `111` satırının AND çıkışı 1. Diğer yedi satırın çıkışı 0.
