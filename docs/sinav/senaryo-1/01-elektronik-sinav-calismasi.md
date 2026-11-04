# Elektronik Uygulamaları — 1. Senaryo Sınav Çalışması

Kaynak: Elektronik Uygulamaları PDF s.18–67. Konu anlatımlarının bir kısmı [2. Senaryo çalışmasıyla](../senaryo-2/01-elektronik-sinav-calismasi.md) ortaktır; burada yalnızca 1. Senaryoya özgü **direnç** ayrıntılı, diğerleri sınav özetidir.

## 1. Direnç (1 soru)

**Ne işe yarar?** Akıma karşı zorluk gösterir; akımı sınırlar, gerilim böler. Harf **R**, birim **ohm (Ω)**.

**4 bantlı renk kodu:** 1. bant 1. rakam · 2. bant 2. rakam · 3. bant çarpan (sıfır sayısı) · 4. bant tolerans.

| Renk | Rakam | Renk | Rakam |
|------|:-----:|------|:-----:|
| Siyah | 0 | Mavi | 6 |
| Kahverengi | 1 | Mor | 7 |
| Kırmızı | 2 | Gri | 8 |
| Turuncu | 3 | Beyaz | 9 |
| Sarı | 4 | Altın | tolerans ±%5 (çarpan ×0,1) |
| Yeşil | 5 | Gümüş | tolerans ±%10 (çarpan ×0,01) |

**Örnek (kitaptaki 12. soru):** 4700 Ω ±%5 → 47 × 100 → sarı (4) – mor (7) – **kırmızı** (×100) – altın. Doğru şık: **Sarı-mor-kırmızı-altın**.
**Örnek:** kahverengi-siyah-turuncu-altın = 10 × 1000 = 10 kΩ ±%5.

**Direnç seçerken üç ölçüt:** değer (Ω), **tolerans** (%) ve **güç** (W: 1/8, 1/4, 1/2 W…). Güç için `P = I² × R` ya da `P = V × I` hesaplanır, direnç gücü hesaplanandan büyük seçilir (çoğu kez 2 katı güvenli).
Örnek: 10 Ω dirençten 0,2 A geçerse P = 0,04 × 10 = 0,4 W → 1/2 W direnç yeter, ama güvenlik payı için **1 W** seçilir.

| Direnç türü | Özellik |
|-------------|---------|
| Sabit direnç | Değeri değişmez |
| Potansiyometre | Ayarlı, 3 bacak, el ile ayarlanan (ses, parlaklık) |
| Trimpot | Ayarlı, küçük; devre kurulurken tornavidayla bir kez ayarlanır |
| Reosta | Yüksek akım için ayarlı direnç |
| LDR | Işık şiddetine göre değeri değişen (ışıkta azalır) |
| NTC | Sıcaklık **arttıkça** direnci **azalır** |
| PTC | Sıcaklık arttıkça direnci artar |

## 2. Kondansatör (1 soru)

Birim F; 1 µF = 1000 nF; 1 nF = 1000 pF. Kod: ilk iki rakam + üçüncü rakam kadar sıfır (pF): **105 = 1 µF**, 104 = 100 nF, 103 = 10 nF, 102 = 1 nF, 473 = 47 nF. Elektrolitik **kutuplu**: eksi bacak işaretli, çalışma gerilimi devre geriliminden büyük. Mika kondansatörün dielektriği **mika**. Ayrıntı: [Kondansatör](../senaryo-2/01-elektronik-sinav-calismasi.md).

## 3. Bobin (1 soru)

Birim **henri (H)**, harf **L**. DC'de akıma neredeyse kısa devre, AC'de frekansla artan `XL = 2πfL`. Çeşitler: hava, ferit, demir, toroid, SMD. LCR metre ile ölçülür. Ayrıntı: [Bobin](../senaryo-2/01-elektronik-sinav-calismasi.md).

## 4. Diyot (1 soru)

İki bacak: anot (+) ve katot (−, çizgili uç). Türler: kristal, zener, Şotki, LED, IR LED (görünmez kızılötesi), varikap, köprü. LED direnci `Rs = (Vcc − Vd)/Id`. Test: diyot kademesi, kırmızı anot / siyah katot → değer; ters → "1" (OL). Ayrıntı: [Diyot](../senaryo-2/01-elektronik-sinav-calismasi.md).

## 5. Transistör (1 soru)

C, B, E; NPN ve PNP. NPN'de B ve C +, E −. Anahtar: doyum (C–E ≈ 0 V) ve kesim (akım 0). Testte kırmızı prob ortak ve değer varsa NPN; küçük değer kolektör, büyük değer emiter. Ayrıntı: [Transistör](../senaryo-2/01-elektronik-sinav-calismasi.md).

## 6. Transformatör (1 soru)

İki bobin + nüve, yalnız AC. `Vp/Vs = Np/Ns`. Türler: alçaltıcı, yükseltici, oto, yalıtım (E1 = E2), toroidal, yüksek frekans, hat. Ayrıntı: [Transformatör](../senaryo-2/01-elektronik-sinav-calismasi.md).

## 7. Seri devre (1 soru)

Akım aynı, gerilim paylaşılır: `RT = R1 + R2 + …`, `I = V/RT`, `VRn = I × Rn`.
Örnek: 12 V, 100 Ω + 220 Ω + 680 Ω → RT = 1000 Ω, I = 12 mA, gerilimler 1,2 V + 2,64 V + 8,16 V = 12 V ✔. Ampermetre **seri**, voltmetre **paralel**.

## 8. Paralel devre (1 soru)

Gerilim aynı, akım paylaşılır: `1/RT = 1/R1 + 1/R2`, iki dirençte `RT = R1·R2/(R1+R2)`, `I = I1 + I2`.
Örnek: 12 V, 400 Ω ∥ 600 Ω → RT = 240 Ω, I1 = 30 mA, I2 = 20 mA, I = 50 mA ✔. Aynı değerli n direnç: R/n.

## 9. Kendin çöz

1. Kahverengi-yeşil-kırmızı-gümüş direncin değeri ve toleransı? 2. 220 Ω'dan 0,1 A geçerse güç? 3. 681 kodlu kondansatör? 4. 6 V'a 30 Ω + 60 Ω seri: I? 5. 12 V'a 30 Ω ∥ 60 Ω: RT ve I?

**Cevaplar:** 1) 15 × 100 = 1,5 kΩ, ±%10. 2) P = 0,01 × 220 = 2,2 W. 3) 68 × 10 = 680 pF. 4) 6/90 ≈ 66,7 mA. 5) RT = 20 Ω, I = 0,6 A.
