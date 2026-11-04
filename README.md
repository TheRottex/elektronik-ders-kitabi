# Görsel Destekli Elektronik ve Mikrodenetleyici Ders Rehberi

Elektroniğe ve sayısal mantığa yeni başlayanlar için, iki ders kitabının belirtilen bölümlerinden hareketle hazırlanmış görsel çalışma rehberi. Formüller tek başına bırakılmaz: semboller, birimler, devre yolu, çözüm adımları, kontroller ve alıştırmalar birlikte verilir.

> **Kapsam:** *Elektronik Uygulamaları* PDF'si 1–72. sayfalar (ders içeriği basılı kitapta 18. sayfada başlar); *Mikrodenetleyici* PDF'si 1–40. sayfalar. PDF dosyaları telif ve dosya boyutu nedeniyle depoya eklenmemiştir. Bölüm başlıklarının yanındaki PDF sayfa numaraları kaynakta geri dönüp ilgili resmi bulmayı sağlar. Rehberdeki yeni şemalar özgün çizimdir.

## Nereden başlamalı?

Tamamını tek uzun Markdown belgesi olarak okumak veya yazdırmak için [Birleşik Ders Kitabı](KITAP.md); görselleri içeren A4 baskı çıktısı için [KITAP.pdf](KITAP.pdf). Bölüm bölüm çalışıp hızlıca aramak için aşağıdaki konu dizinini kullan.

### Elektronik Uygulamaları

1. [Ders haritası ve çalışma yolu](docs/elektronik/00-ders-haritasi.md)
2. [Elektriksel büyüklükler, birimler ve dönüşümler](docs/elektronik/01-buyuklukler-birimler.md)
3. [Devre elemanları: direnç, kondansatör, bobin, diyot, transistör, trafo](docs/elektronik/02-devre-elemanlari.md)
4. [Ohm Kanunu, formül üçgeni ve güç hesapları](docs/elektronik/03-ohm-kanunu-ve-guc.md)
5. [Seri, paralel ve karışık devreleri adım adım çözme](docs/elektronik/04-seri-paralel-karisik.md)
6. [Çapraz/köprü devreleri ve yıldız-üçgen dönüşümü — ek konu](docs/elektronik/05-kopru-yildiz-ucgen.md)
7. [Multimetre, ampermetre, voltmetre ve güvenli ölçüm](docs/elektronik/06-olcum-ve-guvenlik.md)
8. [Frekans, periyot ve Hz–kHz–MHz — kitaba ek çalışma](docs/elektronik/07-frekans-periyot.md)
9. [Elektronik alıştırmalar ve açıklamalı cevap anahtarı](docs/elektronik/08-alistirmalar.md)

### Mikrodenetleyici ve sayısal mantık

1. [Mikrodenetleyici ders haritası](docs/mikrodenetleyici/00-ders-haritasi.md)
2. [İkili sayı sistemi ve taban dönüşümleri](docs/mikrodenetleyici/01-ikili-sayi-sistemi.md)
3. [Doğruluk tablosu, VE ve VEYA kapıları](docs/mikrodenetleyici/02-lojik-kapilar.md)
4. [NOT, NAND, NOR, XOR ve XNOR — ek dijital mantık](docs/mikrodenetleyici/03-diger-kapilar.md)
5. [Mikrodenetleyici, dijital giriş/çıkış ve LED — ek uygulama](docs/mikrodenetleyici/04-mikrodenetleyici-uygulama.md)
6. [Sayısal mantık alıştırmaları ve cevap anahtarı](docs/mikrodenetleyici/05-alistirmalar.md)

### Sınava odaklı çalışma

[Hangi senaryo? — genel harita](docs/sinav/00-sinav-haritasi.md)

**1. Senaryo (Elektronik: direnç dahil 8 soru)**
1. [Harita ve 3 günlük plan](docs/sinav/senaryo-1/00-senaryo-1-haritasi.md)
2. [Elektronik konu çalışması](docs/sinav/senaryo-1/01-elektronik-sinav-calismasi.md)
3. [Deneme sınavı ve cevaplar](docs/sinav/senaryo-1/02-deneme-sinavi-ve-cevaplar.md)

**2. Senaryo (Elektronik 8 soru + Mikrodenetleyici 5 soru)**
1. [Harita, eksik listesi ve 5 günlük plan](docs/sinav/senaryo-2/00-senaryo-2-haritasi.md)
2. [Elektronik: kondansatör, bobin, diyot, transistör, trafo, seri/paralel/karışık](docs/sinav/senaryo-2/01-elektronik-sinav-calismasi.md)
3. [Mikro: sayı sistemleri ve işlemler](docs/sinav/senaryo-2/02-mikro-sayi-sistemleri-sinav.md)
4. [Mikro: Boole, De Morgan, entegre seçimi ve breadboard devresi](docs/sinav/senaryo-2/03-mikro-lojik-entegre-sinav.md)
5. [Deneme sınavı ve cevap anahtarı](docs/sinav/senaryo-2/04-deneme-sinavi-ve-cevaplar.md)

## Görsel dizini

- [Ohm Kanunu formül üçgeni ve birim ölçeği](assets/diagrams/ohm-birimler.svg)
- [Seri ve paralel devre karşılaştırması](assets/diagrams/seri-paralel.svg)
- [Karışık devrenin adım adım sadeleştirilmesi](assets/diagrams/karisik-devre.svg)
- [Köprü devresi ve denge koşulu](assets/diagrams/kopru-devresi.svg)
- [Devre elemanlarının temel sembolleri](assets/diagrams/eleman-sembolleri.svg)
- [Frekans ve periyot dalga şekli](assets/diagrams/frekans-periyot.svg)
- [İki ve üç girişli ikili sayma düzeni](assets/diagrams/ikili-sayma.svg)
- [VE ve VEYA kapıları](assets/diagrams/lojik-kapilar.svg)
- [Mikrodenetleyici giriş–işlem–çıkış görünümü](assets/diagrams/mikrodenetleyici.svg)
- [Kullanıcı görsellerini ekleme yönergesi](assets/kullanici-gorselleri/README.md)

## Kaynak sayfa haritası

| Ders | PDF sayfaları | Başlıklar |
|---|---:|---|
| Elektronik Uygulamaları | 18–53 | Analog devre elemanları |
| Elektronik Uygulamaları | 54–69 | Seri, paralel, karışık devreler ve değerlendirme soruları |
| Elektronik Uygulamaları | 70–72 | Doğru akım devrelerine giriş |
| Mikrodenetleyici | 18–36 | Sayı sistemleri, ikili aritmetik, taban dönüşümleri |
| Mikrodenetleyici | 37–40 | Lojik kapılara giriş; VE ve VEYA uygulamaları |

PDF sayfa numaraları dosya içindeki görüntüleyici sayfa numarasıdır. Ders kitaplarının basılı sayfa numarası farklı olabilir.

## Katkıda bulunma ve görsel ekleme

Kullanıcı tarafından eklenecek fotoğrafları `assets/kullanici-gorselleri/` altına koyup [görsel ekleme yönergesini](assets/kullanici-gorselleri/README.md) izleyin. Görselin size ait olduğundan veya kullanma izniniz bulunduğundan emin olun. Kaynak kitaptaki sayfa görselleri doğrudan kopyalanmamış; bunun yerine kavramları anlatan özgün vektör şemaları çizilmiştir.

## Birleşik dosyaları yeniden üret

Python 3.10+ kurulu ortamda:

```powershell
python -m pip install -r requirements.txt
python tools/build_book.py
python tools/build_pdf.py
python tools/validate_repo.py
```

`KITAP.md` ve `KITAP.pdf`, sırasıyla kaynak bölümlerden ve SVG şemalardan üretilir. Kaynak metinlerde düzenleme yapın; oluşturulmuş çıktıyı sonradan değiştirirseniz bir sonraki derleme üzerine yazar.

## Güvenlik notu

Örnekler düşük gerilimli eğitim devreleridir. Şebeke gerilimiyle deneme yapmayın. Ampermetreyi kaynağın iki ucuna paralel bağlamayın; kısa devre oluşturabilir. Kondansatörleri ölçmeden önce güvenli biçimde boşaltın ve öğretmen gözetimi olmadan yüksek güç devreleri kurmayın.
