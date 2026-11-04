# Mikrodenetleyici — Lojik Kapılar ve Entegre ile Devre Kurma (2 soru)

Kaynak: Mikrodenetleyici PDF s.38–70. Giriş: A, B, C…; çıkış: Q. `·` VE (AND), `+` VEYA (OR), `'` (üstü çizgili) DEĞİL (NOT).

## 1. Kapı özeti (hepsi sınavlık)

| Kapı | İfade | Çıkış 1 olur… |
|------|-------|---------------|
| NOT | Q = A' | giriş 0 iken |
| AND | Q = A·B | **iki giriş de 1** |
| OR | Q = A+B | **en az biri 1** |
| NAND | Q = (A·B)' | AND'in tersi: yalnızca 11'de 0 |
| NOR | Q = (A+B)' | OR'un tersi: yalnızca 00'da 1 |
| XOR | Q = A⊕B | girişler **farklı** |
| XNOR | Q = (A⊕B)' | girişler **aynı** |

| A B | AND | OR | NAND | NOR | XOR | XNOR |
|:---:|:---:|:--:|:----:|:---:|:---:|:----:|
| 0 0 | 0 | 0 | 1 | 1 | 0 | 1 |
| 0 1 | 0 | 1 | 1 | 0 | 1 | 0 |
| 1 0 | 0 | 1 | 1 | 0 | 1 | 0 |
| 1 1 | 1 | 1 | 0 | 0 | 0 | 1 |

## 2. Boole kuralları

| Kural | İfade |
|-------|-------|
| VE ile 0 / 1 | A·0 = 0 · A·1 = A |
| VEYA ile 0 / 1 | A+0 = A · A+1 = 1 |
| Aynı değişken | A·A = A · A+A = A |
| Tümleyen | A·A' = 0 · A+A' = 1 |
| Çift tersleme | (A')' = A |
| Değişme | A·B = B·A · A+B = B+A |
| Birleşme | (A·B)·C = A·(B·C) · (A+B)+C = A+(B+C) |
| Dağılma | A·(B+C) = A·B + A·C · A+B·C = (A+B)(A+C) |
| Yutma | A+A·B = A · A·(A+B) = A |

## 3. De Morgan kuralları

`(A·B)' = A' + B'` ve `(A+B)' = A'·B'` — "çizgiyi kır, işareti değiştir".

Doğrulama (A=1, B=0): (1·0)' = 1 ; 1' + 0' = 0+1 = 1 ✔ · (1+0)' = 0 ; 1'·0' = 0·1 = 0 ✔

Sadeleştirme örneği: `Q = A·B + A·B'` = A·(B+B') = A·1 = **A**.

## 4. İfadeden doğruluk tablosu ve devreden ifade

**Q = A + B·C** (önce VE, sonra VEYA):

| A B C | B·C | Q |
|:-----:|:---:|:-:|
| 0 0 0 | 0 | 0 |
| 0 0 1 | 0 | 0 |
| 0 1 0 | 0 | 0 |
| 0 1 1 | 1 | 1 |
| 1 0 0 | 0 | 1 |
| 1 0 1 | 0 | 1 |
| 1 1 0 | 0 | 1 |
| 1 1 1 | 1 | 1 |

n girişte **2ⁿ** satır vardır (3 giriş → 8). Giriş sıralaması ikili sayma sırasıdır: 000 → 111.

**Devreden ifade çıkarma:** girişten çıkışa doğru her kapının çıkışını yaz. Örn. iki AND (A·B ve C·D) bir OR'a bağlanırsa Q = A·B + C·D. İki OR (A+B ve C+D) bir AND'e bağlanırsa Q = (A+B)·(C+D).

**İfadeden devre çizme:** en içteki parantezden başla; her işlem bir kapı. `Q = A·C' + A'·C` → 2 NOT, 2 AND, 1 OR (bu devre XOR işlevi görür).

## 5. Lojik entegreler

| Kapı | TTL (74 serisi) | CMOS (4000 serisi) | Kapı sayısı |
|------|-----------------|--------------------|-------------|
| NOT | 7404 | 4069 | 6 |
| AND | 7408 | 4081 | 4 (2 girişli) |
| OR | 7432 | 4071 | 4 |
| NAND | 7400 | 4011 | 4 |
| NOR | 7402 | 4001 | 4 |
| XOR | 7486 | 4070 | 4 |

- **TTL besleme:** 5 V. **CMOS (4000):** yaklaşık 3–15 V (genelde 5–12 V). 74HC serisi 5 V civarı. Pin yorumunda bu değerler kitap kullanım örneğine göredir; kesin değer için entegre veri sayfasına bakın.
- Entegre 14 bacaklı DIP kılıf: çentik **yukarıda** tutulurken sol üstten saat yönünün tersine 1'den 14'e numaralanır. **Pin 14 = Vcc (+), Pin 7 = GND (−).**
- 7408 / 7400 / 7432 bacakları: 1A=1, 1B=2, 1Y=3 · 2A=4, 2B=5, 2Y=6 · 3Y=8, 3A=9, 3B=10 · 4Y=11, 4A=12, 4B=13. (7402'de çıkış Y önce gelir: 1Y=1, 1A=2, 1B=3.)
- **Kullanılmayan girişi boş bırakma:** AND/NAND için +5 V'a, OR/NOR için GND'ye bağla.
- Girişler anahtarla verilirken **pull-down** (anahtar açıkken girişi dirençle GND'ye bağla) ya da pull-up direnci kullanılır; yoksa giriş "havada" kalır ve belirsiz okunur.

## 6. Entegre seçimi: örnek

**Q = A·B + C·D** için malzeme: 2 adet AND + 1 adet OR → **bir 7408** (4 AND içerir, 2'si kullanılır) + **bir 7432** (1 OR).
**Q = (A+B)·(C+D)** için: 2 OR + 1 AND → **bir 7432** + **bir 7408**.
**Q = A·C' + A'·C** için: 7404 (2 NOT), 7408 (2 AND), 7432 (1 OR) → toplam 3 entegre.

Birden fazla kapı gerekiyorsa bir entegre içinde yeterli kapı olup olmadığına bak; yoksa ikinci bir entegre kullan.

## 7. Breadboard'da devre kurma — Q = A·B + C·D

Malzeme: 7408, 7432, 5 V besleme, 4'lü DIP anahtar, kırmızı LED, 470 Ω × 5 (4 giriş pull-down + 1 LED).
Adımlar:
1. Enerji kapalıyken entegreleri breadboard orta yarığına yerleştir.
2. Her entegrede pin 14 → +5 V, pin 7 → GND.
3. A, B → 7408 kapı 1 (1,2) ; C, D → kapı 2 (4,5). Çıkışlar pin 3 ve pin 6.
4. Pin 3 → 7432 pin 1, pin 6 → 7432 pin 2; OR çıkışı pin 3.
5. Anahtarın bir ucu +5 V'a, diğer ucu giriş ve 470 Ω ile GND'ye (anahtar açıkken 0).
6. OR çıkışı (7432 pin 3) → 470 Ω → LED anot; LED katot → GND.
7. Besleme ver; A=B=1 **veya** C=D=1 iken LED yanar; aksi halde söner.

**Güvenlik:** besleme polaritesini kontrol et, entegre ısınıyorsa hemen enerjiyi kes, LED'i dirençsiz bağlama.

## 8. Kendin çöz

1. NAND kapısının 11 girişinde çıkış? 2. (A+B)' ifadesini De Morgan ile yaz. 3. Q = A·B' için tablo çıkar. 4. Q = (A+B)·C için kaç entegre ve hangileri? 5. 14 bacaklı entegrede Vcc hangi pindedir?

**Cevaplar:** 1) 0. 2) A'·B'. 3) Yalnızca A=1,B=0 iken Q=1 (diğer 3 satır 0). 4) 7432 (OR) + 7408 (AND). 5) Pin 14 (GND pin 7).
