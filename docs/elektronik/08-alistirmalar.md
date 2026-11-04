# Elektronik Alıştırmaları — Çözümleriyle

Önce yalnız sorular bölümünü çöz. Her soruda `verilenler → bağlantı türü → formül → işlem → birim → kontrol` adımlarını yaz.

## Sorular

1. `0,025 A` kaç mA?
2. 12 V kaynağa 2 Ω ve 4 Ω seri bağlanmış. Toplam direnç, akım ve her dirençteki gerilim nedir?
3. 12 V kaynağa 6 Ω ve 3 Ω paralel bağlanmış. Eşdeğer direnç, kol akımları ve toplam akım nedir?
4. 12 V kaynağa 2 Ω seri; ardından 6 Ω ile 3 Ω paralel. Toplam akım ve kol akımları nedir?
5. PDF 68, Soru 11: 100 Ω, 300 Ω, 600 Ω seri. Eşdeğer direnç?
6. PDF 68, Soru 12: 3 kΩ ile 6 kΩ paralel. Eşdeğer direnç?
7. PDF 69, Soru 13: 3 kΩ seri, ardından 6 kΩ ile 3 kΩ paralel. Toplam direnç?
8. PDF 69, Soru 14: 15 V, 3 Ω seri, ardından 6 Ω ile 3 Ω paralel; ampermetre ana hatta. Kaç A?
9. PDF 69, Soru 15: 15 V, 3 Ω seri, ardından 6 Ω ile 3 Ω paralel; voltmetre paralel kolda. Kaç V?
10. Bakır tel: `ρ=0,0178 Ω·mm²/m`, `L=10 m`, `A=1,5 mm²`. Tel direnci?
11. 12 V'ta 50 W çeken yükün akımı kaç A?
12. 4 kHz'lik sinyalin periyodu kaç ms? (Ek konu)

## Cevap anahtarı ve işlem basamakları

### 1. Amper → miliamper

`1 A=1.000 mA`; `0,025×1.000=25 mA`.

### 2. Seri devre

`R_T=2+4=6 Ω`; `I_T=12/6=2 A`.<br>
Seride akım aynı: `I1=I2=2 A`.<br>
`V1=2×2=4 V`; `V2=2×4=8 V`.<br>
Kontrol: `4+8=12 V`.

### 3. Paralel devre

`R_T=(6×3)/(6+3)=2 Ω`.<br>
`I_6Ω=12/6=2 A`; `I_3Ω=12/3=4 A`.<br>
`I_T=2+4=6 A`; kontrol `12/2=6 A`.

### 4. Karışık devre

Paralel eşdeğer `R_P=(6×3)/(6+3)=2 Ω`.<br>
Seri toplam `R_T=2+2=4 Ω`; toplam akım `I_T=12/4=3 A`.<br>
Seri 2 Ω üzerindeki gerilim `3×2=6 V`; paralel kolda da `12−6=6 V`.<br>
Kol akımları: `6/6=1 A`; `6/3=2 A`. Kontrol `1+2=3 A`.

### 5. Seri eşdeğer

`R_T=100+300+600=1.000 Ω`.

### 6. Paralel eşdeğer

`R_T=(3×6)/(3+6) kΩ=2 kΩ`. Paralel eşdeğer `3 kΩ`'dan küçüktür; sonuç makul.

### 7. Seri ve paralel

`6||3=(6×3)/(6+3)=2 kΩ`; `R_T=3+2=5 kΩ`.

### 8. Ampermetre

Paralel kol `6||3=2 Ω`; toplam `R_T=3+2=5 Ω`.<br>
Ana hatta seri bağlı ampermetre toplamı ölçer: `I_T=15/5=3 A`.

### 9. Voltmetre

Aynı eşdeğer direnç `5 Ω`; toplam akım `15/5=3 A`.<br>
Seri 3 Ω üzerindeki gerilim `3×3=9 V`; paralel kola kalan `15−9=6 V`.<br>
Voltmeter kol uçlarına paralel bağlı olduğundan `6 V` okur.

### 10. Bakır tel

`R=ρL/A=0,0178×10/1,5≈0,119 Ω`. İki telli gidiş-dönüş kablosunda tel uzunluğu yaklaşık 20 m ise yaklaşık `0,237 Ω`.

### 11. Güçten akım

`P=V×I`, akımı yalnız bırak: `I=P/V=50/12≈4,17 A`.

### 12. Frekans ve periyot

`4 kHz=4.000 Hz`; `T=1/f=1/4.000 s=0,00025 s=0,25 ms=250 µs`.

## Kendini kontrol et

- Her paralel grupta gerilimleri eşit buldun mu?
- Her seri yolun akımını aynı tuttun mu?
- Paralel kol akımlarını topladığında kaynak akımını buluyor musun?
- Seri gerilim düşümleri kaynağa eşit mi?
- Sorunun istediği birimle cevap verdin mi?
