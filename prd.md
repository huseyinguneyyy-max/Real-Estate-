# prd.md — Adakey

> **Adakey**: ada + key (anahtar), "Adanın anahtarı". KKTC'nin yapay zeka destekli emlak platformu.
> Sürüm: v0.1 taslak · 24.10.2026 · Rakamlar `models/finans_modeli.py` dosyasından alındı; hepsi varsayım.

---

## 1. Tek cümlede Adakey

Ev arayan için **ücretsiz, güvenli ve 5 dilde konuşan** bir emlak platformu. Emlakçı ve müteahhit için **ilanı bir kez girip her yerde yayınlatan ve müşteri getiren** bir iş aracı.

## 2. Kimler kullanacak?

| Kişi | Ne istiyor | Adakey ona ne veriyor |
|---|---|---|
| Yerel alıcı / kiracı | Hızlı, doğru, güncel ilan | Tüm ilanlar tek yerde, alarm, WhatsApp ile iletişim |
| Öğrenci | Ucuz, okula yakın kiralık | Öğrenci Evi butonu, üniversiteye mesafe filtresi |
| Yabancı alıcı (UK, DE, RU, Orta Doğu) | Güven, süreç bilgisi, uzaktan alım | Tapu rozeti, 5 dilde AI asistan, izin rehberi, video tur |
| Emlak ofisi | Daha az iş, daha çok müşteri | Otomasyon, müşteri takibi, takas ve talep bildirimleri |
| Müteahhit | Projesini yurt dışına satmak | Proje sayfası, ödeme planı, nitelikli yabancı müşteri |

---

## 3. Web sitesi ve uygulama: sayfa sayfa

### 3.1 Kullanıcı tarafı (adakey.app ve iOS/Android)
1. **Ana sayfa:** Büyük arama kutusu ("Ne arıyorsunuz? Yazın, biz bulalım"), hızlı butonlar, öne çıkan projeler, vitrin ilanları.
2. **Hızlı butonlar:** Acil Satılık · Vitrin · Öğrenci Evi · Ödeme Planlı / Taksitli · Takasa Açık · Fiyatı Düşen · Yeni Projeler · Denize Sıfır.
3. **Arama sonuçları:** Liste ve harita görünümü. Filtreler: fiyat, oda, m², bölge, tapu türü, eşyalı, ödeme planı, takasa açık.
4. **İlan detayı:**
   - Fotoğraflar ve video tur
   - Tapu türü rozeti
   - Fiyat ve bölge ortalamasıyla kıyas ("bölge ortalamasının %8 altında")
   - Taksit hesaplayıcı
   - **"Aracımı / arsamı takasa ver"** butonu
   - WhatsApp ve "Ara" butonları
   - Benzer ilanlar
5. **Proje sayfası (müteahhit):**
   - Kat planları, satılan ve kalan daireler
   - Ödeme planı tablosu
   - İnşaat ilerleme albümü
   - "Video görüşme talep et" butonu
6. **Ev Arıyorum:** Kullanıcı ne aradığını bir kez yazar. Uyan ilan çıkınca emlakçılar teklif verir, kullanıcıya bildirim gider.
7. **Yabancı Alım Rehberi (5 dil):**
   - Adım adım süreç: izin, avukat, vergi, tapu
   - Maliyet hesaplayıcı
   - 2026 kuralları özeti
8. **Bölge sayfaları:** Girne, İskele, Lefkoşa, Mağusa, Güzelyurt, Lefke ve mahalleler. Her sayfada ortalama fiyat, kira getirisi, okul ve plaj bilgisi bulunur.
9. **Hesabım:** Favoriler, kayıtlı aramalar, alarmlar, takas teklifleri, mesaj geçmişi.

### 3.2 Emlakçı / müteahhit paneli
1. **İlan girişi:** Fotoğraf yükle, AI başlık ve açıklamayı yazsın, 5 dile çevirsin. Tapu türü zorunlu.
2. **Toplu ilan aktarma:** Excel, XML ya da web sitesinden. İlk kurulumu Adakey ekibi yapar.
3. **Otomasyon merkezi:** Ayrıntısı §5'te.
4. **Müşteri kutusu (mini CRM):**
   - Gelen tüm talepler tek yerde: WhatsApp tıklamaları, formlar, takas teklifleri, Ev Arıyorum eşleşmeleri.
   - Her talebin durumu izlenir: Yeni → Arandı → Randevu → Teklif → Satış.
5. **Performans raporu:** İlan başına görüntülenme, tıklama, arama sayısı; haftalık e-posta.
6. **Paket ve doping:** Vitrin satın alma, öne çıkarma, paket yükseltme.

### 3.3 Yönetim paneli (Adakey ekibi)
- Ofis doğrulama (KTEB belgesi, kimlik), ilan onayı
- Şikayet ve sahte ilan takibi
- Blog ve rehber içerik yönetimi
- Banner ve sponsor alanları
- Raporlar

---

## 4. Adakey Asistan: yapay zeka sohbet botu

Sitenin her sayfasında sağ altta bir balon olarak durur. Uygulamada ayrı bir sekmesi olur. **WhatsApp ve Instagram DM'den de aynı asistan cevap verir** (2. fazda).

**Neleri yapabilir:**
1. **Sohbetle ev arama:** "Girne'de denize yakın, £150 bin altı, eşyalı 2+1 arıyorum." Asistan soruları netleştirir ("Bütçeniz peşin mi, taksitli mi?") ve ilanları kart olarak gösterir.
2. **Taksit ve ödeme planı:** "Bu evi 24 ay taksitle alabilir miyim?" Asistan ilandaki ödeme planını okur, peşinat ve aylık taksiti hesaplar. Banka kredisi seçeneği varsa gösterir.
3. **Takas:** "Arabamı vermek istiyorum." Asistan araç bilgisini alır, tahmini değeri ve farkı söyler, takas kartını emlakçıya gönderir.
4. **Yabancı alıcı soruları:** "Yabancı olarak kaç daire alabilirim?", "Tapu türü ne demek?", "Vergiler ne kadar?" Cevaplar Adakey'in güncel rehberinden gelir ve her cevapta "Avukatınıza doğrulatın" notu bulunur.
5. **Bölge danışmanı:** "Aileyle yaşamak için İskele mi Girne mi?", "Kira getirisi en yüksek bölge hangisi?"
6. **Site yardımı:** "Nasıl ilan veririm?", "Paketler ne kadar?", "Vitrin ne işe yarar?"
7. **Emlakçıya devir:** Kullanıcı ilgilendiğinde asistan "Sizi emlakçıyla bağlayayım mı?" diye sorar. Sohbet özeti (bütçe, aradığı ev, takas varlığı) emlakçının müşteri kutusuna düşer. **Emlakçıya giden müşteri adayı böylece "sıcak" olur.**

**Sınırlar:**
- Fiyat ve tapu bilgisini kendisi uydurmaz, sadece ilan verisini ve rehberi kullanır.
- Hukuki ve finansal tavsiye vermez, bilgi verir.
- Konuşma kayıtları KVKK/GDPR'a uygun saklanır.

**Maliyet:** AI API kullanımı başlangıçta ayda ~£100–300. Konuşma sayısı arttıkça artar ve altyapı bütçesinin içinde.

**evlek'ten farkı:** evlek'in AI'ı arama kutusunda çalışıyor ve uygulamada bir asistan sekmesi var. Adakey Asistan'ın farkları:
- Taksit hesaplıyor ve takas alıyor
- Müşteriyi emlakçıya özetle devrediyor
- WhatsApp ve Instagram'da da çalışıyor

---

## 5. Otomasyonlar

### 5.1 Emlakçı için (ilk sürümde)

| # | Otomasyon | Ne yapar |
|---|---|---|
| 1 | Her yerde yayınla | İlan girilince Instagram gönderisi ve hikâyesi + Facebook sayfası paylaşımı otomatik hazırlanır ve yayınlanır. Her paylaşımda Adakey linki ve ofis etiketi bulunur |
| 2 | Otomatik Reels | İlan fotoğraflarından müzikli kısa video üretilir (2. faz) |
| 3 | 5 dile çeviri | TR, EN, RU, DE, AR |
| 4 | AI ilan metni | Fotoğraflardan oda ve özellik çıkarımı, başlık ve açıklama önerisi |
| 5 | Anında müşteri bildirimi | Yeni talep → emlakçının WhatsApp'ına ve paneline bildirim |
| 6 | Otomatik ilk cevap | Gece gelen mesaja "Teşekkürler, sabah 9'da dönüş yapacağız" + ilan bilgisi |
| 7 | Takip hatırlatma | "Ahmet Bey'i 3 gündür aramadınız" |
| 8 | Eşleştirme | Yeni ilan girilince uyan "Ev Arıyorum" taleplerine ve kayıtlı aramalara otomatik bildirim gider |
| 9 | Eski ilan uyarısı | "Bu ilan 30 gündür az görüntüleniyor: fiyatı veya fotoğrafı güncelle" |
| 10 | Haftalık rapor | Performans e-postası |

### 5.2 Müteahhit için
- İnşaat ilerleme fotoğrafı yüklenince projeyi takip eden herkese otomatik e-posta veya bildirim gider
- "Son 5 daire" gibi kampanya duyuruları
- Yurt dışı müşteri adayları için otomatik çok dilli e-posta dizisi

### 5.3 Kullanıcı için
- Kayıtlı arama alarmı (e-posta ve bildirim)
- "Favorindeki ilanın fiyatı düştü" bildirimi
- Takas teklifine cevap geldi bildirimi

---

## 6. Fazlar, aylar ve giderler

**Aylık sabit gider:**
- Maaşlar £6.100: kurucu £1.500, yazılımcı £2.000, 2 pazarlamacı £2.600
- Altyapı ve AI £400
- Muhasebe ve diğer £500
- 4. aydan itibaren reklam ve içerik £1.500

### Faz 0 · 1. ay: Kurulum ve saha (gider ~£13.000)
- **Yapılacaklar:**
  - Şirket kuruluşu, avukat görüşü (tapu ve reklam politikası)
  - Adakey marka kimliği, alan adları, sosyal medya hesapları
  - **30 emlak ofisi ve 5 müteahhitle görüşme**, Kurucu Ortak sözleşmeleri
  - Tasarım ve teknik altyapı kurulumu
  - Instagram'da ilk içerikler (haftada 5 Reels)
- **Para nereye gidiyor:**
  - Maaşlar £6.100
  - Şirket ve avukat £3.500
  - Marka ve tasarım £1.500
  - Apple/Google hesapları ve test cihazları £1.000
  - Altyapı £400, diğer £500
- **Ay sonu hedefi:** 15 ofis ve 3 müteahhit "evet" demiş, 1.000 takipçi

### Faz 1 · 2.–3. ay: Ürünü yapma (gider ~£14.000)
- **Yapılacaklar:**
  - Web sitesi, emlakçı paneli, otomasyon (Instagram/Facebook paylaşımı, çeviri, AI metin)
  - Takas akışı, Ev Arıyorum, Adakey Asistan'ın ilk sürümü
  - İlan aktarma: Kurucu Ortak ofislerin ilanları taşınır
  - iOS ve Android uygulamaları
- **Para nereye gidiyor:** Maaşlar £12.200, altyapı ve AI £800, diğer £1.000
- **3. ay sonu hedefi:** 1.000+ ilan sisteme girilmiş, kapalı beta, 3.000 takipçi
- **İlk 3 ayın toplamı: ~£27.000**

### Faz 2 · 4.–6. ay: Lansman (gider ~£25.500, gelir ~£5.250)
- **Yapılacaklar:**
  - Herkese açılış (4. ay), basın, ilk reklamlar
  - Rusça, Almanca, Arapça dilleri
  - Vitrin ve proje paketlerinin satışı (4.–5. ay)
  - Ücretli ofis paketleri (6. ay, Kurucu Ortakların 3 ücretsiz ayı bitince)
- **Para nereye gidiyor:**
  - Maaşlar £18.300
  - Reklam ve içerik £4.500 (Meta ve Google testleri, video çekimleri)
  - Altyapı ve AI £1.200
  - Diğer £1.500
- **6. ay sonu hedefi:** 1.500+ ilan, 40+ ofis, 8+ proje, ayda 300 müşteri adayı, 10 ücretli ofis
- **İlk 6 ayın toplamı: ~£52.500 gider, ~£5.250 gelir → net ~£47.000 nakit ihtiyacı**

### Faz 3 · 7.–9. ay: Para kazanmaya başlama (gider ~£25.500, gelir ~£22.000)
- **Yapılacaklar:**
  - Asistan WhatsApp ve Instagram DM'de çalışmaya başlar
  - Otomatik Reels
  - AI sanal döşeme (boş evi dolu gösterme, etiketli)
  - Yurt dışı reklamları (UK ve DE)
  - İlk yurt dışı satış referans anlaşmaları
  - Banka ve sigorta sponsorluk görüşmeleri
- **Para nereye gidiyor:** Maaşlar £18.300, reklam ve içerik £4.500, altyapı ve AI £1.200, diğer £1.500
- **9. ay sonu hedefi:** 46 ücretli ofis, 13 proje, aylık gelir ~£10.000, **şirket aylık kâra geçer**

### Faz 4 · 10.–12. ay: Büyüme (gider ~£25.500, gelir ~£43.650)
- **Yapılacaklar:**
  - Ev360 pilotu (avukat, tapu takibi, taşınma, sigorta)
  - Değerleme aracı ("Evim kaç para?")
  - Aylık KKTC Emlak Raporu
  - UK ve DE fuarlarında stant ve ortaklıklar
- **Para nereye gidiyor:** Gider kalemleri aynı, reklamın büyük kısmı yurt dışı kampanyalara gider
- **12. ay sonu hedefi:** 82 ücretli ofis, 19 proje, aylık gelir ~£16.000, yatırımcıya ayda ~£5.300 (~$7.000)

### Özet

| Dönem | Gider | Gelir | Net |
|---|---|---|---|
| 1. ay | £13.000 | £0 | –£13.000 |
| 2.–3. ay | £14.000 | £0 | –£14.000 |
| 4.–6. ay | £25.500 | £5.250 | –£20.250 |
| 7.–9. ay | £25.500 | £21.970 | –£3.530 |
| 10.–12. ay | £25.500 | £43.650 | +£18.150 |
| **12 ay toplam** | **£103.500** | **£70.870** | **–£32.630** |

**Yatırımcıdan istenen: £65.000.** En derin nakit ihtiyacı 8. ayda ~£52.000; aradaki ~£13.000 tampon. Para iki dilimde gelir: £45.000 hemen, £20.000 5. ayda ve hedeflere bağlı.

---

## 7. evlek.app'e karşı strateji: onun yapmadıklarına odaklan

evlek'in güçlü olduğu alanlar ürün, SEO ve AI. Tek kişi olmasına rağmen hızlı özellik ekliyor. **AI özelliklerinde yarışmak bizi geride bırakır, çünkü AI artık herkesin erişebildiği bir şey.** Bizim kazanacağımız yerler:

| Alan | evlek | Adakey |
|---|---|---|
| İlan hacmi | 931 ilan, %84 Girne | Saha ekibiyle 1.500 → 5.000 ilan, tüm bölgeler |
| Emlakçı otomasyonu (IG/FB) | Yok | Ana özellik |
| Takas (araç/arsa ↔ ev) | Yok | Var |
| Müteahhit ve proje odağı, ödeme planı | Zayıf | Ana gelir kalemi |
| WhatsApp/Instagram'da asistan | Yok | 2. fazda |
| Sosyal medya ve video içerik | Zayıf | 2 pazarlamacı, haftada 5 Reels |
| Saha satış, yüz yüze ilişki | Tek kişi | 4 kişilik ekip |
| Müşteri adayını emlakçıya özetle devretme (CRM) | Yok | Var |

Kural: Her yeni özellik için önce şu soru sorulur: **"Bu emlakçıya ya da müteahhide müşteri getiriyor mu?"** Getirmiyorsa sıranın sonuna gider.

---

## 8. Adakey nerelere büyüyebilir?

1. **Ev360 hizmet pazaryeri:** avukat, tapu takibi, taşınma, tadilat, konut sigortası. Gelir modeli komisyon.
2. **Mülk yönetimi:** Yurt dışındaki ev sahipleri için kira tahsilatı, bakım, kısa dönem kiralama yönetimi. Düzenli aylık gelir getirir.
3. **Finans aracılığı:** Banka kredisi ön onayı ve müteahhit taksitlerinin takibi.
4. **Veri ürünü:** KKTC Emlak Endeksi. Bankalara, müteahhitlere ve basına raporlar.
5. **Araç ortaklığı:** galerimplus ile takas ve değerleme entegrasyonu.
6. **Başka pazarlar:** Aynı yapı, yabancıya mülk satılan başka küçük pazarlara taşınabilir (ör. Karadağ, Gürcistan, Türkiye kıyıları). Platformun başka şirketlere lisanslanması da bir seçenek.

---

## 9. Açık konular
- Hisse oranı (%40 veya %50) ve aylık kâr payı ödemesinin hukuki yapısı (muhasebeci ve avukat)
- adakey.app / adakey.io alan adlarının satın alınması ve marka tescili (adakey.com kayıtlı)
- Şirketin hangi ülkede kurulacağı
- İlk 5 müteahhitten niyet mektubu
