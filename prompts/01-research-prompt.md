# Araştırma Promptu — KKTC Yapay Zeka Destekli Emlak Platformu

> Bu promptu yeni bir Claude oturumuna (web araştırması açık) olduğu gibi yapıştırın.
> Çıktı: `research.md` (önce) → `prd.md` (araştırma bittikten sonra) → yatırımcı sunumu taslağı.

---

## ROL

Sen; emlak teknolojisi (PropTech) pazarları, iki taraflı marketplace büyütme, mobil uygulama ürün yönetimi ve uluslararası dijital pazarlama konusunda deneyimli bir **strateji danışmanı ve ürün araştırmacısısın**. Görevin, kurucunun fikirlerini **onaylamak değil, test etmek**. Her iddiayı kaynakla destekle; kaynak bulamazsan "varsayım" olarak etiketle. Kurucunun fikirlerinden zayıf olanları açıkça söyle ve gerekçesini yaz.

## BAĞLAM

- **Pazar:** Kuzey Kıbrıs Türk Cumhuriyeti (KKTC). Hedef: KKTC'nin yapay zeka destekli en büyük emlak platformu olmak, ardından yurt dışından (TR, UK, DE, RU/UA, İran, Orta Doğu, Orta Asya, İskandinavya vb.) ev almak/kiralamak isteyenleri çekmek.
- **Ana rakip:** evlek.app
- **Referans ürün:** galerimplus.com ve mobil uygulaması (araç galerisi platformu). Bu ürünün iş modeli, özellik seti ve UX akışları emlak dikeyine uyarlanacak.
- **Ekip (toplam 4 kişi):** Kurucu (dijital pazarlama), 1 yazılımcı (kod denetleyici / reviewer — kodun büyük kısmını yapay zeka yazacak), 2 pazarlamacı.
- **Finansman:** Bir yatırımcıya (tanıdık) sunum yapılacak; bu araştırma o sunumun temeli.
- **Kanallar:** Instagram ve diğer sosyal medya hesapları açılacak.
- **Bütçe hassasiyeti:** Pazarlama bütçesi ayrılacak ama düşük maliyetle trafik çekmek öncelik.

## KURUCUNUN FİKİRLERİ (DOĞRULANACAK — ONAYLANMIŞ DEĞİL)

Her biri için: *Pazarda örneği var mı? Kullanıcı gerçekten istiyor mu? KKTC'de yasal/pratik engel var mı? Gelir potansiyeli? Geliştirme maliyeti? MVP'ye girmeli mi, sonraya mı kalmalı, yoksa hiç yapılmamalı mı?*

1. **AI sanal mobilya (virtual staging)** — boş evleri dolu gösterme (evlek.app'in "Nano Banana" ile yaptığı gibi). Etik/yanıltıcı ilan riski ve "AI ile düzenlendi" etiketi gerekliliği de değerlendirilsin.
2. **Takas sistemi** (ev ↔ ev, ev ↔ araç, ev ↔ arsa).
3. **Taksitli ev seçenekleri** (müteahhit taksiti, banka kredisi, yabancılar için finansman).
4. **Öne çıkarma sistemi** — ilanı öne çıkarma, projeyi öne çıkarma.
5. **Bankalarla banner anlaşması** — ilk 3 ay ücretsiz.
6. **E-posta pazarlama** altyapısı (alıcıya ve emlakçıya).
7. **Müşteri ↔ emlakçı birebir iletişim** (uygulama içi mesaj, WhatsApp, arama, video tur).
8. **Emlakçılara otomasyon hizmeti** (CRM, otomatik ilan paylaşımı, lead takibi, AI ilan metni).
9. **Paketler:** Ücretsiz / Pro / ProMax — aylık ve yıllık.

## ARAŞTIRMA GÖREVLERİ

### 1. KKTC Pazar Analizi
- Pazar büyüklüğü: yıllık satış/kiralama işlem sayısı, aktif ilan sayısı, emlak ofisi ve müteahhit sayısı (tahmini aralıklarla, kaynaklı).
- Alıcı profilleri: yerel, TC vatandaşı, yabancı (ülke bazında), öğrenci kiralama pazarı (üniversiteler), yatırımcı.
- **KKTC'ye özgü kritik konular** (yabancı alıcının en büyük korkusu burası):
  - Tapu türleri: Türk koçanı, eşdeğer koçan, tahsis, Rum malı — farkları ve riskleri.
  - Yabancıların mülk alımı: Bakanlar Kurulu izni, süreç, süre, sınırlamalar.
  - Döviz, vergi, harç, avukat zorunluluğu.
  - Uluslararası pazarlamada hukuki/itibari riskler (ör. Rum tarafının açtığı davalar, Orams davası emsali, AB/UK'de reklam kısıtları, Meta/Google reklam politikalarında bölge ve emlak kategorisi kısıtları).
- Mevcut platformlar: evlek.app, 101evler, Kıbrıs'ta sahibinden.com kullanımı, Facebook grupları, Instagram emlakçıları, yabancı odaklı portallar (ör. uluslararası listeleme siteleri). Her biri için trafik tahmini (SimilarWeb vb. açık veriler), ilan sayısı, gelir modeli.

### 2. evlek.app Derin Analizi
- Özellik envanteri (web + iOS + Android), fiyatlandırma/paketler, emlakçı tarafı paneli.
- App Store / Google Play puanları, indirme tahmini, **kullanıcı yorumlarının tematik analizi** (en sık şikayetler, en çok övülenler).
- Sosyal medya: takipçi sayıları, içerik türleri, etkileşim oranları, reklam kütüphanesindeki (Meta Ad Library) aktif reklamlar.
- SEO: hangi anahtar kelimelerde görünüyor, hangi dillerde içerik var.
- **Çıktı:** Başarılı yönler / başarısız yönler / bizim için açık bırakılan boşluklar tablosu.

### 3. galerimplus.com Analizi ve Emlağa Uyarlama
- Yalnızca **herkese açık yüzeylerden** (web sitesi, mağaza sayfaları, ekran görüntüleri, uygulamanın kullanıcı olarak gezilmesi) özellik, akış ve iş modeli analizi yap. Kaynak koduna, API'lerine veya korunan içeriğine erişmeye çalışma; tasarım ve metinleri kopyalama — amaç *ilham ve fonksiyonel eşleştirme*.
- Ekran/akış haritası: onboarding, arama-filtre, ilan detayı, ilan verme, galeri (bayi) paneli, paketler, ödeme, bildirimler.
- **Eşleştirme tablosu:** galerimplus özelliği → emlak karşılığı → KKTC'de anlamlı mı? → öncelik (MVP / V2 / hiç).

### 4. Global Örneklerle Karşılaştırma
Şu platformları incele ve **KKTC'ye taşınabilecek en değerli 10 fikri** çıkar:
- Zillow (Zestimate, 3D tur, kredi entegrasyonu), Redfin, Realtor.com
- Rightmove, Zoopla (UK — emlakçı abonelik modeli)
- Idealista (İspanya — yabancı alıcı odaklı), Immobilienscout24 (DE)
- Property Finder, Bayut (BAE/Orta Doğu — doğrulanmış ilan "TruCheck", yabancı yatırımcı odağı)
- sahibinden.com, hepsiemlak, Emlakjet (TR)
- Opendoor (iBuying), Compass (emlakçı SaaS), Matterport
- AI odaklı yeni oyuncular (sohbetle ev arama, AI değerleme, AI staging)

Her biri için: gelir modeli, emlakçıyı nasıl ikna ettiği (soğuk başlangıç problemi), en ayırt edici özellik.

### 5. "Müşteriyi Gerçekten Buraya Getirecek Şey" — Değer Önerisi
Sadece ilan listesi yetmez. Aşağıdaki adayları kullanıcı faydası, rakiplerden ayrışma ve uygulanabilirlik açısından puanla (1–5), en güçlü 2–3 tanesini **çekirdek değer önerisi** olarak öner:
- Doğrulanmış ilan + tapu türü rozeti (sahte/eski ilan sorununu çözer)
- Yabancı alıcı rehberi: adım adım satın alma süreci, maliyet hesaplayıcı, avukat/izin süreci takibi
- Çok dilli AI asistan ("Girne'de denize 1 km, 150 bin £ altı, kira getirisi en yüksek 2+1")
- AI değerleme / bölgesel fiyat endeksi ve kira getirisi hesaplayıcı (KKTC'de şeffaf fiyat verisi yok)
- Video/sanal tur, uzaktan alım (görmeden alım güveni)
- Proje (off-plan) takibi: inşaat ilerleme fotoğrafları, müteahhit güven puanı
- Öğrenci kiralama dikeyi
- Diğer bulduğun fikirler

### 6. Emlakçı/Müteahhit İkna Stratejisi (Arz Tarafı — Soğuk Başlangıç)
- Global platformlar ilk ilanları nasıl topladı? (ücretsiz dönem, toplu ilan aktarımı/XML-feed, saha satış ekibi, ücretsiz fotoğraf çekimi, lead garantisi)
- KKTC'deki emlakçıların bugünkü acıları neler? (Mülakat soruları taslağı hazırla — 10–15 soru.)
- Teklif paketi önerisi: ilk X ay ücretsiz, kurucu ortak emlakçı programı, performansa dayalı ücretlendirme vb.
- Bankalarla banner/işbirliği: KKTC'deki bankaların yabancıya kredi verme durumu, işbirliği modeli, "3 ay ücretsiz" fikrinin mantıklı olup olmadığı.

### 7. Trafik Edinme Stratejisi (Düşük Bütçe Öncelikli)
- Kanal bazında tahmini maliyet ve etki: SEO (çok dilli içerik, bölge/proje sayfaları), Instagram/TikTok Reels, YouTube ev turları, influencer/expat içerik üreticileri, Facebook expat grupları, Google Ads, Meta Ads, e-posta, ortaklıklar (havayolu, otel, üniversite, göçmenlik danışmanları), PR.
- Hedef ülkelere göre kanal önceliği.
- Emlak kategorisinde tahmini CPC / CPL / CPM aralıkları (TR, UK, DE, Orta Doğu için ayrı).
- İlk 90 günlük içerik ve büyüme planı (2 pazarlamacı + kurucu kapasitesine göre).

### 8. Ürün Geliştirme Süresi ve Teknik Kapsam
- Ekip varsayımı: kodun çoğunu AI yazıyor, 1 yazılımcı review/denetim yapıyor.
- Fazlar ve gerçekçi süre aralıkları (iyimser / gerçekçi / kötümser):
  - Faz 0: Araştırma + PRD + tasarım
  - Faz 1 (MVP): Web + iOS + Android, ilan, arama/filtre, emlakçı paneli, mesajlaşma, temel AI özelliği
  - Faz 2: Paketler/ödeme, öne çıkarma, otomasyon, çok dil
  - Faz 3: Takas, finansman, gelişmiş AI
- Önerilen teknoloji yığını (ör. React Native/Expo veya Flutter, backend seçenekleri, harita, görsel AI API'leri) ve aylık altyapı maliyeti tahmini.
- App Store/Play Store yayın süreçleri, KVKK/GDPR uyumu, ödeme altyapısının KKTC'de kullanılabilirliği (Stripe, iyzico vb. — KKTC desteği kontrol edilsin).

### 9. Bütçe Modeli
Üç senaryo hazırla (Minimum / Dengeli / Agresif), 12 ve 18 aylık:
- Geliştirme ve altyapı (sunucu, AI API, harita, SMS/e-posta, mağaza hesapları)
- Ekip maliyeti (4 kişi — KKTC/TR maaş aralıkları)
- Pazarlama (aylık reklam, içerik üretimi, influencer, etkinlik/fuar)
- Hukuk, şirket kuruluşu, muhasebe
- Beklenmeyen giderler (%10–15)
- **Gelir projeksiyonu:** paket fiyat önerileri (KKTC emlakçısının ödeme gücüne göre), öne çıkarma gelirleri, banner gelirleri; başabaş noktası tahmini.

### 10. Pazarlama Süresi ve Milestone'lar
4 kişilik ekip için ay ay yol haritası (lansman öncesi + sonrası):
- Örnek KPI'lar: aktif ilan sayısı, kayıtlı emlakçı sayısı, MAU, yurt dışı trafik oranı, lead/ay, ücretli abone sayısı.
- "KKTC'nin en büyüğü" olmak için hangi metriklerde evlek.app'i geçmek gerekir ve bu ne kadar sürer (tahmini).
- Yatırımcıya gösterilecek go/no-go kontrol noktaları.

### 11. Riskler
Hukuki (tapu, uluslararası tanınmama, reklam kısıtları), rekabet (evlek.app'in tepkisi, sahibinden'in girişi), operasyonel (sahte ilan, emlakçı direnci), teknik (AI maliyeti, AI staging'in yanıltıcılık riski), finansal. Her risk için olasılık / etki / azaltma önlemi.

## ÇIKTI FORMATI

1. **`research.md`** — yukarıdaki 11 başlık; her bölüm sonunda "Ana bulgular" (3–5 madde) ve "Kaynaklar" (link + erişim tarihi). Varsayımlar ve doğrulanmış veriler ayrı işaretlensin.
2. **Fikir Değerlendirme Matrisi** — kurucunun 9 fikri: Karar (MVP / V2 / V3 / Yapma), gerekçe, tahmini efor, gelir etkisi.
3. **Yönetici Özeti** (1 sayfa) — yatırımcı sunumuna doğrudan girecek.
4. **Açık Sorular** — kurucunun cevaplaması gereken ve araştırmayla çözülemeyen sorular (ör. hedef ilk ülke, bütçe tavanı, yatırımcıdan beklenen tutar).
5. `prd.md`'yi **henüz yazma**; araştırma onaylandıktan sonra ayrı bir adımda yazılacak. Sadece PRD için önerilen başlık iskeletini ver.

## KURALLAR

- Türkçe yaz; tablo kullanmaktan çekinme.
- Rakam verirken aralık ve kaynak ver; tahmin ise yöntemini açıkla.
- Kurucunun fikirlerine katılmıyorsan açıkça söyle — "evet efendimcilik" istemiyoruz.
- Güncel veriler kullan (son 12 ay öncelikli); eski veriyi tarihle belirt.
