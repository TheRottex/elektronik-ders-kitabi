# Elektronik Uygulamaları — Sınav Çalışması

Kaynak: Elektronik Uygulamaları PDF s.26–69. "Ek" etiketli formüller kitapta açık yazmayabilir; standart bilgidir.

## 1. Kondansatör (1 soru)

**Ne işe yarar?** Elektrik yükü depolar. Birimi **farad (F)**; pratikte µF, nF, pF kullanılır.

| Dönüşüm | Değer |
|---------|-------|
| 1 µF | 1000 nF |
| 1 nF | 1000 pF |
| 1 µF | 1 000 000 pF |

**Üç haneli kod okuma:** ilk iki rakam değer, üçüncü rakam sıfır sayısıdır; sonuç **pikofarad (pF)** olur.

| Kod | Hesap | Sonuç |
|-----|-------|-------|
| 104 | 10 × 10⁴ pF = 100 000 pF | 100 nF = 0,1 µF |
| 105 | 10 × 10⁵ pF = 1 000 000 pF | **1 µF** |
| 103 | 10 × 10³ pF | 10 nF |
| 102 | 10 × 10² pF | 1 nF (1000 pF) |
| 473 | 47 × 10³ pF | 47 nF |
| 331 | 33 × 10¹ pF | 330 pF |

**Kutuplu mu?** Elektrolitik kondansatörlerin eksi (−) bacağı işaretlidir; ters bağlanırsa zarar görür. Üzerinde yazan **çalışma gerilimi** devre geriliminden büyük olmalıdır. Seramik, mika, film kondansatörler kutupsuzdur. Mika kondansatörde yalıtkan (dielektrik) **mika**dır.

**Örnek (kitaptaki 13. soru):** Üzerinde 105 yazan kondansatör → **1 µF**.

## 2. Bobin (1 soru)

- Birimi **henri (H)**, pratikte mH ve µH. Sarılmış telden oluşur.
- **DC'de** (yalnızca bobinin direnci kadar) akıma neredeyse kısa devre gibi davranır; **AC'de** frekans arttıkça akıma karşı koyar.
- Ek formül: bobinin AC direnci `XL = 2·π·f·L` (Ω). Örnek: f = 50 Hz, L = 0,5 H → XL = 2 × 3,14 × 50 × 0,5 ≈ **157 Ω**.
- Çekirdeğe göre çeşitler: hava çekirdekli, ferit çekirdekli, demir çekirdekli, toroid, SMD.
- Kullanım: filtre, röle, trafo, motor sargısı, osilatör.
- LCR metre ile bobin (L), kondansatör (C), direnç (R) ölçülür. **Avometre (multimetre) bu iş için değil**, akım–gerilim–direnç içindir (kitap D/Y sorusu 2: yanlış).

## 3. Diyot (1 soru)

**Yapı:** P ve N tipi maddenin birleşimi, **iki bacaklı**: anot (A, +) ve katot (K, −, çizgili uç). Akımı yalnızca anottan katoda geçirir.

| Tür | Akılda kalacak özellik |
|-----|-----------------------|
| Kristal (doğrultucu) | AC'yi DC'ye çevirir |
| Zener | Ters yönde belli gerilimde iletir, gerilim sabitler |
| Şotki (Schottky) | Hızlı, düşük gerilim düşümlü; sembolde çubuk "S" biçiminde |
| LED | Doğru kutuplanınca ışık verir; IR LED görünmez **kızılötesi** ışık yayar |
| Varikap | Ters gerilime göre kapasitesi değişir |
| Köprü diyot | 4 diyot tek kılıfta; AC giriş uçları ~ ~, DC çıkış + − |

**LED seri direnci:** `Rs = (Vcc − Vd) / Id`. Örnek: Vcc = 5 V, LED gerilimi Vd = 2 V, Id = 15 mA → Rs = 3 V / 0,015 A = **200 Ω** → bir üst standart değer **220 Ω** seçilir.

**Sağlamlık testi (dijital multimetre, diyot kademesi):** kırmızı prob anotta, siyah prob katotta iken bir değer (yaklaşık 500–800) görünür; ters bağlanınca **"1" / OL** görünür. İki yönde de değer → diyot kısa devre; iki yönde de "1" → açık devre (arızalı).

## 4. Transistör (1 soru)

- Üç bacak: **kolektör (C), beyz (B), emiter (E)**. İki ana tür BJT ve FET. BJT'de **NPN** ve **PNP** vardır.
- NPN: iki N arasında ince P (beyz). PNP: iki P arasında ince N (beyz).
- Beyz-emiter **doğru**, beyz-kolektör **ters** kutuplanırsa iletime geçer.
  - NPN: beyz ve kolektör **+**, emiter **−**.
  - PNP: beyz ve kolektör **−**, emiter **+**.
- **Anahtar olarak:** *doyum* → C–E arası gerilim ≈ 0 V, akım maksimum (anahtar kapalı); *kesim* → B–E gerilimi 0 V, kolektör akımı 0 (anahtar açık).
- **Sağlamlık ve uç bulma (diyot kademesi):** Altı ölçümde yalnız ikisinde değer okunur. Kırmızı prob **ortak uçtaysa** ve değer veriyorsa ortak uç beyz ve tip **NPN**'dir (siyah prob ortaksa PNP). Küçük değer → **kolektör**, büyük değer → **emiter**.
  - Kitaptaki örnek: kırmızı 2 – siyah 3 = 513, kırmızı 2 – siyah 1 = 510 → 2 = beyz, NPN; 1 (510, küçük) = kolektör, 3 (513, büyük) = emiter.

## 5. Transformatör (1 soru)

- Yapı: **iki bobin (primer, sekonder) ve nüve**. Primere AC verilince nüvede değişen manyetik akı oluşur, sekonderde gerilim indüklenir. Yalnızca **AC'de** çalışır.
- Ek formül: `Vp / Vs = Np / Ns`. Örnek: 220 V → 12 V, Np = 1100 sarım → Ns = 1100 × 12 / 220 = **60 sarım**.

| Tür | Özellik |
|-----|---------|
| Alçaltıcı | Vs < Vp; adaptörlerde en yaygın |
| Yükseltici | Vs > Vp; eski tüplü TV |
| Oto trafosu | Tek sargı hem primer hem sekonder; küçük, verimli |
| Yalıtım (izolasyon) | Gerilimi değiştirmez (E1 = E2), devreleri ayırır |
| Toroidal | Halka nüve, yüksek verim, düşük frekans |
| Yüksek frekans | 10 kHz üzeri, anahtarlamalı güç kaynakları |
| Hat trafosu | Ses sistemlerinde, hoparlör gücüne göre seçilir |

## 6. Seri devre (1 soru)

Kurallar: **akım aynı**, gerilimler paylaşılır, dirençler toplanır.

`RT = R1 + R2 + R3` · `I = V / RT` · `VRn = I × Rn` · `V = VR1 + VR2 + …`

**Örnek:** V = 12 V, R1 = 100 Ω, R2 = 220 Ω, R3 = 680 Ω
1. RT = 100 + 220 + 680 = 1000 Ω
2. I = 12 / 1000 = 0,012 A = **12 mA**
3. VR1 = 1,2 V, VR2 = 2,64 V, VR3 = 8,16 V
4. Kontrol: 1,2 + 2,64 + 8,16 = 12 V ✔

Ölçü aleti: **ampermetre seri**, voltmetre **paralel** bağlanır.

## 7. Paralel devre (1 soru)

Kurallar: **gerilim aynı**, akımlar paylaşılır, toplam direnç **küçülür** (en küçük dirençten de küçük).

`1/RT = 1/R1 + 1/R2` · iki direnç için `RT = (R1 × R2)/(R1 + R2)` · `In = V / Rn` · `I = I1 + I2`

**Örnek:** V = 12 V, R1 = 400 Ω, R2 = 600 Ω
1. RT = 400 × 600 / 1000 = **240 Ω**
2. I1 = 12/400 = 30 mA, I2 = 12/600 = 20 mA
3. I = 50 mA; kontrol: 12 / 240 = 50 mA ✔

Aynı değerli n direnç: RT = R / n.

## 8. Seri-paralel (karışık) devre (1 soru)

**Yöntem:** önce paralel grubu tek dirence indir → devre seri olur → akımı bul → geri dön.

**Örnek:** V = 12 V; R1 = 200 Ω seri, ardından R2 = 300 Ω ∥ R3 = 600 Ω
1. R23 = 300 × 600 / 900 = 200 Ω
2. RT = 200 + 200 = 400 Ω
3. I = 12 / 400 = 30 mA (R1'den geçen)
4. VR1 = 0,03 × 200 = 6 V; paralel grupta kalan **6 V**
5. I2 = 6/300 = 20 mA, I3 = 6/600 = 10 mA; toplam 30 mA ✔

Çapraz bağlı görünen devreleri sadeleştirme için bkz. [Köprü ve yıldız-üçgen](../elektronik/05-kopru-yildiz-ucgen.md). Devre çizimi: seri/paralel şemalar için [Seri-paralel bölümü](../elektronik/04-seri-paralel-karisik.md).

## 9. Kendin çöz

1. 473 kodlu kondansatör kaç nF'tır? 2. Vcc = 9 V, LED 2 V, 20 mA: Rs = ? 3. 5 V'a 100 Ω ve 400 Ω seri bağlı: I ve VR2 ? 4. 90 Ω ∥ 90 Ω ∥ 90 Ω = ? 5. 12 V, R1 = 100 Ω seri, (200 Ω ∥ 200 Ω): I = ?

**Cevaplar:** 1) 47 nF. 2) 7/0,02 = 350 Ω (360 Ω veya 390 Ω seçilir). 3) RT = 500, I = 10 mA, VR2 = 4 V. 4) 30 Ω. 5) Paralel 100 Ω, RT = 200 Ω, I = 60 mA.
