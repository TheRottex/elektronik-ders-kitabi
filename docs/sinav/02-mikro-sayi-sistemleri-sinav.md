# Mikrodenetleyici — Sayı Sistemleri ve Sayısal İşlemler (3 soru)

Kaynak: Mikrodenetleyici PDF s.18–45. Sistemler: **ikilik (2)**, **sekizlik (8)**, **onluk (10)**, **onaltılık (16)**. Onaltılıkta rakamlar: 0–9, A=10, B=11, C=12, D=13, E=14, F=15.

## 1. Temel kural: basamak ağırlıkları

- İkilik: …, 32, 16, 8, 4, 2, 1 (2'nin kuvvetleri)
- Sekizlik: …, 512, 64, 8, 1
- Onaltılık: …, 4096, 256, 16, 1

Taban kadar değere ulaşınca o basamak 0 olur, **1 elde** soldaki basamağa gider (ikilikte 1+1 = 10, sekizlikte 7+1 = 10, onaltılıkta F+1 = 10).

## 2. İkilik işlemler

### Toplama
Kural: 0+0=0 · 0+1=1 · 1+1=**10** (0 yaz, 1 elde) · 1+1+1=**11** (1 yaz, 1 elde)

**1110 + 0101**
```
  1 1 1 0     (elde: soldan sağa 1,1,1 oluşur)
+ 0 1 0 1
---------
1 0 0 1 1
```
Sağdan: 0+1=1 · 1+0=1 · 1+1=0 elde 1 · 1+0+elde 1=0 elde 1 · elde 1 → **10011** (14+5=19 ✔).

### Çıkarma (borç alma)
Kural: 0−0=0 · 1−0=1 · 1−1=0 · **0−1 → soldan borç al:** 10−1=1, soldaki basamak 1 azalır.

**1001 − 0111**: bit0: 1−1=0 · bit1: 0−1 olmaz, soldan borç gerekir; bit2 de 0 olduğundan borç bit3'ten gelir (bit3: 1→0, bit2: 0→10, bit2 de bit1'e 1 verir, kendinde 1 kalır) → bit1: 10−1=1 · bit2: 1−1=0 · bit3: 0−0=0 → **0010**. Doğrulama: 9−7=2 ✔.
**101 − 10 = 011** (5−2=3 ✔).

### Çarpma
Onluktaki gibi: ×0 → 0, ×1 → sayının kendisi, her satır bir basamak sola kaydırılır, sonra toplanır.
**10 × 10 = 100** (2×2=4 ✔). **110 × 11**: 110 + 1100 = **10010** (6×3=18 ✔).

### Bölme
Onluktaki uzun bölme gibi; 1 sığıyorsa 1, sığmıyorsa 0 yazılır.
**10100 ÷ 10 = 1010** (20÷2=10 ✔). **11011 ÷ 11 = 1001** (27÷3=9 ✔).

## 3. Sekizlik işlemler

Toplam 8 veya üzeriyse 8'e böl: kalan yazılır, bölüm elde olur.

**725 + 534**: 5+4=9=8+1 → yaz 1 elde 1 · 2+3+1=6 · 7+5=12=8+4 → yaz 4 elde 1 → **1461₈**.

**704 − 651**: 4−1=3 · 0−5 → borç, 8+0−5=3 · 7−1(borç)−6=0 → **033₈**.

## 4. Onaltılık işlemler

**79A + 5C8**: A+8=10+8=18=16+2 → yaz 2 elde 1 · 9+C+1=9+12+1=22=16+6 → yaz 6 elde 1 · 7+5+1=13=D → **D62₁₆**.

**AD8 − 7E3**: 8−3=5 · D−E: 13−14 → borç, 16+13−14=15=F · A−1−7=10−1−7=2 → **2F5₁₆**.

## 5. Dönüşümler

| İstek | Yöntem |
|-------|--------|
| Onluk → ikilik | 2'ye art arda böl, kalanları **alttan yukarı** oku |
| Onluk → sekizlik/onaltılık | 8'e/16'ya böl, kalanları alttan yukarı oku |
| İkilik/sekizlik/onaltılık → onluk | Her rakamı basamak ağırlığıyla çarp, topla |
| İkilik → sekizlik | Sağdan **3'erli** grupla |
| İkilik → onaltılık | Sağdan **4'erli** grupla |
| Sekizlik/onaltılık → ikilik | Her rakamı 3 / 4 bitlik karşılığa aç |

**Onluk → ikilik, 35₁₀:** 35÷2=17 k1 · 17÷2=8 k1 · 8÷2=4 k0 · 4÷2=2 k0 · 2÷2=1 k0 · 1÷2=0 k1 → alttan yukarı **100011₂**.

**Onluk → onaltılık, 185₁₀:** 185÷16=11 kalan 9 · 11 = B → **B9₁₆**.

**Onaltılık → onluk, 7B3₁₆:** 7×256 + 11×16 + 3 = 1792 + 176 + 3 = **1971₁₀**.

**İkilik → onluk, 101101₂:** 32+8+4+1 = **45₁₀**.

**İkilik → onaltılık, 1110110001₂:** 0011 1011 0001 → **3B1₁₆**.

**İkilik → sekizlik, 1110110001₂:** 001 110 110 001 → **1661₈**.

**Onaltılık → ikilik, 1A3₁₆:** 1=0001, A=1010, 3=0011 → **110100011₂** (baştaki sıfırlar atılır).

**Sekizlik → ikilik, 273₈:** 2=010, 7=111, 3=011 → **10111011₂**.

## 6. Kitaptaki dönüşüm sorularının cevapları

| Soru | Cevap |
|------|-------|
| 35₁₀, 51₁₀, 64₁₀ → ikilik | 100011, 110011, 1000000 |
| 38₁₀, 185₁₀, 216₁₀ → onaltılık | 26, B9, D8 |
| 101101₂, 11101010₂, 101011₂ → onluk | 45, 234, 43 |
| 7B3₁₆, 26EA₁₆, 15B₁₆ → onluk | 1971, 9962, 347 |
| 1A3₁₆, F4C6₁₆, A5D7₁₆ → ikilik | 110100011, 1111010011000110, 1010010111010111 |
| 1110110001₂, 1110110001000011₂, 111110001011011₂ → onaltılık | 3B1, EC43, 7C5B |
| 273₈, 654₈ → ikilik | 10111011, 110101100 |
| 1110110001₂, 111101100₂ → sekizlik | 1661, 754 |

## 7. "Sıra sizde" işlemlerinin cevapları

| İşlem | Sonuç |
|-------|-------|
| 1101 + 1110 | 11011 |
| 10001 − 01111 | 10 |
| 110 × 11 | 10010 |
| 11011 ÷ 11 | 1001 |
| 657₈ + 433₈ | 1312₈ |
| 523₈ − 345₈ | 156₈ |
| EFC₁₆ + 975₁₆ | 1871₁₆ |
| B39₁₆ − 34A₁₆ | 7EF₁₆ |

## 8. Sık yapılan hatalar

- Onluk **12**'yi "12 tane 1" sanmak: 12₁₀ = 1100₂.
- İkili toplamada 1+1'i "2" yazmak: doğrusu **10**.
- Onluk → ikilide kalanları yukarıdan aşağı okumak: **alttan yukarı** okunur.
- Hex'te A–F değerlerini unutmak: B = 11, E = 14.
- Gruplamayı soldan yapmak: ikilik→hex/oktal dönüşümünde **sağdan** gruplanır, eksik gruplar soldan 0 ile tamamlanır.
