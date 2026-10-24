# research.md — KKTC Yapay Zeka Destekli Emlak Platformu

> Tarih: 24 Ekim 2026 · Durum: **Taslak v1**. Bulgular bu tarihte herkese açık kaynaklardan toplandı.
> Etiketler: **[Doğrulandı]** = kaynakta görüldü · **[Varsayım]** = tahmin, yöntemi yazılı · **[Açık]** = doğrulanamadı, saha araştırması gerekiyor.

---

## 0. Yönetici Özeti (yatırımcı sunumuna girecek)

1. **evlek.app düşündüğümüz kadar büyük bir rakip değil.** Tek kişinin kendi parasıyla kurduğu bir proje (bootstrapped). Yaklaşık **931 aktif ilanı** var ve bunların %84'ü Girne'de. iOS uygulamasında **henüz hiç puan yok**, web'den ödeme alınamıyor. Ama ürünü ve SEO'su çok iyi: 5 dil, fiyat endeksi, hesaplayıcılar, MCP sunucusu. **Bizi asıl zorlayacak olan ilan (arz) hacmi.** O tarafta 101evler ve HangiEv (yaklaşık 16 bin satılık ilan beyan ediyor) var, bir de Facebook grupları ve Instagram emlakçıları. **[Doğrulandı]**
2. **galerimplus'un formülü taşınabilir.** Formül şu: ilanları toplu içe aktararak hızla arz oluşturmak, şehir/fiyat/özellik kombinasyonlarıyla yüzlerce otomatik SEO sayfası üretmek (pSEO), "Araç Arıyorum" gibi alıcının talep yayınladığı ters ilan, takas sayfaları, AI asistan (Kirpi) ve sigorta/servis pazaryeri (Auto360). Emlakta bunun karşılıkları: "Ev Arıyorum" talep ilanı, "Ev360" hizmet pazaryeri, bölge × bütçe × oda tipi sayfaları. **[Doğrulandı]**
3. **Globale açılmanın en büyük riski hukuki ve itibari.** Kıbrıs Cumhuriyeti, kuzeyde Rum mülkünün **reklamını yapanları** bile yargılıyor. 2026'da bir Ukraynalı reklam yaptığı için suçunu kabul etti, Macar emlakçılar hapis cezası aldı, İsrailli bir müteahhide 5 yıl hapis verildi. Bu yüzden **tapu türünü filtrelemek ürünün zorunlu bir parçası.** Aynı zamanda pazarlamada da kullanılabilir: "yalnızca güvenli tapulu ilanlar". **[Doğrulandı]**
4. **Önerdiğimiz çekirdek değer önerisi:** (a) KKTC'nin en çok **doğrulanmış ve tapu türü etiketli** ilanını toplamak, (b) yabancı alıcı için **uzaktan alım hizmeti**: video tur, avukat ağı, izin süreci takibi, (c) emlakçıya **"bir kez gir, her yerde yayınla"** otomasyonu: 5 dile çeviri ve Instagram/Facebook'a otomatik paylaşım. Emlakçıyı ikna edecek olan c maddesi.
5. **Süre:** MVP'nin yayına çıkması **4–5 ay** sürer (kodu AI yazar, 1 yazılımcı denetler). İlk ücretli paketler **6.–9. ayda** gelir. "KKTC'nin en büyüğü" demek için gereken ilan hacmi ve trafik **12–18 ayda** gerçekçi. **[Varsayım]**
6. **Bütçe (12 ay):** Minimum ≈ **£100 bin**, Dengeli ≈ **£190 bin**, Agresif ≈ **£400 bin**. Gerçekçi başabaş noktası **18–30. ay** arasında. Detay §9'da. **[Varsayım]**

---

## 1. KKTC Pazar Analizi

### 1.1 Mevzuat (yabancı alıcı)
- **11 Mayıs 2026'da yürürlüğe giren yasa gücünde kararname (63/2026)** yabancıların mülk edinimini yeniden düzenledi. **[Doğrulandı]**
  - Bakanlar Kurulu izni hâlâ şart. Bir yabancı en fazla şunlardan birini alabiliyor: ≤1.338 m² arsa üzerinde 1 konut, **3 daire** ya da ≤3.300 m² arsa üzerinde 1 müstakil ev. Site projelerinde 2 villa.
  - İmara açık alandaki bir konut projesinin **en fazla %80'i** yabancıya satılabiliyor.
  - Yatırımcı şirketlerin KKTC'deki bir bankada **en az €10 milyon** bulundurması gerekiyor.
  - Vekâletname ve "trust" sözleşmesiyle kuralları dolanmaya ek denetim getirildi.
- İzin kararları sık çıkıyor: Ekim 2026'da tek kararda **297 kişiye**, yaklaşık 5 hafta önce **557 kişiye** izin verildi. İzin sayısı satış sayısına eşit değil. **[Doğrulandı]**
- **Fırsat:** Kurallar sık değişiyor ve kaynaklar birbiriyle çelişiyor. **Güncel ve güvenilir bir "yabancı alım rehberi"** gerçek bir boşluk. Yalnız evlek bunu kısmen yapıyor (`foreign_buyer_roadmap` aracı).

### 1.2 Tapu türleri ve uluslararası risk
- Tapu türleri Türk koçanı, eşdeğer koçan, tahsis ve 1974 öncesi Rum adına kayıtlı tapu. Uluslararası risk düzeyleri birbirinden çok farklı. **[Doğrulandı]**
- **Kıbrıs Cumhuriyeti'nin yargılamaları:**
  - Simon Aykut (İsrailli müteahhit): 5 yıl hapis (Ekim 2025).
  - Ukraynalı bir kişi: Rum mülkünün **reklamını yapmaktan** suçunu kabul etti (Nisan 2026).
  - Macar emlakçılar: hapis cezası (Mayıs 2025).
  - Lefkoniko projesindeki 4 Türk vatandaşı: Avrupa tutuklama emri.
- UK Dışişleri de mülkiyet uyuşmazlıkları için uyarı yayınlıyor. **[Doğrulandı]**
- **Ürüne etkisi:**
  - Tapu türü alanı zorunlu olmalı.
  - Rum tapulu ilanlar ya hiç alınmamalı ya da açıkça ayrıştırılmalı.
  - AB'de yapılacak reklamlar ve AB'ye seyahat eden ekip üyeleri için avukat görüşü alınmalı (**[Açık]**, bütçeye eklendi).

### 1.3 Mevcut platformlar

| Platform | Ölçek | Güçlü yön | Zayıf yön |
|---|---|---|---|
| **101evler** | KKTC'nin en eski ve büyük portalı olduğunu söylüyor. Bot erişimine kapalı (403), sayısı alınamadı. | Marka bilinirliği, emlakçı alışkanlığı | Eski UX, AI yok **[Varsayım]** |
| **HangiEv** | ~16.139 satılık + 3.681 kiralık (kendi beyanı) | Hacim | Kopya ilan oranı bilinmiyor **[Açık]** |
| **evlek.app** | 931 onaylı ilan (695'i satılık Girne) | AI, 5 dil, SEO, doğrulama | Arz az, Girne dışı zayıf, uygulama yeni |
| **Northern Cyprus Property Portal** | 2024'te kuruldu, ev sahibi odaklı | Sahibinden ilanlar | Küçük |
| **Zoopla Overseas / globallistings** | Küçük (globallistings'te ~118 ilan) | UK trafiği | KKTC ile Rum kesimi karışık |
| **Facebook grupları / Instagram emlakçıları** | Çok büyük ama dağınık | Alışkanlık, ücretsiz | Arama yok, güven yok |

**Ana bulgular**
- Pazar parçalı. "En büyük" iddiası her yerde var ama kimse doğrulamıyor. **Bağımsız ve doğrulanmış ilan sayacı** başlı başına bir pazarlama malzemesi olur.
- Girne'de medyan satış fiyatı **£185.000** (evlek endeksi, Ekim 2026, 393 ilan).
- KTEB üye sayısı, aktif emlak ofisi sayısı ve yıllık tapu devri istatistiği bulunamadı. **[Açık]** Saha araştırmasında toplanacak (Tapu Dairesi, KTEB).

---

## 2. evlek.app Derin Analizi

**Teknoloji (public koddan):** Next.js 16, React 19, Supabase, Vercel, Mapbox, Gemini, OpenAI Vision. Herkese açık bir MCP sunucusu var (16 araç: `search_listings`, `get_price_index`, `get_yield_estimate`, `assess_title_risk`, `foreign_buyer_roadmap`, `payment_plan`…). Ürünü tek kurucu geliştiriyor (Onur Dokuzoğlu).

**SEO yapısı (sitemap analizi):**
- Her dilde ayrı, yerelleştirilmiş URL'ler var: `/for-sale/kyrenia`, `/kaufen/kyrenia`, `/prodazha/kireniya`, `/tr/satilik`.
- Bölge, içerik ve dizin sitemap'leri 5 dilde ayrı ayrı tutuluyor.
- Araçlar: yatırım, vergi ve kredi hesaplayıcı, kur dönüştürücü, yabancı edinim aracı, fiyat endeksi, 240 mahalle endeksi, 56 mahalle profili, üniversite rehberleri, blog.

**Paketler:**
- Solo Mini **£39,99/ay** (40 ilan, yılda 1.000 AI kredisi)
- Solo Pro **£49,99/ay** (100 ilan, 1.500 kredi)
- Ek AI kredisi: £20 / £50 / £100
- Kurumsal: teklifle
- 14 gün deneme
- Web'den **ödeme henüz açık değil.**

| ✅ Başarılı yönler | ❌ Zayıf yönler | 🎯 Bize bıraktığı boşluk |
|---|---|---|
| 5 dil, yerelleştirilmiş SEO URL'leri | **931 ilan.** Arz çok sınırlı, %84'ü Girne | Mağusa, İskele, Lefkoşa ve Güzelyurt'ta arz |
| Sadece onaylı ofis + KYC + ilan incelemesi | Sadece ofisler ilan verebiliyor (sahibinden yok) | Kontrollü sahibinden ilan + proje (müteahhit) ilanı |
| Cümleyle arama, fotoğraf analizi | AI staging yok ("Nano Banana" iddiası sitede doğrulanmadı) | Etiketli AI staging (sanal döşeme) |
| Fiyat endeksi, hesaplayıcılar | iOS'ta 0 puan, Android yeni. Topluluk ve sosyal etki zayıf **[Varsayım]** | Instagram/TikTok içerik motoru, insan yüzü olan bir marka |
| MCP: ChatGPT/Claude içinde görünür | Ödeme altyapısı açılmadı. Gelir yok ya da çok düşük **[Varsayım]** | Emlakçı otomasyonu ve lead (müşteri adayı) yönetimi |
| Hukuki dürüstlük ("tapu garantisi vermiyoruz") | Tek kişi, ölçeklenmesi zor | 4 kişilik ekip + saha satış |

> Not: "evlek.app Nano Banana ile boş evleri dolu gösteriyor" bilgisi evlek'in kendi AI sayfasında geçmiyor. Sayfada tam tersine "fotoğraf piksellerine dokunulmaz" yazıyor. Bu bilgiyi nereden duyduğunuzu teyit edelim; uygulamada farklı olabilir. **[Açık]**

---

## 3. galerimplus.com Analizi → Emlağa Uyarlama

**Teknoloji (public HTML ve JS bundle'larından):**
- Next.js (ISR, Cloudflare arkasında), Supabase. Görseller `r2.galerimplus.com` üzerinden Supabase Storage'dan sunuluyor.
- Apple ile giriş var.
- API rotaları: `/api/analytics/{behavior,search,app-download}`, **`/api/meta-capi`** (sunucu taraflı Meta Conversions API; reklam takibinin olgun olduğunu gösteriyor), `/api/exchange-rates`, `/api/flash-deals`, `/api/favorites`, `/api/user/search-history`, `/api/upload/r2`, `/api/rental/status`.

**Arz stratejisi:**
- Sitemap'te yaklaşık **7.350 ilan URL'si** var. Sitede "3.500+ aktif ilan, 120+ galeri" yazıyor.
- Görsellerin bir kısmı `migrated/` klasöründe ve kaynak olarak **kktcarabam.com** URL'leri görünüyor. Yani başlangıçta **başka bir platformdan ilan taşımışlar.** Hızlı bir başlangıç taktiği ama izin alınmazsa hukuki ve itibari risk taşıyor. evlek bunu "kaynak izni kaydı" tutarak yapıyor.

**Sayfa ve özellik haritası** (statik sitemap'te ~60 sayfa ve pSEO sayfaları):

| galerimplus | Ne yapıyor | Emlak karşılığı | Öncelik |
|---|---|---|---|
| `/ikinci-el/{şehir}/{özellik}`, `/ikinci-el/10000-sterlin` | Programatik SEO (pSEO): yüzlerce otomatik sayfa | `/satilik/girne/2+1`, `/satilik/iskele/100000-sterlin-alti`, 5 dilde | **MVP** |
| `/arac-ariyorum` | Alıcı talep yayınlar, galeriler teklif verir | **"Ev Arıyorum"**: talebe emlakçılar teklif verir | **MVP** (benzersiz, ucuz) |
| `/takas`, `/takas/{ilan}-takas` | Takasa açık ilanların ayrı SEO sayfaları | "Takasa açık" etiketi + filtre + sayfa | MVP-lite |
| `/taksitli-araclar` | Taksitli ilanlar | **Ödeme planlı projeler** (müteahhit taksiti) | **MVP** |
| `/kirpi` (Kirpi Max) | AI danışman, değerleme, eşleştirme | Çok dilli AI emlak danışmanı | MVP-lite |
| `/arabam-kac-para`, `/arac-degerleme` | Değerleme | "Evim kaç para?" → **satıcı lead'i** (emlakçıya satılır) | V2 |
| `/fiyati-dusen`, `/acil-satilik`, `/flash-firsatlar` | Fırsat sayfaları | Aynısı | MVP |
| `/pazar-raporu`, `/kktc-araba-fiyatlari` | Veri içeriği | Aylık KKTC emlak raporu (PR'da kullanılır) | V1.5 |
| `/vitrin-ilanlari`, doping | Öne çıkarma | Vitrin ve doping | V1.5 (gelir) |
| `/galeri-basvuru` (kurumsal üyelik, WhatsApp ile satış) | Bayi kazanımı | Ofis başvurusu + WhatsApp ile onboarding | MVP |
| `/auto360`, `/sigorta`, `/sigorta/acente-basvuru` | Servis ve sigorta pazaryeri | **"Ev360"**: avukat, taşınma, tadilat, konut sigortası, mülk yönetimi | V2 (komisyon geliri) |
| `/ihaleler` | Canlı ihale | Bankadan ve icradan satılık mülkler | V3 / araştırılacak |
| `/karsilastir`, `/en/cars`, `sitemap-ru` | Karşılaştırma, çok dil | Aynısı | MVP |
| `/sarj-istasyonlari`, `/parcalar` | Yan trafik sayfaları | Okul, hastane ve plaj haritaları, mahalle rehberi | V1.5 |

**Ana bulgular**
- galerimplus'un ürün kadar güçlü bir **büyüme makinesi** var: pSEO, Meta CAPI, fırsat sayfaları, ters ilan.
- Paket fiyatlarını yayınlamıyor, satışı WhatsApp üzerinden insanla yapıyor. KKTC'de satış hâlâ **ilişkiyle** yürüyor.
- Not: galerimplus'un robots.txt dosyası AI tarayıcılarını engelliyor. İncelemeyi, herkese açık yalnızca birkaç sayfa ve sitemap ile sınırlı tuttum.

---

## 4. Global Örnekler

| Platform | Gelir modeli | Arzı nasıl topladı | KKTC'ye taşınacak fikir |
|---|---|---|---|
| **Rightmove (UK)** | Ofis aboneliği. FY2025 gelir £425M, ofis başına aylık gelir (ARPA) **£1.530**, %90+ elde tutma | UK ofislerine ilk dönemde ücretsiz/ucuz, sonra paket yükseltme | Kademeli paket + ek özellik satışı (upsell). Elde tutmak her şeyden önemli |
| **Zillow (US)** | Premier Agent: lead satışı | Herkese açık veri + Zestimate trafiği | "Evim kaç para?" değerlemesi ile trafik ve satıcı lead'i |
| **Property Finder / Bayut (BAE)** | Abonelik + kredi bazlı öne çıkarma | Ofis zorunluluğu + doğrulama | **Doğrulanmış ilan rozeti** (TruCheck benzeri), yabancı yatırımcı odağı **[Açık: güncel veri alınamadı]** |
| **Idealista (ES)** | Abonelik + ilan ücreti | Sahibinden + ofis | Yabancı alıcıya çok dilli içerik |
| **sahibinden / hepsiemlak (TR)** | Doping, vitrin, kurumsal paket | Ücretsiz ilan ile hacim | Doping kataloğu, "acil", "fiyatı düştü" |
| **Matterport** | 3D tur SaaS | — | 3D/video tur: uzaktan alıcı için kritik |
| **Compass** | Emlakçıya SaaS + CRM | Emlakçıya araç vererek | Emlakçı paneli = CRM |

**Taşınabilecek en değerli 10 fikir:** (1) doğrulanmış ilan rozeti, (2) değerleme ile satıcı lead'i, (3) kredi bazlı öne çıkarma, (4) pSEO, (5) ters ilan, (6) 3D/video tur, (7) kayıtlı arama alarmı (e-posta/push), (8) emlakçı CRM'i, (9) aylık pazar raporu ile PR, (10) hizmet pazaryeri.

---

## 5. Değer Önerisi — "Müşteriyi Gerçekten Getirecek Şey"

Puanlar 1–5 arası: Fayda / Ayrışma (evlek'e karşı) / Uygulanabilirlik.

| Aday | F | A | U | Not |
|---|---|---|---|---|
| **En çok doğrulanmış ilan + tapu türü rozeti** | 5 | 4 | 3 | Ayrışma ilan hacminden gelir, teknolojiden değil |
| **Uzaktan alım hizmeti** (video tur, avukat ağı, izin süreci takibi) | 5 | 5 | 3 | Yabancı alıcının en büyük acısı. Müteahhitten referans geliri getirir |
| **Emlakçı otomasyonu** (bir kez gir, 5 dile çevir, IG/FB'ye otomatik paylaş) | 5 | 5 | 4 | Arzı çekecek özellik. GaleriPost gibi tek başına bir ürün |
| Proje (off-plan) takibi + müteahhit güven skoru | 4 | 5 | 3 | İskele/Long Beach yabancı alımları çoğunlukla projeden **[Varsayım]** |
| Çok dilli AI asistan | 4 | 2 | 5 | evlek'te zaten var. Olmazsa olmaz ama ayrıştırmaz |
| Fiyat endeksi / kira getirisi | 4 | 2 | 4 | evlek'te var. Biz "gerçek satış verisi" toplarsak ayrışır |
| AI staging | 3 | 3 | 5 | Ucuz, güzel bir upsell ama tek başına trafik getirmez |
| Öğrenci kiralama dikeyi | 4 | 3 | 4 | Yerel trafik ve sezonluk talep (üniversiteler) |

**Öneri:** Çekirdek değer önerisi **ilk üç satır**. AI asistan ve endeks "olmazsa olmaz" seviyesinde yapılsın, öne çıkan özellik olarak sunulmasın.

---

## 6. Emlakçı / Müteahhit İkna Stratejisi

**Teklif önerisi (Kurucu Ortak Ofis programı):**
- İlk **50 ofise** 6 ay ücretsiz Pro + ömür boyu %30 indirim + "Kurucu Ortak" rozeti.
- **Ücretsiz içe aktarma:** Mevcut ilanlarını (Excel, kendi siteleri, XML) biz taşırız, **yazılı izinle**.
- **Ücretsiz içerik:** Her ofise ayda 1 profesyonel video tur. Pazarlama ekibi çeker, bizim Instagram'da yayınlanır, ofis etiketlenir.
- **Lead garantisi** yerine şeffaf **lead raporu**: kaç kişi baktı, kaç kişi aradı.
- **Müteahhitler için:** Proje sayfası + ödeme planı + inşaat ilerleme albümü. Ücretlendirme proje başına ya da satış başına referans ücreti (**[Açık]**, sözleşmeyle).

**Saha mülakatı soruları (ilk 30 ofis):**
1. Şu an hangi platformlarda, kaç ilanınız var? Aylık ne ödüyorsunuz?
2. Müşterilerinizin yüzde kaçı yabancı, hangi ülkelerden?
3. Lead'leriniz en çok nereden geliyor (FB, IG, 101evler, referans)?
4. Bir ilanı kaç platforma, kaç dilde, ne kadar sürede giriyorsunuz?
5. En çok zaman kaybettiren iş hangisi?
6. Sahte, eski veya kopya ilan sizi ne kadar etkiliyor?
7. Bir platforma ayda en fazla ne ödersiniz? Ne olursa öderdiniz?
8. Instagram/TikTok içeriğini kim üretiyor?
9. Yabancı müşteride en çok hangi aşamada satış düşüyor?
10. CRM kullanıyor musunuz? Müşteri takibini nasıl yapıyorsunuz?
11. Video tur yapıyor musunuz? Yapmıyorsanız neden?
12. Tapu türünü ilanda belirtmek sizin için sorun olur mu?
13. Müteahhitlerle çalışma modeliniz ve komisyonunuz nedir?
14. evlek veya galerimplus'u duydunuz mu? Ne düşünüyorsunuz?
15. Ücretsiz deneme sunsak hemen ilan girer misiniz? Engel olan ne?

**Bankalar:**
- "3 ay ücretsiz banner" erken dönemde değersiz kalır, çünkü banka trafik görmeden ilgilenmez.
- Daha iyisi: **kredi hesaplayıcı + "bu bankadan ön onay al" butonu** ile lead başına ücret ya da sabit sponsorluk. Bu 6. aydan sonra trafik verisiyle konuşulmalı.
- KKTC'de yabancıya sterlin konut kredisi verildiği doğrulanamadı. Merkez Bankası'nın "İlk Evim" paketi TL cinsinden, en fazla %80 kredi ve 120 ay vadeli. **[Açık]** Bankalarla görüşülecek. Yabancı alıcı için gerçek "taksit" seçeneği büyük olasılıkla **müteahhit ödeme planı**.

---

## 7. Trafik Edinme (düşük bütçe öncelikli)

| Kanal | Maliyet | Etki | Öncelik | Not |
|---|---|---|---|---|
| **pSEO + çok dilli SEO** | Düşük (geliştirme) | Yüksek, 3–6 ayda | 1 | evlek bu konuda önde. Hız ve hacimle yakalanır |
| **Instagram/TikTok Reels** (ev turları, "£150k'ya Girne'de ne alınır") | Düşük (2 pazarlamacı) | Yüksek | 1 | Ofislerle ortak içerik, arzı da büyütür |
| **YouTube uzun turlar** (EN/DE/RU) | Orta | Yüksek (yabancı) | 2 | Uzaktan alıcının güveni için |
| **Facebook expat grupları** | ~0 | Orta | 1 | Spam değil, değer paylaşımı (rehber, rapor) |
| **Google Ads** ("north cyprus property" UK/DE) | Emlak CPC ort. ~$2,8–3,2 (US, 2025–26). Yurt dışı emlak muhtemelen daha yüksek **[Varsayım]** | Hızlı, ölçülebilir | 2 | Ayda £1–3k ile test |
| **Meta Ads** (lead form, retargeting) | CPL **[Açık]**. Test edilecek | Yüksek | 2 | Meta CAPI kurulumu (galerimplus gibi). Emlak "özel reklam kategorisi" kuralları ülke bazında kontrol edilecek |
| **Influencer / expat içerik üreticileri** | Orta | Orta–Yüksek | 2 | Performansa dayalı (referans kodu) |
| **PR: aylık KKTC emlak raporu** | Düşük | Orta | 2 | Kıbrıs basını ve TR basını |
| **Ortaklıklar** (üniversite, göç danışmanı, havayolu) | Düşük | Orta | 3 | |
| **AI asistanlarda görünürlük** (MCP, llms.txt) | Düşük | Yükseliyor | 3 | evlek'in yaptığı. Ucuz bir kopya hamlesi |

**Hedef ülke sırası (öneri):**
1. **TR** (en kolay)
2. **UK** (en büyük expat havuzu)
3. **DE**
4. **RU/UA ve Orta Asya**
5. **Orta Doğu (AR)**

İsrail ve Rum tarafıyla bağlantılı pazarlarda §1.2'deki risk nedeniyle dikkatli olunmalı.

**İlk 90 gün içerik ritmi (2 pazarlamacı + kurucu):** Haftada 5 Reels, 1 YouTube turu, 2 blog/pSEO içeriği, 1 e-bülten. Ayda 1 "KKTC Emlak Raporu".

---

## 8. Geliştirme Süresi ve Teknik Kapsam

**Önerilen yığın:**
- **Web:** Next.js + Supabase (Postgres, Auth, Storage) + Vercel veya Cloudflare. İki rakip de bunu kullanıyor ve AI ile hızlı kodlanıyor.
- **Mobil:** Expo (React Native), kodun bir kısmı web ile ortak.
- **Harita:** Mapbox.
- **AI:** Gemini / Claude / OpenAI. Görsel tarafında AI staging için Gemini görsel modeli (Nano Banana) veya benzeri.
- **E-posta:** Resend veya Brevo. **Ödeme:** iyzico (TR/KKTC) + Stripe (yurt dışı). KKTC'de kullanılabilirliği **[Açık]**, şirket yapısına göre değişir.

| Faz | Kapsam | İyimser | Gerçekçi | Kötümser |
|---|---|---|---|---|
| 0 | Saha mülakatları, PRD, tasarım, marka | 3 hf | 4–5 hf | 8 hf |
| 1 — MVP Web | İlan, arama/filtre, harita, ofis paneli, ilan içe aktarma, WhatsApp/form lead, kayıtlı arama + e-posta, TR/EN, pSEO, "Ev Arıyorum", tapu türü alanı, ödeme planlı projeler | 6 hf | 8–10 hf | 14 hf |
| 1b — Mobil | iOS + Android (Expo), push bildirim, mağaza onayı | 3 hf | 4–6 hf | 8 hf |
| 2 | Paketler, ödeme, doping/vitrin, otomasyon (IG/FB otomatik paylaşım, AI çeviri), RU/DE/AR, AI staging | 6 hf | 8–10 hf | 14 hf |
| 3 | Ev360, değerleme, takas eşleştirme, banka entegrasyonu, video tur | 8 hf | 12 hf | 20 hf |

**Toplam:** Herkese açık lansman (Faz 0 + 1 + 1b) **~4–5 ay**. Gelir özellikleri (Faz 2) **6.–8. ay**. **[Varsayım]**

Kodu AI'nın yazması süreyi kısaltır. Ama asıl darboğaz kod değil: **ilan toplama, mağaza onayı, hukuk ve içerik.**

**Aylık altyapı maliyeti:** Başlangıçta **£150–400**. 50 bin aylık aktif kullanıcıda (MAU) **£600–1.500** (AI görsel işleme dahil). **[Varsayım]**

---

## 9. Bütçe Modeli (12 ay, GBP) [Varsayım]

| Kalem | Minimum | Dengeli | Agresif |
|---|---|---|---|
| Ekip (4 kişi). Yazılımcı ~£2–3k, pazarlamacı ~£1,2–1,8k/ay; kurucu maaşsız ya da asgari | 60.000 | 78.000 | 108.000 (+freelance) |
| Altyapı, AI, mağaza hesapları, yazılım | 6.000 | 12.000 | 24.000 |
| Reklam (Google/Meta) | 18.000 (£1,5k/ay) | 60.000 (£5k/ay) | 180.000 (£15k/ay) |
| İçerik üretimi (video, drone, influencer) | 4.000 | 12.000 | 36.000 |
| Hukuk, şirket, muhasebe, AB riski için avukat görüşü | 5.000 | 8.000 | 15.000 |
| Etkinlik ve fuar (UK/DE emlak fuarları) | — | — | 5.000 |
| Beklenmeyen giderler (%10) | 9.300 | 17.000 | 37.000 |
| **Toplam** | **≈ £102.000** | **≈ £187.000** | **≈ £405.000** |

**Gelir projeksiyonu (Dengeli senaryo):**
- **Ofis paketleri:** £30 / £60 / £120 ayda (Pro/ProMax). Referans: evlek £39,99–49,99. Rightmove'un £1.530'luk ARPA'sı KKTC için gerçekçi değil.
- **12. ay hedefi:** 120 ücretli ofis × ort. £55 = **~£6,6k/ay** + doping/vitrin **~£2k/ay** + müteahhit proje paketleri (10 × £300) **~£3k/ay** ≈ **£11–12k/ay MRR**.
- Bu durumda Dengeli senaryonun aylık yakımı (~£15k) **18.–24. ayda** karşılanır.
- **En büyük gelir kaldıracı:** Yabancı alımlarda müteahhitten alınan **satış başına referans ücreti**. Tek bir satış binlerce sterlin edebilir **[Varsayım, sözleşmeyle doğrulanacak]**.

**Yatırımcıya öneri:** Dengeli senaryo + 18 aylık pist ≈ **£250–280 bin**. Para dilimler halinde verilsin, her dilim §10'daki go/no-go noktalarına bağlansın.

---

## 10. Milestone'lar ve KPI'lar (4 kişi)

| Ay | Milestone | KPI |
|---|---|---|
| 0–1 | 30 ofisle mülakat, PRD, marka, IG/TikTok/YouTube hesapları açılır, içerik başlar | 30 mülakat, 15 "evet" diyen ofis, 1.000 takipçi |
| 1–4 | MVP web + mobil, Kurucu Ortak Ofis programı, ilan içe aktarma | **≥1.500 aktif ilan** (evlek'i geçer), ≥40 ofis |
| 4 | Soft launch (TR/EN) | 5k MAU, 150 lead/ay |
| 5–6 | Herkese açık lansman + RU/DE, ilk reklam testleri | 20k MAU, 500 lead/ay, IG 10k |
| 6–9 | Paketler ve doping açılır, otomasyon modülü, AI staging | 50 ücretli ofis, £4k MRR |
| 9–12 | Yurt dışı kampanyaları (UK/DE), Ev360 pilotu, banka görüşmeleri | 50k MAU, yurt dışı trafik %35+, 120 ücretli ofis |
| 12–18 | "KKTC'nin en büyüğü" iddiası: bağımsız ilan sayacı, aylık rapor | 5.000+ ilan, 100k MAU |

**Go/no-go noktaları:**
- **4. ay:** 1.500 ilan / 40 ofise ulaşılmadıysa reklam bütçesi açılmaz, sorun arz tarafındadır.
- **9. ay:** 50 ücretli ofise ulaşılmadıysa paket fiyatı ve değer önerisi yeniden kurgulanır.

---

## 11. Riskler

| Risk | Olasılık | Etki | Önlem |
|---|---|---|---|
| Rum mülkü reklamı nedeniyle yargılama / AB'de tutuklama riski | Orta | Çok yüksek | Tapu türü zorunlu, Rum tapulu ilan alınmaz, avukat görüşü, AB'de reklam politikası |
| Arz toplanamaz (emlakçı direnci, 101evler alışkanlığı) | Yüksek | Yüksek | Kurucu Ortak programı, ücretsiz içe aktarma, otomasyon, saha satış |
| İzinsiz ilan aktarımıyla telif ve itibar kaybı | Orta | Orta | Yalnızca yazılı izinle içe aktarma, kaynak kaydı |
| AI staging yanıltıcı bulunur | Orta | Orta | "AI ile döşendi" etiketi + orijinal fotoğraf her zaman gösterilir (California AB 723 ve NAR kuralları referans) |
| evlek kopyalar ya da 101evler AI ekler | Yüksek | Orta | Avantajımız ilan hacmi, saha ilişkisi ve içerik. Bunlar kolay kopyalanmaz |
| Mevzuat değişir (yabancı kotası %80, 3 daire sınırı) | Yüksek | Orta | Rehber sürekli güncellenir, avukat ortaklığı |
| Ödeme altyapısı KKTC'de sorun çıkarır | Orta | Orta | TR veya UK şirketi üzerinden tahsilat, havale |
| AI maliyeti kontrolden çıkar | Düşük | Düşük | Kredi sistemi (evlek modeli) |

---

## 12. Kurucunun 9 Fikri — Değerlendirme Matrisi

| # | Fikir | Karar | Gerekçe | Efor | Gelir etkisi |
|---|---|---|---|---|---|
| 1 | AI staging (boş evi dolu göster) | **V2** (6.–8. ay) | Ucuz ve iyi bir upsell, ama trafik getirmez. Etiket + orijinal fotoğraf **zorunlu** | Düşük | Orta (AI kredisi satışı) |
| 2 | Takas | **MVP-lite / tam sistem: Yapma** | Ev↔ev takasında likidite çok düşük. Sadece "takasa açık" etiketi + SEO sayfası (galerimplus modeli) | Çok düşük | Düşük |
| 3 | Taksitli ev | **MVP** (ödeme planlı projeler olarak) | Yabancıya banka kredisi belirsiz. Asıl taksit müteahhitten geliyor. Güçlü filtre + hesaplayıcı | Düşük | Yüksek (müteahhit paketleri) |
| 4 | Öne çıkarma (ilan/proje) | **V1.5** (6. ay) | Ana gelir kalemi ama trafik olmadan satılamaz | Orta | Yüksek |
| 5 | Banka banner'ı, 3 ay ücretsiz | **Değiştir → V2** | Trafik yokken değersiz. Kredi hesaplayıcı + ön onay lead'i modeline dönüştür | Düşük | Orta |
| 6 | E-posta | **MVP** | Kayıtlı arama alarmları en önemli geri getirme mekanizması | Düşük | Dolaylı |
| 7 | Müşteri ↔ emlakçı birebir iletişim | **MVP** | WhatsApp + form + lead raporu. Uygulama içi chat V2'de | Düşük | Dolaylı (paketin gerekçesi) |
| 8 | Emlakçı otomasyonu | **MVP'ye çek (lite)** | **Arzı çekecek özellik.** 5 dile çeviri + IG/FB otomatik paylaşım | Orta | Yüksek |
| 9 | Pro / ProMax, aylık/yıllık | **V1.5** | İlk 6 ay Kurucu Ortak programıyla ücretsiz. Yıllık paket ~2 ay indirimli | Düşük | Yüksek |

**Benim eklediğim fikirler:** "Ev Arıyorum" ters ilanı (MVP), tapu türü rozeti (MVP), pSEO (MVP), uzaktan alım hizmeti (V1.5), Ev360 hizmet pazaryeri (V2), "Evim kaç para?" satıcı lead'i (V2), aylık pazar raporu (V1.5), MCP/AI görünürlüğü (V2).

---

## 13. Açık Sorular (kurucu cevaplayacak)

1. Şirket nerede kurulacak (KKTC / TR / UK)? Bu ödeme altyapısını ve AB riskini belirler.
2. İlk hedef ülke UK mi, TR mi?
3. Yatırımcıdan istenen tutar ve vazgeçilecek hisse oranı ne?
4. Kurucu maaş alacak mı?
5. Rum tapulu ilanları tamamen reddediyor muyuz?
6. Sahibinden (bireysel) ilan alacak mıyız, yoksa yalnızca ofis ve müteahhit mi?
7. "evlek Nano Banana kullanıyor" bilgisinin kaynağı ne?
8. Marka adı ve domain belirlendi mi?

## 14. PRD İskeleti (araştırma onaylanınca doldurulacak)

1. Amaç ve başarı metrikleri · 2. Personalar (yerel alıcı, yabancı alıcı, öğrenci, ofis, müteahhit) · 3. Değer önerisi · 4. Kapsam: MVP / V1.5 / V2 / V3 · 5. Kullanıcı akışları · 6. Fonksiyonel gereksinimler (modül modül) · 7. AI özellikleri ve sınırları · 8. Veri modeli · 9. Doğrulama ve moderasyon politikası · 10. Monetizasyon ve paketler · 11. Çok dil ve SEO · 12. Hukuk, KVKK/GDPR, tapu politikası · 13. Analitik ve olay takibi · 14. Teknik mimari · 15. Yol haritası · 16. Riskler.

---

## Kaynaklar (erişim: 24.10.2026)

- evlek: [evlek.app](https://evlek.app) · [Fiyatlar](https://evlek.app/pricing) · [Evlek AI](https://evlek.app/evlek-ai) · [App Store](https://apps.apple.com/app/id6760562764) · [GitHub](https://github.com/Evlek) · [MCP](https://glama.ai/mcp/connectors/app.evlek/mcp-server) · sitemap.xml analizi
- galerimplus: [galerimplus.com](https://www.galerimplus.com) · [Takas](https://www.galerimplus.com/takas) · [Galeri başvuru](https://www.galerimplus.com/galeri-basvuru) · [Kirpi](https://www.galerimplus.com/kirpi) · sitemap ve public JS bundle analizi
- Rakipler: [101evler](https://www.101evler.com/north-cyprus/properties-for-sale) · [HangiEv](https://www.hangiev.com/home) · [NC Property Portal](https://www.accessnewswire.com/newsroom/en/real-estate/northern-cyprus-property-portal-set-to-revolutionize-real-estate-market-927403) · [Zoopla Overseas](https://www.zoopla.co.uk/overseas/property/cyprus/northern-cyprus/) · [Globallistings](https://www.globallistings.com/northern-cyprus-property-search)
- Mevzuat: [TKTO](https://www.turkkibristicaretodasi.org/kktcde-yabancilara-tasinmaz-duzenlemesi-konut-arazi-ve-yatirim-sartlari-degisti/) · [Kıbrıs Manşet](https://www.kibrismanset.com/yabancilarin-tasinmaz-ediniminde-yeni-duzenleme-konut-projelerinde-yuzde-80-siniri) · [Yenidüzen](https://www.yeniduzen.com/yabancilarin-tasinmaz-mal-sahibi-olmasina-iliskin-yapilan-yeni-duzenleme-neleri-icer-25553yy.htm) · [Bugün Kıbrıs – 297 izin](https://bugunkibris.com/bakanlar-kurulu-bir-gunde-297-yabanciya-tasinmaz-satin-alma-izni-verdi/) · [Kıbrıs Türk – 557 izin](https://www.kibristurk.com/bakanlar-kurulundan-557-yabanciya-tasinmaz-mal-satin-alma-izni) · [Dovec – 63/2026](https://www.dovecgroup.com/en/blog/north-cyprus-property-law-2026-new-rules) · [Gars – tapu rehberi](https://www.garsconsulting.com/blog/buying-property-north-cyprus-title-deed-residency-2026)
- Hukuki risk: [Cyprus Mail – Ukraynalı, Nisan 2026](https://cyprus-mail.com/2026/04/20/ukrainian-national-pleads-guilty-to-advertising-greek-cypriot-owned-property-in-north) · [Cyprus Mail – tutuklama emirleri](https://cyprus-mail.com/2025/05/13/arrest-warrants-issued-for-developers-on-greek-cypriot-land-in-north) · [New Arab – Aykut](https://www.newarab.com/news/israeli-sentenced-over-illegal-development-northern-cyprus) · [Yahoo – Macarlar](https://www.yahoo.com/news/cyprus-court-jails-hungarians-brokering-125325038.html)
- Finansman: [KKTC MB – İlk Evim](https://www.kktcmerkezbankasi.org/sites/default/files/IV.%20%C4%B0lk%20Evim%20Konut%20Kredisi%20Paketine%20%C4%B0li%C5%9Fkin%20Usul%20ve%20Esaslar_0.pdf) · [Halkbank KKTC Konut](https://www.halkbank.com.tr/tr/bireysel/krediler/kktc-ye-ozel-krediler/kktc-konut.html)
- Global: [Rightmove RNS 27.02.26](https://plc.rightmove.co.uk/content/uploads/2026/02/Rightmove-RNS-27.02.26.pdf) · [The Negotiator](https://thenegotiator.co.uk/news/marketing-news/rightmove-revenue-up-9-as-agent-spending-rises/)
- AI staging kuralları: [The Close](https://theclose.com/news-ai-listing-photo-disclosure/) · [NorthstarMLS](https://northstarmls.com/insights/guidelines-for-virtual-staging-and-ai-enhanced-listing-photos/)
- Reklam maliyeti: [LocaliQ](https://localiq.com/blog/real-estate-search-advertising-benchmarks/) · [Search Engine Land](https://searchengineland.com/google-ads-costs-keep-rising-but-conversion-rates-improved-in-2025-477927)
