# Görsel Destekli Elektronik ve Mikrodenetleyici Ders Kitabı

> Bu dosya `tools/build_book.py` ile bölüm Markdown dosyalarından üretilir. Bölümleri düzenledikten sonra aynı komutu yeniden çalıştırın.

## İçindekiler

- [Elektronik Uygulamaları: Elektronik Uygulamaları — Ders Haritası](#chapter-01)
- [Elektronik Uygulamaları: Elektriksel Büyüklükler ve Birimler](#chapter-02)
- [Elektronik Uygulamaları: Devre Elemanları: Ne İşe Yarar, Nasıl Tanınır?](#chapter-03)
- [Elektronik Uygulamaları: Ohm Kanunu ve Güç — Hangi Formül, Hangi İşlem?](#chapter-04)
- [Elektronik Uygulamaları: Seri, Paralel ve Karışık Devreler](#chapter-05)
- [Elektronik Uygulamaları: Çapraz Çizilmiş Devre, Wheatstone Köprüsü ve Yıldız-Üçgen](#chapter-06)
- [Elektronik Uygulamaları: Ölçü Aletleri: Nereye Bağlanır, Nasıl Kullanılır?](#chapter-07)
- [Elektronik Uygulamaları: Frekans, Periyot ve Hz–kHz–MHz](#chapter-08)
- [Elektronik Uygulamaları: Elektronik Alıştırmaları — Çözümleriyle](#chapter-09)
- [Mikrodenetleyici: Mikrodenetleyici — Sayı Sistemleri ve Mantık Kapıları](#chapter-10)
- [Mikrodenetleyici: İkili Sayı Sistemi, Sayma ve Taban Dönüşümleri](#chapter-11)
- [Mikrodenetleyici: Doğruluk Tablosu, VE ve VEYA Kapıları](#chapter-12)
- [Mikrodenetleyici: NOT, NAND, NOR, XOR ve XNOR Kapıları](#chapter-13)
- [Mikrodenetleyici: Mikrodenetleyici, HIGH/LOW, Buton ve LED](#chapter-14)
- [Mikrodenetleyici: Sayı Sistemleri ve Lojik Kapılar — Alıştırmalar](#chapter-15)


---

<a id="chapter-01"></a>

# Elektronik Uygulamaları — Ders Haritası

**Kaynak:** *Elektronik Uygulamaları*, PDF 1–72; içerik PDF 18'de başlar.

## Bu bölümde neler var?

| PDF sayfası | Konu | Rehber |
|---:|---|---|
| 18–25 | Direnç, öz direnç, çeşitler, renk kodu | [Devre elemanları](docs/elektronik/02-devre-elemanlari.md) |
| 26–33 | Kondansatör, kapasite, kod okuma | [Devre elemanları](docs/elektronik/02-devre-elemanlari.md) |
| 34–36 | Bobin, indüktans, AC/DC davranışı | [Devre elemanları](docs/elektronik/02-devre-elemanlari.md) |
| 37–43 | Diyot çeşitleri ve ölçümü | [Devre elemanları](docs/elektronik/02-devre-elemanlari.md), [ölçüm](docs/elektronik/06-olcum-ve-guvenlik.md) |
| 44–49 | NPN/PNP transistor, anahtar kullanımı | [Devre elemanları](docs/elektronik/02-devre-elemanlari.md) |
| 50–52 | Transformatör | [Devre elemanları](docs/elektronik/02-devre-elemanlari.md) |
| 54–60 | Seri devre | [Seri-paralel devreler](docs/elektronik/04-seri-paralel-karisik.md) |
| 60–64 | Paralel devre | [Seri-paralel devreler](docs/elektronik/04-seri-paralel-karisik.md) |
| 64–67 | Karışık devre ve ölçüm | [Seri-paralel devreler](docs/elektronik/04-seri-paralel-karisik.md) |
| 68–69 | Devre değerlendirme soruları 11–15 | [Çözümlü cevaplar](docs/elektronik/08-alistirmalar.md) |
| 70–72 | Doğru akıma giriş, kaynak türleri | [Büyüklükler](docs/elektronik/01-buyuklukler-birimler.md), [ölçüm](docs/elektronik/06-olcum-ve-guvenlik.md) |

## Önerilen öğrenme yolu

1. Önce [gerilim, akım, direnç ve birimleri](docs/elektronik/01-buyuklukler-birimler.md) öğren.
2. [Ohm Kanunu](docs/elektronik/03-ohm-kanunu-ve-guc.md) formül üçlüsünün ne bulduğunu anla.
3. Devre elemanlarının isim, sembol ve görevlerini [buradan](docs/elektronik/02-devre-elemanlari.md) çalış.
4. Devre topolojisini tanı ve [seri-paralel soruları](docs/elektronik/04-seri-paralel-karisik.md) çöz.
5. Hangi büyüklüğün sorulduğunu, aletin devreye nasıl bağlandığını [ölçüm bölümünden](docs/elektronik/06-olcum-ve-guvenlik.md) öğren.
6. Sonra [alıştırmaları](docs/elektronik/08-alistirmalar.md) çözüp cevap anahtarıyla kontrol et.
7. Çapraz köprü soruları gelirse [ek köprü bölümüne](docs/elektronik/05-kopru-yildiz-ucgen.md) geç.

## Soruya başlamadan önce kendine sor

- Benden **eşdeğer direnç**, **toplam akım**, **kol akımı**, **gerilim** veya **güç** mü isteniyor?
- Kaynağın gerilimi ve dirençlerin birimleri birbiriyle uyumlu mu?
- Bu elemanlar gerçekten seri/paralel mi, yoksa yalnızca öyle çizilmiş gibi mi duruyor?
- Sonucu amper mi, miliamper mi; ohm mu, kiloohm mu yazmalıyım?

> **Ek konular:** Frekans/periyot, güç verimi ve köprü dönüşümleri ilk 72 sayfanın kapsamını aşan tamamlayıcı açıklamalardır; ilgili sayfalarda ayrıca işaretlenmiştir.


---

<a id="chapter-02"></a>

# Elektriksel Büyüklükler ve Birimler

**Kaynak:** *Elektronik Uygulamaları* PDF 18–19, 26–27, 34–35, 70–72. **Frekans/periyot** eki kitapta bu sayfa aralığının dışındadır.

## 1. Dört temel büyüklük

| Büyüklük | Harf | Birim | Basit anlatım | Örnek |
|---|---|---|---|---|
| Gerilim | `V` | volt (V) | Yükleri devrede hareket ettiren elektriksel fark | 9 V pil |
| Akım | `I` | amper (A) | İletkenden geçen elektrik yükü akış hızı | 0,02 A |
| Direnç | `R` | ohm (Ω) | Akım akışına karşı koyma | 470 Ω |
| Güç | `P` | watt (W) | Elektrik enerjisinin kullanılma/dönüşme hızı | 2 W |

Su benzetmesi yalnızca ilk sezgi içindir: gerilimi basınca, akımı akışa, direnci dar boruya benzetebilirsin. Elektrik devresindeki gerçek davranışı hesaplamak için yine devre yasalarını kullan.

![Ohm Kanunu üçgeni ve birim ölçeği](assets/diagrams/ohm-birimler.svg)

## 2. Ön ekler: k, M, m ve µ

Ön ek, sayının kaç kat büyük veya küçük olduğunu gösterir. **Büyük ve küçük harf önemlidir:** `m` mili, `M` mega demektir.

| Ön ek | Değer | Örnek |
|---|---:|---|
| giga `G` | `10⁹` | `1 GHz = 1.000.000.000 Hz` |
| mega `M` | `10⁶` | `1 MΩ = 1.000.000 Ω` |
| kilo `k` | `10³` | `1 kΩ = 1.000 Ω` |
| temel birim | `1` | `1 A`, `1 Ω`, `1 Hz` |
| mili `m` | `10⁻³` | `1 mA = 0,001 A` |
| mikro `µ` | `10⁻⁶` | `1 µA = 0,000001 A` |
| nano `n` | `10⁻⁹` | `1 nF = 0,000000001 F` |
| piko `p` | `10⁻¹²` | `1 pF = 0,000000000001 F` |

### Sık kullanılan dönüşümler

- Akım: `1 A = 1.000 mA`; `1 mA = 0,001 A`; `1 A = 1.000.000 µA`.
- Direnç: `1 MΩ = 1.000 kΩ = 1.000.000 Ω`; `1 kΩ = 1.000 Ω`.
- Güç: `1 kW = 1.000 W`; `1 W = 1.000 mW`.
- Frekans (ek): `1 kHz = 1.000 Hz`; `1 MHz = 1.000 kHz`; `1 GHz = 1.000 MHz`.
- Kapasite: `1 F = 1.000 mF = 1.000.000 µF`; `1 µF = 1.000 nF = 1.000.000 pF`.
- Zaman (ek): `1 s = 1.000 ms = 1.000.000 µs`.

**Örnek:** `0,025 A` kaç mA?

`1 A = 1.000 mA`, dolayısıyla `0,025 × 1.000 = 25 mA`.

**Örnek:** `4,7 kΩ` kaç Ω?

`1 kΩ = 1.000 Ω`, dolayısıyla `4,7 × 1.000 = 4.700 Ω`.

### Birimleri işlemin içinde sadeleştir

Ohm Kanunu'nda `V / Ω = A`. Örneğin `12 V / 240 Ω = 0,05 A = 50 mA`. Önce sonucu temel birimle bul; en sonda sorunun istediği birime çevir.

## 3. Frekans ve periyot — ek konu

- Frekans `f`, bir saniyedeki tekrar sayısıdır; birimi hertz (Hz).
- Periyot `T`, bir tam tekrarın sürdüğü zamandır; birimi saniye (s).
- Birbirlerinin tersidir: `f = 1/T`, `T = 1/f`.

Örnek: Sinyal saniyede 1.000 kez tekrarlanıyorsa `f=1.000 Hz=1 kHz`; `T=1/1.000 s=0,001 s=1 ms`.

**Karıştırma:** `mA` bir akım; `MHz` bir frekans; `ms` bir zamandır. Her biri farklı fiziksel büyüklük olduğundan birbirine dönüştürülemez.

## Alıştırma

1. `0,003 A` kaç mA?
2. `2,2 kΩ` kaç Ω?
3. `470 nF` kaç µF?
4. Frekansı `50 Hz` olan bir sinyalin periyodu kaç ms? (Ek konu)

**Cevap:** 1) `3 mA`. 2) `2.200 Ω`. 3) `0,47 µF`. 4) `T=1/50 s=0,02 s=20 ms`.


---

<a id="chapter-03"></a>

# Devre Elemanları: Ne İşe Yarar, Nasıl Tanınır?

**Kaynak:** *Elektronik Uygulamaları* PDF 18–52. Çizimler kavramları anlatan özgün sembollerdir; kaynak kitap görsellerinin kopyası değildir.

![Direnç, kondansatör, bobin, diyot ve transistör için temel şematik semboller](assets/diagrams/eleman-sembolleri.svg)

## 1. Direnç ve bakır iletken

Direnç (`R`), akımı sınırlar/belirli bir değere ayarlar. Birimi ohm (Ω). Sabit direnç, potansiyometre, trimpot, reosta ve ışık/sıcaklıkla değişen direnç türleri bulunur.

- **Potansiyometre:** Döner kol ile ayarlanan, çoğunlukla üç uçlu değişken direnç.
- **Trimpot:** Devre kalibrasyonu için tornavidayla ayarlanır.
- **Reosta:** Daha yüksek güçlerde değişken direnç olarak tasarlanır.
- **LDR:** Işık arttıkça direnci genellikle azalır.
- **NTC:** Sıcaklık arttıkça direnci azalır.
- **PTC:** Sıcaklık arttıkça direnci artar.
- **Renk kodu:** 4 bantlı dirençte ilk iki bant rakam, üçüncü çarpan, son bant toleranstır. Örnek: sarı-mor-turuncu-altın → `47 × 1.000 Ω = 47 kΩ ±%5`.

Tel için direnç yaklaşık `R = ρL/A` ile bulunur. Bakır için kitapta verilen yaklaşık öz direnç `ρ=0,0178 Ω·mm²/m`; `L` metre, `A` mm² olmalı. Tel uzadıkça direnç artar, kesiti büyüdükçe azalır.

**Örnek:** 10 m uzunluk ve 1,5 mm² kesit: `R=0,0178×10/1,5≈0,119 Ω`. İki telli gidiş-dönüş bağlantıda toplam tel uzunluğu yaklaşık 20 m olur; direnç yaklaşık `0,237 Ω` çıkar.

> Bu bağıntı ile bir bağlantı telinin direnci hesaplanır. Kontrollü akım sınırlamak için değeri ve güç kapasitesi uygun bir direnç seçilir. İnce teli bilerek ısıtmak güvenli bir güç dönüştürme yöntemi değildir.

## 2. Kondansatör

Kondansatör (`C`), elektrik yükünü/enerjisini elektrik alanında depolar; kapasitesi farad (F). Plakaların alanı ve yalıtkanın dielektrik katsayısı arttıkça kapasite artar; plakalar arası mesafe arttıkça azalır.

- Elektrolitik kondansatör çoğunlukla kutupludur. `+`/`−` uçlarını ters bağlama ve üstündeki gerilim sınırını aşma.
- Seramik/film kondansatörler genellikle kutupsuzdur.
- Kod `104`: ilk iki anlamlı rakam `10`, son rakam pF cinsinden sıfır sayısı `4` → `100.000 pF = 100 nF = 0,1 µF`.
- LCR metre, L (indüktans), C (kapasite), R (direnç) ölçmek için kullanılabilir.

## 3. Bobin

Bobin (`L`), sarılmış iletkendir; birimi henry (H). Akım değişimine karşı koyan manyetik alan oluşturur. DC kararlı hâle geldiğinde esas olarak tel direnci, AC'de ise frekansa ve indüktansa bağlı endüktif reaktans etkilidir. Güç kaynaklarında filtreleme, sinyal ve frekans devrelerinde kullanılır.

## 4. Diyot, LED ve zener

- **Diyot:** Anot (A) ve katot (K) uçludur; ileri yönde iletir, ters yönde büyük ölçüde engeller. Fiziksel diyotta çizgili uç genellikle katodu gösterir.
- **LED:** Işık yayan diyottur; doğru kutuplanır ve akımı sınırlamak için uygun seri dirençle kullanılır.
- **Zener:** Uygun ters kutuplamada ve anma değerleri içinde gerilimi sınırlama/sabitleme için kullanılır.
- **Köprü diyot:** Dört diyotla alternatif akımı doğrultmaya yarar.
- **Diyot testi:** Enerjisi kesilmiş devrede multimetre diyot moduna alınır. Bir yönde ileri gerilim düşümü, ters yönde açık devre okunması genellikle sağlamlık işaretidir.

## 5. BJT transistör

Uçları kolektör (C), beyz (B), emiter (E). Beyz-emiter girişindeki küçük akım, kolektör-emiter yolundaki daha büyük akımı kontrol edebilir; bu yüzden anahtar veya yükselteç olarak kullanılır.

- **NPN:** Bazı kaynak şemalarında emiter oku dışarı doğrudur; doğru çalışma kutuplaması PNP'nin tersidir.
- **PNP:** NPN'ye göre kutuplama yönü tersidir.
- Anahtar: beyz sürülmüyorsa kesim/kapalı; yeterli baz sürmesiyle doyum/açık.
- Bacak dizilimi modelden modele değişir; parça veri sayfasına bak. Kılıf şekline göre tahmin etme.

## 6. Transformatör

İki sargı ve manyetik nüve üzerinden **değişen akımla/AC ile** enerji aktarır. Alçaltıcı tip gerilimi düşürür; yükseltici artırır; izolasyon tipi iki devreyi elektriksel olarak ayırır. Gerilim dönüşümü akım ve güç ilişkisiyle birlikte düşünülmelidir; gerçek elemanda kayıp bulunur. Transformatör tek başına “500 W'ı 50 W'a ayarlamaz”.

## Kendini dene

1. Işık arttıkça direnci azalan eleman hangisi?
2. Sıcaklık artınca direnci artan ve azalan termistörlerin adları ne?
3. `104` kondansatör kodunun değeri?
4. Diyotun katot ucunu tanımaya yarayan yaygın gövde işareti nedir?

**Cevap:** 1) LDR. 2) PTC artar, NTC azalır. 3) `100 nF = 0,1 µF`. 4) Katot tarafındaki bant/çizgi (parça tipini yine veri sayfasıyla doğrula).


---

<a id="chapter-04"></a>

# Ohm Kanunu ve Güç — Hangi Formül, Hangi İşlem?

**Kaynak:** Elektriksel büyüklükler ve devre ilkeleri, *Elektronik Uygulamaları* PDF 18–19 ve 54–65. Güç uygulamalarına dair ek örnekler bu notta ayrıca işaretlidir.

![Ohm Kanunu üçgeni](assets/diagrams/ohm-birimler.svg)

## 1. V, I, R üçlüsü

```text
      V
    -----
     I × R
```

| Sorulan | Formül | Bulduğun |
|---|---|---|
| Gerilim? | `V = I × R` | volt (V) |
| Akım? | `I = V / R` | amper (A) |
| Direnç? | `R = V / I` | ohm (Ω) |

`V` gerilim, `I` akım, `R` dirençtir. Yani verilen iki büyüklüğü formüle koyup üçüncüyü bulursun.

**Örnek:** 12 V kaynağa 4 Ω yük bağlanmış. Akım isteniyor:

1. Bilinenler: `V=12 V`, `R=4 Ω`.
2. İstenen `I`; formülde yalnız bırak: `I=V/R`.
3. Yerine koy: `I=12/4=3 A`.
4. Birim kontrolü: `V/Ω=A`.

`I=V/R`, **bu dirençten** geçen akımı verir. Toplam kaynak akımı soruluyorsa `R` yerine devrenin eşdeğeri `R_T` kullanılır. Bir kol soruluyorsa o kola düşen gerilimi ve kol direncini kullan.

## 2. Güç ne demek?

Güç `P`, elektrik enerjisinin kullanım/dönüşüm hızıdır; birimi watt (W). Dirençli yükler için:

- `P = V × I`
- `P = I² × R`
- `P = V² / R`

`I²`, akımın karesi; `V²`, gerilimin karesi demektir. Üç ifade Ohm Kanunu kullanılarak birbirinden elde edilir. Elindeki verilere uyanı seç; birim kontrolü yap (`V×A=W`).

**Örnek:** 12 V'ta 4 A çeken yük: `P=12×4=48 W`.

## 3. 500 W / 50 W sorusunu doğru ayır

“500 W'lık kaynaktan 50 W almak” iki ayrı durumu anlatabilir:

**Kaynak en çok 500 W sağlayabiliyor, yük 50 W istiyor:** Bu normaldir. Uygun gerilimde yük ihtiyacı kadar akım çeker. Örneğin 12 V, 50 W yük `I=P/V=50/12≈4,17 A` çeker. Kaynağın 500 W kapasitesi yükü 500 W'a zorlamaz.

**Gerçek giriş 500 W, yararlı çıkış 50 W ise:** Verim `η=P_out/P_in×100%=10%`; yaklaşık `450 W` kayıp çoğunlukla ısıya dönüşür. Bu normal/verimli bir düşürme yöntemi değildir.

“500 V'tan 50 V'a” denmek isteniyorsa bu watt değil **gerilim** değeridir. Uygun AC transformatörü veya DC-DC dönüştürücü seçmek gerekir; basit seri direnç özellikle yüksek güçte güvenli çözüm değildir.

## İşlem kontrol listesi

1. Soru benden hangi büyüklüğü istiyor?
2. Devrede o büyüklüğü belirleyen doğru direnç/gerilim hangisi?
3. Birimleri temel birimde mi?
4. Formülün sonucu istenen fiziksel büyüklük mü?
5. Akım amper çıktıysa ve soru mA istiyorsa `×1.000` yaptım mı?
6. Watt hesabında hem gerilim hem akımı hesaba kattım mı?

## Alıştırma

1. 9 V kaynağa 3 kΩ bağlanıyor. Akım kaç mA?
2. 6 V gerilimle 0,2 A akım alan yükün gücü kaç W?
3. 2 W ve 100 Ω dirençte akım `I=√(P/R)` ile kaç A? (Ek formül uygulaması)

**Cevap:** 1) `9/3.000=0,003 A=3 mA`. 2) `6×0,2=1,2 W`. 3) `√(2/100)=√0,02≈0,141 A`.


---

<a id="chapter-05"></a>

# Seri, Paralel ve Karışık Devreler

**Kaynak:** *Elektronik Uygulamaları* PDF 54–69. Devre şekilleri öğretim için yeniden çizilmiştir; karşılık gelen kaynak PDF sayfaları aşağıda yazılıdır.

![Seri ve paralel devrede akım ve gerilim](assets/diagrams/seri-paralel.svg)

## 1. Seri bağlantı

Elemanlar uç uca ve tek akım yolu üzerindedir. Arada başka kol yoktur.

- Aynı akım her elemandan geçer: `I_T = I_1 = I_2`.
- Eşdeğer dirençler toplanır: `R_T = R_1 + R_2 + ...`.
- Kaynak gerilimi dirençlere bölünür: `V_T = V_1 + V_2 + ...`.
- Her dirençte `V_n = I × R_n`.

**Örnek:** 12 V kaynağa 2 Ω ve 4 Ω seri.

1. `R_T=2+4=6 Ω`.
2. `I_T=12/6=2 A`. Bu akım iki dirençten de 2 A geçer.
3. `V_1=2×2=4 V`; `V_2=2×4=8 V`.
4. Kontrol: `4+8=12 V`.

### Kaynak kitap seri örneği

PDF 59–60'da seri bağlantıda devre akımının her elemanda aynı olduğu ve voltmetrenin eleman uçlarına paralel bağlandığı anlatılır. PDF 68'de üç seri direnç sorusunun çözümü [alıştırmalar sayfasındadır](docs/elektronik/08-alistirmalar.md).

## 2. Paralel bağlantı

Her direnç aynı iki düğüm arasına bağlanır. Kollar ayrı akım yolu oluşturur.

- Kolların uçları aynı düğümlerde olduğundan gerilim aynı: `V_1=V_2=V`.
- Akım kollara bölünür: `I_T=I_1+I_2+...`.
- `I_n=V/R_n`; direnci küçük kola daha fazla akım gider.
- İki direnç için `R_T=(R_1×R_2)/(R_1+R_2)`.
- Genel formül: `1/R_T=1/R_1+1/R_2+...`.
- Eşdeğer direnç en küçük paralel dirençten küçüktür.

**Örnek:** 12 V'ta 6 Ω ve 3 Ω paralel.

1. `R_T=(6×3)/(6+3)=2 Ω`.
2. `I_1=12/6=2 A`; `I_2=12/3=4 A`.
3. `I_T=2+4=6 A`. Kontrol: `12/2=6 A`.

### Aklında kalsın

**Paralelde aynı olan gerilim; ayrılan ve toplanan akımdır.** Her direncin uçlarının gerçekten aynı iki düğüme bağlı olduğunu izleyerek doğrula.

## 3. Karışık devreyi çözme

![Karışık devrede ilk paralel grubu sadeleştir, sonra seri eşdeğeri çöz](assets/diagrams/karisik-devre.svg)

### Her soruda uygulayacağın 8 adım

1. Kaynağı, dirençleri ve sorulanı yaz.
2. Bağlantı düğümlerini takip et; şeklin görünüşüne aldanma.
3. Önce içteki seri/paralel grubu seç.
4. O grubu eşdeğer dirençle değiştirip yeni, küçük bir devre çiz.
5. Tek bir `R_T` kalana kadar sadeleştir.
6. Toplam kaynak akımını `I_T=V/R_T` ile bul.
7. Orijinal devreye geri dön: seri akımlarını eşitle; paralel gerilimlerini eşitle; her bir elemanı `V=IR` ile hesapla.
8. Kontrol: seri gerilimler kaynak gerilimine, paralel kol akımları ana akıma eşit mi?

> **Yanlış yöntem:** Şemadaki telleri sadece yeniden kıvırıp dirençleri başka düğümlere taşımak bağlantıyı değiştirebilir. Yalnızca iletken üzerinde eleman bulunmayan aynı düğümü sayfa üzerinde farklı biçimde çizebilirsin.

## 4. Tam çözümlü karışık devre (kitap PDF 64–66, Görsel 2.19)

Devre: `R1=R2=R3=R4=20 Ω`, kaynak `12 V`; `R1` seri, `R2` ile `R3` paralel, `R4` tekrar seri.

### A. Toplam akımı bul

1. Paralel grup: `R_23=(20×20)/(20+20)=400/40=10 Ω`.
2. Seri toplam: `R_T=20+10+20=50 Ω`.
3. Kaynak akımı: `I_T=12/50=0,24 A=240 mA`.

### B. Her elemanı bul

4. `R1` ve `R4` seri yolda olduğundan her ikisinden de `240 mA` geçer.
5. Bu dirençlerdeki gerilim: `V_R1=0,24×20=4,8 V`; `V_R4=4,8 V`.
6. Paralel gruba düşen gerilim: `12−4,8−4,8=2,4 V`.
7. Paralel dirençlerin her birinde `2,4 V` bulunur.
8. `I_R2=2,4/20=0,12 A=120 mA`; `I_R3=120 mA`.
9. Kontrol: `120+120=240 mA`; `4,8+2,4+4,8=12 V`.

| Eleman | Akım | Gerilim |
|---|---:|---:|
| R1 | 240 mA | 4,8 V |
| R2 | 120 mA | 2,4 V |
| R3 | 120 mA | 2,4 V |
| R4 | 240 mA | 4,8 V |

## 5. PDF 68–69'daki şekilli soruların kısa yanıtları

| PDF soru | Devre özeti | Çözüm sonucu |
|---:|---|---:|
| 11 | 100 Ω + 300 Ω + 600 Ω seri | `R_T=1.000 Ω` |
| 12 | 3 kΩ paralel 6 kΩ | `R_T=2 kΩ` |
| 13 | 3 kΩ seri (6 kΩ paralel 3 kΩ) | `R_T=5 kΩ` |
| 14 | 15 V, 3 Ω seri (6 Ω paralel 3 Ω), ampermetre ana hatta | `I_T=3 A` |
| 15 | 15 V, 3 Ω seri (6 Ω paralel 3 Ω), voltmetre paralel kolda | `V_ölçülen=6 V` |

Tüm işlem basamakları ve nedenleri [alıştırmalarda](docs/elektronik/08-alistirmalar.md).

## Alıştırma

`R1=4 Ω` seri; `R2=12 Ω` ile `R3=6 Ω` paralel; kaynak `18 V`.

1. Eşdeğer direnç nedir?
2. Kaynak akımı kaç A?
3. Paralel grup gerilimi ve iki kol akımı nedir?

**Cevap:** `R23=4 Ω`; `R_T=8 Ω`; `I_T=18/8=2,25 A`. `R1` gerilimi `9 V`; paralel grupta `9 V`. `I2=0,75 A`, `I3=1,5 A`; kol akımları toplamı `2,25 A`.


---

<a id="chapter-06"></a>

# Çapraz Çizilmiş Devre, Wheatstone Köprüsü ve Yıldız-Üçgen

**Ek konu:** Elektronik Uygulamaları PDF 1–72'de Wheatstone köprüsü/yıldız-üçgen bölümü yoktur. Bu sayfa, öğrencinin bahsettiği çapraz çizilmiş devreler için ek devre analizi anlatımıdır.

![Dengeli Wheatstone köprüsü ve orta koldaki akım](assets/diagrams/kopru-devresi.svg)

## 1. Çapraz çizgi görünce hemen devreyi değiştirme

Bir devre şemasının görünüşünü değiştirmek mümkündür; ancak elektrik bağlantılarını değiştirmek mümkün değildir. Düğüm, aralarında devre elemanı bulunmayan ve iletkenle doğrudan bağlı tüm noktalardır.

- İki tel kesişiyor ama kesişme noktasında birleşme işareti yoksa, çizim kuralına göre bağlantısız olabilir.
- Kesişme noktasında bağlantı noktası (dolu nokta/junction) varsa teller birleşir.
- Bir kablonun geçtiği kavşakta direnç varsa, o direnç iki düğüm arasındaki gerçek bir devre elemanıdır; sırf devreyi seri hale getirmek için silinemez.
- Aynı düğüm üzerindeki uzun telleri farklı biçimde çizmek serbesttir; direnç uçlarının bağlı olduğu düğümleri değiştirmek serbest değildir.

## 2. Köprü biçiminde devre ne zaman sıradan seri-paralel olur?

Önce köprü kolu yok mu diye kontrol et. Sonra:

- İki direncin birleştiği düğümde başka dal yoksa, o iki direnç seri olabilir.
- İki direnç aynı iki düğüme bağlıysa, paraleldir.
- Bu koşullar gerçekleşmiyorsa devre doğrudan seri-paralel değildir.

`R1/R3` sol kolda, `R2/R4` sağ kolda ve `R5` orta köprüde olsun. Kaynağı üst-alt düğümlere bağladığımızda denge koşulu:

`R1/R3 = R2/R4`

Eşdeğer çarpım biçimi: `R1×R4 = R2×R3`.

Denge varsa iki orta düğüm aynı gerilimdedir:

- Orta direnç `R5` üzerinden akım sıfırdır.
- `R5` kolunu hesap dışında bırakabilirsin.
- İki yan kolu seri topla ve birbirine paralel bağla: `R_T=(R1+R3)||(R2+R4)`.

### Denge örneği

`R1=100 Ω`, `R3=200 Ω`, `R2=150 Ω`, `R4=300 Ω`.

`100/200=0,5` ve `150/300=0,5`; köprü dengededir. Orta direnç ne olursa olsun ideal devrede orta kol akımı `0 A`. Sol kol `300 Ω`, sağ kol `450 Ω`:

`R_T=(300×450)/(300+450)=135.000/750=180 Ω`.

## 3. Dengesiz köprü: Yıldız (Y)–Üçgen (Δ) dönüşümü

Denge koşulu yoksa köprü direncini silemezsin. Üç dış düğüm arasındaki Δ bağlantısını aynı uç davranışını veren Y ağıyla değiştirirsen, bazı devreler yeniden seri-paralel hâle gelir.

Δ kenarları `R_AB`, `R_BC`, `R_CA`; dönüşen Y kolları `R_A`, `R_B`, `R_C` olsun. `S=R_AB+R_BC+R_CA`:

```text
R_A = (R_AB × R_CA) / S
R_B = (R_AB × R_BC) / S
R_C = (R_BC × R_CA) / S
```

Her Y kolu: o dış düğüme bağlı iki Δ kenarının çarpımı / üç Δ kenarının toplamı.

**Örnek:** Eşkenar üçgenin her kenarı `3 Ω`. `S=9 Ω`; her Y kolu `3×3/9=1 Ω`. Dönüşümden sonra devreyi yeniden çizip düğüm ve bağlantıları tekrar işaretle.

Y'den Δ'ya dönüşüm gerekirse `Q=R_A R_B + R_B R_C + R_C R_A`:

```text
R_AB = Q / R_C
R_BC = Q / R_A
R_CA = Q / R_B
```

## 4. Yıldız-üçgen dönüşümünü uygulama sırası

1. Dönüşüm yapacağın üç dış düğümü adlandır (`A`, `B`, `C`).
2. Şu an bu düğümler arasında Δ mı, Y mi olduğunu belirle.
3. Üçgen veya yıldız dirençlerini tek tek etiketle; hangi formüldeki kenara ait olduklarını not et.
4. Formülle yeni üç değeri hesapla.
5. Eski üç bağlantıyı çıkarıp yenilerini **aynı üç düğüme** bağla.
6. Yeni devre şeması çiz ve artık seri/paralel grupları bul.
7. Toplam direnci, kaynak akımını ve istenen kol akımlarını/gerilimlerini hesapla.
8. Birim ve fiziksel tutarlılık kontrolü yap.

> Üçgeni yıldıza çevirme, telleri geometrik biçimde bükme değildir; düğümler arası elektriksel eşdeğerliği koruyan direnç dönüşümüdür. Kitapta bu yöntem yok; sınavda kullanılacak yöntemi öğretmenine sor.

## Alıştırma

`R1=100 Ω`, `R3=220 Ω`, `R2=150 Ω`, `R4=300 Ω` ise köprü dengeli mi?

**Cevap:** `100/220≈0,455`, `150/300=0,5`; oranlar eşit değil. Köprü dengesiz, orta kol akımı genel olarak sıfır değildir; köprü direncini silme. Devre/topolojiye göre Y-Δ veya düğüm gerilimi gerekir.


---

<a id="chapter-07"></a>

# Ölçü Aletleri: Nereye Bağlanır, Nasıl Kullanılır?

**Kaynak:** *Elektronik Uygulamaları* PDF 24–25, 32–34, 41–43, 45–50, 57–67, 70–72.

## Ölçü aletinin devreye bağlanması

| Ölçülen | Alet | Bağlantı | Devrenin durumu |
|---|---|---|---|
| Gerilim | Voltmetre | Ölçülecek elemanın uçlarına paralel | Enerjili olabilir; doğru AC/DC modu ve güvenli sınır |
| Akım | Ampermetre | Akım yolunu açıp araya seri | Akım girişi ve kademe doğru seçilmeli |
| Direnç | Ohmmetre | Parçanın iki ucuna | Güç kesik; kondansatör boşalmış |
| Diyot | Diyot test modu | Problar iki uçta; sonra ters çevrilip kıyaslanır | Devre enerjisiz |
| Kapasite | LCR metre/kapasite modu | Parçanın uçlarına | Devre enerjisiz ve kondansatör boşalmış |

### Ampermetreyi paralel bağlama

Ampermetrenin iç direnci çok küçüktür. Kaynağın iki ucuna paralel bağlanırsa kısa devreye yakın yol oluşturabilir. Akım ölçmek için devrenin enerji bağlantısını kes, ölçmek istediğin seri yolu aç, ampermetreyi araya ekle; sonra öğretmen gözetiminde yeniden enerji ver.

### Voltmetreyi seri bağlama

Voltmetrenin iç direnci yüksektir. Akım yoluna seri bağlamak devreyi bozabilir ve yanlış ölçüm verir. Ölçülecek direncin iki ucuna paralel bağla.

### Direnç ölçümünde

Devre enerjisiz olmalıdır. Devre üstünde paralel başka yollar varsa ölçü aleti birden fazla yolun eşdeğerini okuyabilir; doğru parça değerini ölçmek için öğretmenin talimatına göre bacağın birini devreden ayır.

## Multimetreyi kullanma sırası

1. Ölçülecek büyüklüğü seç: `V`, `A`, `Ω`, süreklilik veya diyot.
2. AC mi DC mi ölçüleceğini belirle (`~` AC, `⎓` DC işareti).
3. Probları doğru sokete tak: siyah `COM`; kırmızı gerilim/direnç veya gereken akım soketi.
4. Manuel kademeli cihazda bilinmiyorsa güvenli yüksek kademeden başla.
5. Prob bağlantısını enerjiyi keserek kur; öğretmen onayı olmadan enerjilendirme.
6. Sonucun birimini oku ve gerekiyorsa `A↔mA` gibi dönüşüm yap.
7. İş bitince akım girişindeki kırmızı kabloyu tekrar V/Ω soketine al.

## Kitaptaki uygulamalara bağla

- PDF 24–25: Direnç renk kodunu ohmmetreyle karşılaştır.
- PDF 32–34: Kondansatör değerini koddan bul ve LCR metreyle karşılaştır.
- PDF 41–43: Diyot/LED yönünü test et.
- PDF 45–48: Transistörün sağlamlığını ve uçlarını ölç.
- PDF 57–67: Akım için ampermetreyi seri; gerilim için voltmetreyi paralel kullan.
- PDF 70–72: DA/DC kaynakların tanımı ve kaynak örnekleri.

## Güvenlik

- Şebeke elektriğiyle uygulama yapma. Yalnızca öğretmenin hazırladığı düşük gerilimli eğitim kaynağını kullan.
- Enerjili devrede direnç/kapasite ölçme.
- Kondansatörler güç kesilse de enerji tutabilir; boşaltmayı öğretmen gözetiminde yap.
- Ampermetreyi doğrudan pile/kaynağa bağlama.
- Ölçü aletinin soket, AC/DC modu, kademe ve maksimum giriş değerini kontrol et.
- Elinde hasarlı prob veya yalıtımı açılmış kablo varken ölçüm yapma.


---

<a id="chapter-08"></a>

# Frekans, Periyot ve Hz–kHz–MHz

**Ek konu:** Bu başlık *Elektronik Uygulamaları* PDF'sinin ilk 72 sayfasında temel konu olarak yer almıyor. Dalga biçimi ve devre sorularında gereken birim farkını tamamlamak için eklenmiştir.

![Dalgada bir periyot ve frekans gösterimi](assets/diagrams/frekans-periyot.svg)

## Frekans nedir?

Frekans (`f`), tekrar eden bir sinyalin bir saniyede kaç tam çevrim yaptığını söyler. Birimi hertz (Hz).

- `1 Hz`: saniyede 1 çevrim.
- `1 kHz = 1.000 Hz`.
- `1 MHz = 1.000 kHz = 1.000.000 Hz`.
- `1 GHz = 1.000 MHz = 1.000.000.000 Hz`.

## Periyot nedir?

Periyot (`T`), dalganın bir tam çevrimi tamamlaması için geçen süredir. Birimi saniye (s).

```text
f = 1/T         T = 1/f
```

Frekans yükseldikçe periyot kısalır; frekans düşerse periyot uzar.

### Örnek 1 — 50 Hz'in periyodu

`T=1/f=1/50 s=0,02 s=20 ms`.

### Örnek 2 — 2 kHz'in periyodu

Önce `2 kHz=2.000 Hz`.<br>
`T=1/2.000 s=0,0005 s=0,5 ms=500 µs`.

### Örnek 3 — Periyottan frekans

Periyot `T=4 ms`. Önce saniyeye çevir: `4 ms=0,004 s`.<br>
`f=1/0,004=250 Hz`.

## Birimler neden karışıyor?

`MHz` frekans; `mA` akım; `mΩ` direnç; `ms` zaman birimidir. Baş harf ve büyüklük aynı şey değildir. `m` mili, `M` mega; `Hz` çevrim/saniye, `A` elektrik akımıdır.

### Kendini dene

1. `3 MHz` kaç kHz?
2. `1 kHz` sinyalin periyodu kaç ms?
3. `250 µs` periyot kaç Hz?

**Cevap:** 1) `3.000 kHz`. 2) `1/1.000 s=1 ms`. 3) `250 µs=0,00025 s`; `f=1/0,00025=4.000 Hz=4 kHz`.


---

<a id="chapter-09"></a>

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


---

<a id="chapter-10"></a>

# Mikrodenetleyici — Sayı Sistemleri ve Mantık Kapıları

**Kaynak:** *Mikrodenetleyici*, PDF 1–40. PDF 1–17 kapak, ön bilgiler ve bölüm tanıtımıdır. Sayı sistemleri PDF 18'de, temel lojik kapı tanıtımı PDF 37'de başlar. İlk 40 sayfada özellikle ikilik sayılar, taban dönüşümleri, AND/OR kapıları ve uygulamalar yer alır.

## Konu haritası

| PDF sayfaları | Kaynak konusu | Bu rehber |
|---:|---|---|
| 18–19 | Sayı sistemi, onluk/ikilik/sekizlik/onaltılık | [İkili sayı sistemi](docs/mikrodenetleyici/01-ikili-sayi-sistemi.md) |
| 20–27 | İkili, sekizlik, onaltılık sayılarda işlemler | [İkili sayı sistemi](docs/mikrodenetleyici/01-ikili-sayi-sistemi.md) |
| 28–36 | Tabanlar arasında dönüşüm ve değerlendirme | [İkili sayı sistemi](docs/mikrodenetleyici/01-ikili-sayi-sistemi.md), [alıştırmalar](docs/mikrodenetleyici/05-alistirmalar.md) |
| 37–39 | Temel kapılar; AND kapısı, 4081/7408 uygulaması | [VE ve VEYA kapıları](docs/mikrodenetleyici/02-lojik-kapilar.md) |
| 39–40 | OR kapısı tanımı ve uygulaması | [VE ve VEYA kapıları](docs/mikrodenetleyici/02-lojik-kapilar.md) |

## Önerilen sıra

1. Bit, basamak ve sayı değerinin farkını öğren.
2. `00, 01, 10, 11` dizisinin ikili sayma olduğunu gör.
3. Onluk ↔ ikilik dönüşümü ve 3 bit / 4 bit sayıların kapsamını çalış.
4. Doğruluk tablosu satırlarını üret: n girişte `2ⁿ` durum.
5. Önce AND, sonra OR için her satırın çıkışını kendin hesapla.
6. Boş tabloları [alıştırmalarda](docs/mikrodenetleyici/05-alistirmalar.md) doldur, ardından cevap anahtarını aç.

## Kaynak ile ek bilginin ayrımı

- **Kaynakta (PDF 18–40):** sayı sistemleri ve taban dönüşümleri; temel lojik kapılar tanıtımı; VE (AND), VEYA (OR) ve 4081/7408 ile uygulama.
- **Kısa tamamlayıcı anlatım:** NOT kapısı, aynı PDF'de PDF 37'de temel kapı olarak sayılır.
- **Bu sayfa aralığının dışında, ek bilgi:** NAND, NOR, XOR, XNOR'un ayrıntılı doğruluk tabloları; mikrodenetleyicinin portları ve Arduino benzeri kartla buton/LED örneği.

Ek konuları, kaynakta öğretilmiş gibi göstermemek için ilgili bölümde ayrıca etiketledim.


---

<a id="chapter-11"></a>

# İkili Sayı Sistemi, Sayma ve Taban Dönüşümleri

**Kaynak:** *Mikrodenetleyici* PDF 18–36. Bu bölümde ikilik (binary), onluk (decimal), sekizlik (octal) ve onaltılık (hexadecimal) sistemler yer alır.

![İki ve üç bit ile ikili sayma](assets/diagrams/ikili-sayma.svg)

## 1. Basamak ve sayı değeri farklı şeylerdir

Onluk sayı sisteminde on sembol vardır: `0,1,2,3,4,5,6,7,8,9`. Bir sayının basamağının değeri, konumuna göre 10'un kuvvetleriyle belirlenir.

`341₁₀ = 3×10² + 4×10¹ + 1×10⁰ = 300+40+1`.

İkilik sayı sisteminde sadece iki sembol vardır: `0` ve `1`. Basamaklar sağdan başlayarak `2⁰, 2¹, 2², ...` ağırlıklarını alır.

`1100₂ = 1×2³ + 1×2² + 0×2¹ + 0×2⁰ = 8+4=12₁₀`.

**Buradaki `1100` dört bittir ve değeri on ikidir.** Onluk `12` sayısı, “12 tane 1” veya “12 basamak” demek değildir.

| Sistem | Taban | Kullanılan rakamlar | Örnek |
|---|---:|---|---|
| Onluk (decimal) | 10 | 0–9 | `12₁₀` |
| İkilik (binary) | 2 | 0–1 | `1100₂` |
| Sekizlik (octal) | 8 | 0–7 | `14₈` |
| Onaltılık (hexadecimal) | 16 | 0–9, A–F | `C₁₆` |

Onaltılıkta `A=10`, `B=11`, `C=12`, `D=13`, `E=14`, `F=15`.

## 2. İki girişin kombinasyonlarını neden 00, 01, 10, 11 yazarız?

İkili sayma yaparız:

| Onluk sıra | A | B | İki bit |
|---:|---:|---:|---|
| 0 | 0 | 0 | `00` |
| 1 | 0 | 1 | `01` |
| 2 | 1 | 0 | `10` |
| 3 | 1 | 1 | `11` |

İki bağımsız girişin her biri iki değer alır; toplam durum sayısı `2×2=4`. Daha fazla girişte `2ⁿ` kullanılır:

| Giriş sayısı n | Kombinasyon sayısı `2ⁿ` |
|---:|---:|
| 1 | 2 |
| 2 | 4 |
| 3 | 8 |
| 4 | 16 |
| 5 | 32 |

Üç girişli kombinasyonlar `000, 001, 010, 011, 100, 101, 110, 111` şeklinde sayılır. Her bir bit sütunu, sayma boyunca 0 ile 1 arasında düzenli aralıklarla değişir.

## 3. Onluk sayıyı ikiliye çevirme

Onluk sayıyı art arda 2'ye böl. Kalanları **alttan üste** oku.

**Örnek: `12₁₀` → ikilik**

| Bölme | Bölüm | Kalan |
|---|---:|---:|
| 12 ÷ 2 | 6 | 0 |
| 6 ÷ 2 | 3 | 0 |
| 3 ÷ 2 | 1 | 1 |
| 1 ÷ 2 | 0 | 1 |

Kalanları alttan üste oku: `1100₂`. Kontrol: `8+4=12`.

**Örnek: `13₁₀`**

`13÷2=6 kalan1`; `6÷2=3 kalan0`; `3÷2=1 kalan1`; `1÷2=0 kalan1`.<br>
Alttan üste `1101₂`. Kontrol: `8+4+1=13`.

## 4. İkiliden onluya

Basamakları sağdan sola `2⁰, 2¹, 2², ...` ile çarp; sonuçları topla.

`10110₂ = 1×16 + 0×8 + 1×4 + 1×2 + 0×1 = 22₁₀`.

## 5. İkili ↔ onaltılık / sekizlik

- İkili → onaltılık: sağdan başlayıp dörder bitlik gruplara ayır. Her grup bir hex rakamına karşılık gelir.
  - `1100 1010₂` → `C A` → `CA₁₆`.
- Onaltılık → ikili: her hex rakamını 4 bite çevir.
  - `3F₁₆` → `0011 1111₂`.
- İkili → sekizlik: sağdan başlayıp üçer bitlik gruplara ayır.
  - `101 110₂` → `5 6` → `56₈`.

Grup eksik kalırsa en sola sıfır eklenebilir: `1100₂` zaten dört bit; `101₂` sekizlik dönüşümde üçlü gruptur.

## 6. İkili toplama — en çok kullanılan kurallar

| İşlem | Sonuç |
|---|---|
| `0+0` | `0` |
| `0+1` | `1` |
| `1+0` | `1` |
| `1+1` | `10` (0 yaz, 1 elde) |

**Örnek:**

```text
  1011₂  (11)
+ 0110₂  ( 6)
-------
 10001₂  (17)
```

Sağdan sola: `1+0=1`; `1+1=10` (0, elde 1); `0+1+elde1=10`; `1+0+elde1=10`. Sonuç `10001₂=17₁₀`.

Kaynak PDF 20–27'de ikili, sekizlik, onaltılık toplama/çıkarma; ikili çarpma ve bölme örneklenir. Sıfıra bölme matematikte tanımsızdır.

## Alıştırmalar

1. `1011₂` kaç onluk?
2. `12₁₀` ikilikte kaçtır?
3. `111₂ + 1₂`?
4. `10110110₂` onaltılıkta kaçtır?
5. Üç lojik giriş için kaç olası giriş satırı gerekir?

**Cevap:** 1) `11`. 2) `1100₂`. 3) `1000₂`. 4) `B6₁₆`. 5) `2³=8`.


---

<a id="chapter-12"></a>

# Doğruluk Tablosu, VE ve VEYA Kapıları

**Kaynak:** *Mikrodenetleyici* PDF 37–40. PDF 37 VE/OR/NOT kapılarını tanıtır; PDF 38'de AND için `00, 01, 10, 11` girişlerini 4081 ile deneyip tablo doldurma; PDF 39–40'da OR uygulaması yer alır.

![AND ve OR sembolleri, giriş anahtarları ve çıkış LED'i](assets/diagrams/lojik-kapilar.svg)

## 1. Lojik giriş 0 ve 1 ne demek?

İkili dijital devrede giriş bir mantık durumu taşır:

- `0` = LOW/pasif/düşük lojik seviye.
- `1` = HIGH/aktif/yüksek lojik seviye.

Gerçek devrede 0 ve 1, belirli gerilim aralıklarıyla temsil edilir. Hangi voltajın HIGH olduğu entegre ailesine ve besleme gerilimine bağlıdır; her cihazda `1=5 V` diye varsayma.

`A` ve `B` girişlerin; `Q` çıkışın adıdır. Doğruluk tablosu, her giriş durumunda çıkışın ne olduğunu gösterir.

## 2. Tablo satırlarını sıfırdan oluştur

İki giriş, her biri 0 veya 1: dört durum vardır (`2²=4`). İkili sayar gibi yaz:

```text
00
01
10
11
```

Başka satır yoktur: A için 2, B için 2 olasılık; çarpımları 4. Üç giriş olursa `2³=8` satır.

**İpucu:** En sağdaki bit her satırda değişir: `0,1,0,1`. Yanındaki bit iki satırda bir değişir: `0,0,1,1`. Üç girişte en soldaki bit dört satırda bir değişir.

## 3. VE kapısı (AND)

AND, matematikteki **mantıksal çarpma** işlemidir. `Q=A·B` veya `Q=A AND B`.

- Çıkış `Q=1` olması için A **ve** B girişleri ikisi de 1 olmalı.
- Girişlerden en az biri 0 ise çarpım 0 çıkar.

| A | B | Q=A·B |
|---:|---:|---:|
| 0 | 0 | 0 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 1 |

Satırları neden böyle?

- `00`: iki koşul da sağlanmıyor → 0.
- `01`: A koşulu yok → 0.
- `10`: B koşulu yok → 0.
- `11`: ikisi de aktif → 1.

**Gerçek hayat modeli:** Makineyi çalıştırmak için güvenlik kapağı kapalı **ve** başlat düğmesine basılmış olmalı. İki koşuldan biri eksikse motor çıkışı aktif olmaz.

### Elektriksel eşdeğer fikri

İki normal anahtarı seri bağla: iki anahtar da kapanınca lambaya yol açılır. Bu, AND mantığını gösteren öğretici modeldir. Gerçek lojik entegre aynı mekanik anahtar bağlantısı değildir.

### Entegreler

Kaynak PDF 38–39'da 4081 ve 7408/74LS08 entegreleriyle VE uygulaması yaptırır. Bir 4081/7408 paketinde birden fazla iki girişli AND kapısı bulunur; gerçek bacak ve besleme bağlantısını kullanılan tam modelin veri sayfasından doğrula.

## 4. VEYA kapısı (OR)

OR, **mantıksal toplama** işlemidir. `Q=A+B` veya `Q=A OR B`. Bu `+`, normal aritmetik toplama değil, “en az bir giriş aktif mi?” sorusudur.

- A veya B'den **en az biri** 1 ise çıkış 1.
- Yalnız ikisi de 0 ise çıkış 0.

| A | B | Q=A+B |
|---:|---:|---:|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 1 |

- `00`: aktif kaynak yok → 0.
- `01`: B aktif → 1.
- `10`: A aktif → 1.
- `11`: ikisi aktif → 1.

**Gerçek hayat modeli:** Alarm iki pencereden **herhangi biri** açıldığında çalışsın. İki sensörün birden alarm vermesi gerekmez.

### Elektriksel eşdeğer fikri

İki normal anahtarı paralel bağla: kollardan biri kapansa bile lambaya akım yolu oluşur. Bu, OR mantığının öğretici modelidir.

## 5. AND ve OR yan yana

| Giriş AB | AND (ikisi de 1 gerekir) | OR (en az biri 1 yeter) |
|---|---:|---:|
| `00` | 0 | 0 |
| `01` | 0 | 1 |
| `10` | 0 | 1 |
| `11` | 1 | 1 |

Girişler `01` veya `10` olduğunda çıkışların farklı olması, iki kapının farklı koşulu test etmesindendir. `11` her iki koşulda da 1 üretir; `00` her ikisinde de 0.

## 6. Doğruluk tablosunu her kapı için oluşturma

1. Giriş sayısını bul (`n`).
2. Satır sayısını `2ⁿ` hesapla.
3. Giriş kombinasyonlarını 0'dan başlayarak ikili say.
4. Kapının kuralını bir cümleyle yaz.
5. Girişleri tek satırda kurala uygula; çıkışı yaz.
6. Örnek satırlarla kontrol et.

**Boş tablo — önce kendin doldur:**

| A | B | AND çıkışı | OR çıkışı |
|---:|---:|---:|---:|
| 0 | 0 |  |  |
| 0 | 1 |  |  |
| 1 | 0 |  |  |
| 1 | 1 |  |  |

Yanıtı sayfanın altındaki [alıştırma cevaplarında](docs/mikrodenetleyici/05-alistirmalar.md) kontrol et.

## Alıştırma

Bir makine için `A=kapak kapalı`, `B=başlat düğmesi basılı`, `Q=motor etkin`. Motor ancak kapak kapalı ve düğme basılıyken çalışsın.

1. AND mi OR mu?
2. `A=1, B=0` iken `Q`?
3. `A=1, B=1` iken `Q`?

**Cevap:** 1) AND. 2) `0`, çünkü başlat koşulu yok. 3) `1`, çünkü iki koşul da mevcut.


---

<a id="chapter-13"></a>

# NOT, NAND, NOR, XOR ve XNOR Kapıları

**Kapsam notu:** PDF 37, AND/OR/NOT kapılarını temel kapılar olarak adlandırır. PDF 1–40 içinde NAND, NOR, XOR ve XNOR'un ayrıntılı anlatımı yoktur; bunlar tamamlayıcı dijital mantık bilgisidir.

`A̅` veya `NOT A`, A'nın tersidir: `A=0` ise `A̅=1`; `A=1` ise `A̅=0`.

| A | NOT A |
|---:|---:|
| 0 | 1 |
| 1 | 0 |

## İki girişli kapılar

| A | B | AND | NAND | OR | NOR | XOR | XNOR |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 0 | 1 | 0 | 1 | 0 | 1 |
| 0 | 1 | 0 | 1 | 1 | 0 | 1 | 0 |
| 1 | 0 | 0 | 1 | 1 | 0 | 1 | 0 |
| 1 | 1 | 1 | 0 | 1 | 0 | 0 | 1 |

- **NAND:** AND sonucunun tersi. Yalnız `11` iken 0.
- **NOR:** OR sonucunun tersi. Yalnız `00` iken 1.
- **XOR:** Girişler farklıysa 1; aynıysa 0.
- **XNOR:** Girişler aynıysa 1; farklıysa 0.

## Günlük örnekler

- **NOT:** “Kapı kapalı değil” uyarısı. Giriş kapalı bilgisiyse NOT çıkışı açık alarmını verebilir.
- **NAND:** AND koşullarının tamamlanmadığını bildiren hata çıkışı.
- **NOR:** Hiçbir sensör aktif değilken bekleme göstergesi.
- **XOR:** İki anahtarın durumları birbirinden farklıysa 1.
- **XNOR:** İki bit aynı mı? Basit eşitlik karşılaştırıcı.

Kapıların fiziksel sembolleri ve pin bağlantıları için tam parça numarasının veri sayfasını kullan. Lojik ifadelerde AND genellikle `·`, OR `+`, NOT üst çizgi/`¬`, XOR `⊕` ile gösterilir.


---

<a id="chapter-14"></a>

# Mikrodenetleyici, HIGH/LOW, Buton ve LED

**Tamamlayıcı uygulama:** PDF 1–40 sayı sistemleri ve lojik kapı girişine odaklanır. Mikrodenetleyicinin programlanması bu kitabın daha sonraki PDF sayfalarında yer alır; aşağıdaki Arduino benzeri örnek, ilk 40 sayfa dışında başlangıç amaçlı ek açıklamadır.

![Mikrodenetleyicide girişleri okuma, koşulu işleme ve çıkışı sürme](assets/diagrams/mikrodenetleyici.svg)

## 1. Mikrodenetleyici nedir?

Mikrodenetleyici; işlemci, bellek ve giriş/çıkış birimleri aynı çipte bulunan programlanabilir bir kontrol bilgisayarıdır. Sensör veya butondan giriş okur, programındaki kuralları uygular ve LED, buzzer ya da sürücü devresine çıkış verir.

```text
Buton / sensör → dijital giriş → program/lojik → dijital çıkış → LED / sürücü
```

## 2. Dijital giriş, çıkış ve lojik seviye

- **Giriş:** Kartın dış dünyadan okuduğu sinyal (`digitalRead`).
- **Çıkış:** Kartın dış devreye verdiği kontrol seviyesi (`digitalWrite`).
- **LOW:** Lojik 0'a karşılık gelen düşük gerilim aralığı.
- **HIGH:** Lojik 1'e karşılık gelen yüksek gerilim aralığı.

HIGH'ın kaç volt olduğu kart modeline bağlıdır; 3,3 V kartın girişine 5 V uygulamak kartı bozabilir. Üretici sınırını kontrol et.

## 3. Butonla LED örneği

Buton bir dijital girişe; LED ise uygun seri akım sınırlama direnciyle dijital çıkışa bağlanır. Kartta dahili pull-up varsa, aşağıdaki bağlantı örneğinde buton giriş pini ile GND arasında bağlanır. Buton basılınca giriş LOW olur; bırakılınca dahili pull-up HIGH okutur.

```cpp
const int buttonPin = 2;
const int ledPin = 13;

void setup() {
  pinMode(buttonPin, INPUT_PULLUP);
  pinMode(ledPin, OUTPUT);
}

void loop() {
  const bool pressed = (digitalRead(buttonPin) == LOW);
  digitalWrite(ledPin, pressed ? HIGH : LOW);
}
```

Satır satır:

- `buttonPin` ve `ledPin`: kullanılacak pin numaralarını isimlendirir.
- `setup()`: program başlayınca bir kez çalışır.
- `INPUT_PULLUP`: buton girişini kararlı HIGH seviyesinde tutan iç direnci etkinleştirir.
- `OUTPUT`: LED pinini çıkış yapar.
- `loop()`: sürekli tekrarlanır.
- `digitalRead(...) == LOW`: buton basılınca LOW okunacağını hesaba katar.
- `digitalWrite(...)`: basılıyken LED çıkışını HIGH, değilken LOW yapar.

Bazı kartların dahili LED'i 13 numaralı pine bağlıdır; harici LED bağlayacaksan kart pin sınırına uygun **seri direnç** kullan. Pin kapasitesini aşma; motor/röle gibi yükleri doğrudan mikrodenetleyici pininden sürme, uygun sürücü/transistör ve koruma elemanı kullan.

## 4. Mantık kapıları ile bağı

Bir programdaki `if (A && B)` koşulu iki koşulun birlikte doğru olmasını istediğinden AND mantığıdır. `if (A || B)` koşulu en az birinin doğru olmasını istediğinden OR mantığıdır. Donanım kapıları ve yazılımdaki Boole koşulları aynı temel mantık kurallarını kullanır.

## Güvenlik ve bağlantı kontrolü

1. Kartın çalışma gerilimini ve pin eşiklerini kontrol et.
2. GND ortak bağlantısını doğru yap.
3. LED'i dirençsiz bağlama.
4. Güç vermeden önce polarite ve kısa devreyi kontrol et.
5. Şebeke gerilimi veya yüksek akımlı yükü mikrodenetleyici pinine bağlama.


---

<a id="chapter-15"></a>

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
