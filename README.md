# 🏥 Yapay Zeka Destekli Ameliyat Onam Bilgi Asistanı

Bu proje, ameliyat öncesi **onam formlarını sade bir dille açıklamak** için geliştirilmiş bir yapay zeka destekli bilgi asistanıdır. Kullanıcıların anlayabileceği netlikte cevaplar üretmeyi amaçlar.

---

## 📌 Amaç

- Onam formlarındaki tıbbi terimlerin, hastalar tarafından kolayca anlaşılmasını sağlamak  
- Her ameliyat için özel hazırlanmış onam metinlerinden, kullanıcı sorusuna uygun olan bilgiyi çıkarmak  
- Kullanıcıya korkutmadan, sade ve dürüst bir açıklama sunmak

---

## 🔧 Kullanılan Teknolojiler

| Teknoloji        | Açıklama |
|------------------|----------|
| **FastAPI**      | Python tabanlı web framework (API oluşturmak için kullanıldı) |
| **Gemini 1.5 Flash** | Google'ın ücretsiz, güçlü dil modeli (model ile kullanıcı sorusuna cevap üretiliyor) |
| **Python 3.10+** | Tüm uygulama Python ile yazıldı |
| **dotenv**       | API anahtarlarını yönetmek için |
| **curl**         | API'yi test etmek için |

---

## 🧠 Teknik Mimari

### 🔹 Adım 1: Soru Alma
Kullanıcı bir soru sorar (örneğin:  
*"Bu ameliyat sonrası sertleşme sorunu yaşanır mı?"*)

### 🔹 Adım 2: Prompt Oluşturma
Soru ve ilgili onam formu bir araya getirilerek Gemini’ye verilecek “prompt” hazırlanır.

```text
Sen bir sağlık danışmanısın. Aşağıdaki onam formuna göre, hastanın sorusuna sade, açık ve korkutmadan cevap ver.

ONAM FORMU:
... (form bilgisi)

SORU:
... (kullanıcının sorusu)
