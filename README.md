#  Yapay Zeka Destekli Onam Bilgi Asistanı

Bu proje, hastalar için **onam formlarını sade bir dille açıklamak** için geliştirilmiş bir yapay zeka destekli bilgi asistanıdır. Kullanıcıların anlayabileceği netlikte cevaplar üretmeyi amaçlar.

---


### NOT

Bu proje bir sağlık danışmanı yerine geçmez. Amaç, hastaların tıbbi belgeleri daha iyi anlamasını desteklemektir. Geliştirme süreci devam etmektedir.

---

## Amaç

- Her ameliyat için özel hazırlanmış onam metinlerinden, kullanıcı sorusuna uygun olan bilgiyi çıkarmak ve Onam formlarındaki tıbbi terimlerin, hastalar tarafından kolayca anlaşılmasını sağlamak 

---

## 


 **FastAPI**      | Python tabanlı web framework (API oluşturmak için kullanıldı) |
 **Gemini 1.5 Flash** | Google'ın ücretsiz dil modeli (model ile kullanıcı sorusuna cevap üretiliyor) |
 **Python 3.10+** | Tüm uygulama Python ile yazıldı |
 **dotenv**       | API anahtarlarını yönetmek için |
 **curl**         | API'yi test etmek için |

---

## 

###   Soru Alma
Kullanıcı bir soru sorar (örneğin:  
*"Bu ameliyat sonrası enfeksiyon sorunu yaşanır mı?"*)

###  Prompt Oluşturma
Soru ve ilgili onam formu bir araya getirilerek Gemini’ye verilecek “prompt” hazırlanır.

```text
Sen bir sağlık danışmanısın. Aşağıdaki onam formuna göre, hastanın sorusuna sade, açık ve korkutmadan cevap ver.

ONAM FORMU:
... (form bilgisi)

SORU:
... (kullanıcının sorusu)
---

![image](https://github.com/user-attachments/assets/419a6ab8-cc59-4b99-a447-33df43d2a667)



###Expected Point Completion within Sprint:
Bu sprintte tamamlanması hedeflenen toplam puan: 200 Point

### Point Completion Logic:
Proje genelinde toplam 1000 puanlık iş yükü planlandı.

İlk sprintte fikir geliştirme, tasarım ve planlama aşamaları için 200 puanlık hedef belirlendi.

İkinci sprintte geliştirme ve API entegrasyonu için 400 puan hedefleniyor.

Üçüncü sprintte kalan geliştirme, test ve entegrasyon işleri için 400 puanlık hedef planlandı.


### Daily Scrum:
Jira üzerinden günlük görev takibi yapılacak.

Haberleşme ve günlük durum raporları WhatsApp grubundan paylaşılacak.

### Sprint Toplantılarına katılanlar;
Mehmet Lafcı,  Ömer Faruk Asker, Sena Abasız,Eylül Durdane Yıldırım
