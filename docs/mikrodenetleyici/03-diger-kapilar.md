# NOT, NAND, NOR, XOR ve XNOR Kapıları

**Kapsam notu:** PDF 37, AND/OR/NOT kapılarını temel kapılar olarak adlandırır. NAND (PDF s.42), NOR (s.43), XOR/ÖZEL VEYA (s.44–45, 4070 ile uygulama) ve XNOR/ÖZEL VEYA DEĞİL (s.46) kaynakta da vardır; bu bölüm onları ek görsel ve örneklerle açıklar.

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
