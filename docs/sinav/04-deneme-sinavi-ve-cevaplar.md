# Deneme Sınavı ve Cevap Anahtarı

Gerçek sınav değildir; 2. Senaryo dağılımına göre hazırlandı (Elektronik 8 + Mikrodenetleyici 5 = 13 soru). Önce cevaplara bakmadan çöz.

## Elektronik Uygulamaları

1. Üzerinde **104** yazan kondansatörün değeri nedir? A) 10 nF B) 100 nF C) 104 pF D) 1 µF E) 0,01 nF
2. Bobinin birimi ve harfi? A) F – C B) Ω – R C) H – L D) V – U E) A – I
3. Bir LED 5 V ile 2 V / 15 mA'de çalışacaksa seri direnç yaklaşık kaç Ω'dur? A) 100 B) 200 C) 300 D) 500 E) 1000
4. Diyot kademesinde bir transistörde kırmızı prob 2'de sabit, siyah 1'de 512, siyah 3'te 520 okunuyor. Tip ve uçlar?
5. Primeri 220 V, sekonderi 22 V olan bir transformatörün türü?  A) Yükseltici B) Alçaltıcı C) Yalıtım D) Toroid E) Oto
6. 6 V'a bağlı 100 Ω ve 200 Ω seri devrede akım kaç mA? A) 10 B) 20 C) 30 D) 60 E) 300
7. 12 V'a paralel bağlı 60 Ω ve 40 Ω dirençlerin toplam akımı? A) 0,3 B) 0,5 C) 0,6 D) 0,25 E) 5
8. 12 V kaynak, R1 = 100 Ω seri, R2 = R3 = 200 Ω paralel: R1 üzerindeki gerilim?

## Mikrodenetleyici

9. 1101 + 0111 = ? (ikilik)
10. 2F₁₆ sayısının onluk karşılığı?
11. 100101₂ sayısını onaltılığa çevir.
12. Q = A·B' + A'·B ifadesi hangi kapıya eşdeğerdir ve gerçeklemek için hangi entegreler gerekir?
13. 7408 entegresinin Vcc ve GND pinleri kaçıncı bacaklardır?

---

## Cevap anahtarı

| # | Cevap | Çözüm |
|---|-------|-------|
| 1 | **B** | 10 × 10⁴ pF = 100 000 pF = 100 nF |
| 2 | **C** | Henri (H), sembol L |
| 3 | **B** | (5−2)/0,015 = 200 Ω |
| 4 | **NPN**: beyz 2, kolektör 1 (512 küçük), emiter 3 (520 büyük) | Kırmızı ortak uçta iletim → NPN; küçük değer kolektör |
| 5 | **B** | Vs < Vp → alçaltıcı |
| 6 | **B** | RT = 300 Ω; I = 6/300 = 20 mA |
| 7 | **B** | RT = 60×40/100 = 24 Ω; I = 12/24 = 0,5 A |
| 8 | **6 V** | Paralel 100 Ω → RT = 200 Ω; I = 60 mA; V = 0,06 × 100 = 6 V |
| 9 | **10100** | 13 + 7 = 20 = 10100₂ |
| 10 | **47** | 2×16 + 15 = 47 |
| 11 | **25₁₆** | 0010 0101 → 2 5 |
| 12 | **XOR**; 7404 (NOT) + 7408 (AND) + 7432 (OR) | Girişler farklıysa 1 |
| 13 | **Vcc = 14, GND = 7** | Standart 14 bacaklı TTL |

**Değerlendirme:** 12–13 doğru: sınava hazır · 9–11: lojik ve dönüşümlere tekrar · 8 ve altı: gün planını baştan uygula.
