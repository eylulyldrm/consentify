from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
from pathlib import Path
import os
import traceback

import google.generativeai as genai
from embed_utils import tum_pdfleri_embedding_yap, pdf_metnini_oku, metni_embedding_uret
from similarity_utils import en_yakin_pdfyi_bul

env_path = Path(__file__).resolve().parent / ".env"
load_dotenv(dotenv_path=env_path)

api_key = os.getenv("GEMINI_API_KEY")
print("API key yüklendi mi:", bool(api_key))

app = FastAPI()

class Soru(BaseModel):
    soru: str
PDF_KLASOR = "./onam"  # Buraya  kendi PDF klasör yolumu yazmıştım

print("PDF embeddingleri hazırlanıyor...")
pdf_icerikleri, pdf_embeddings = tum_pdfleri_embedding_yap(PDF_KLASOR, api_key)
print(f"Toplam {len(pdf_icerikleri)} PDF embedding hazır.")

@app.post("/soru-sor")
async def soru_sor(soru: Soru):
    try:
        if not api_key:
            return {"hata": "API anahtarı eksik. .env dosyasını kontrol et."}

        genai.configure(api_key=api_key)
        model = genai.GenerativeModel("models/gemini-1.5-flash")

        soru_embedding = metni_embedding_uret(soru.soru, api_key)

    
        secilen_pdf = en_yakin_pdfyi_bul(soru_embedding, pdf_embeddings, pdf_icerikleri)

        
        prompt = f"""
Sen bir sağlık danışmanısın. Aşağıdaki ameliyat onam formuna göre, hastanın sorusuna sade, açık ve mantıklı cevap ver.

ONAM FORMU:
{secilen_pdf['metin']}

SORU:
{soru.soru}
"""

        chat = model.start_chat()
        yanit = chat.send_message(prompt)
        return {
            "cevap": yanit.text,
            "secili_dosya": secilen_pdf['dosya']
        }

    except Exception as e:
        print("❗ HATA:", str(e))
        traceback.print_exc()
        return {"hata": str(e)}

































'''from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
from pathlib import Path
import os
import google.generativeai as genai
import traceback

# .env dosyasını yükle
env_path = Path(__file__).resolve().parent / ".env"
load_dotenv(dotenv_path=env_path)

api_key = os.getenv("GEMINI_API_KEY")
print("API key yüklendi mi:", bool(api_key))

app = FastAPI()

class Soru(BaseModel):
    soru: str

onam_metni = """
Ameliyat Adı: Laparoskopik Radikal Prostatektomi
Amaç: Prostatta bulunan tümörü çıkarmak.
Riskler: İdrar kaçırma (%15-35), Sertleşme sorunu (%15-50), Enfeksiyon (%2-5), Rektum yaralanması (%0.5-1)
İyileşme: Hastanede 3-5 gün kalış, 1 hafta sonra dikiş alınır
Alternatif: Açık cerrahi, radyoterapi
"""

@app.post("/soru-sor")
async def soru_sor(soru: Soru):
    try:
        if not api_key:
            return {"hata": "API anahtarı eksik. .env dosyasını kontrol et."}

        genai.configure(api_key=api_key)
        model = genai.GenerativeModel("models/gemini-1.5-flash")


        chat = model.start_chat()
        prompt = f"""
Sen bir sağlık danışmanısın. Aşağıdaki onam formuna göre, hastanın sorusuna sade, açık ve korkutmadan cevap ver.

ONAM FORMU:
{onam_metni}

SORU:
{soru.soru}
"""
        yanit = chat.send_message(prompt)
        return {"cevap": yanit.text}

    except Exception as e:
        print("❗ HATA:", str(e))
        traceback.print_exc()
        return {"hata": str(e)}

@app.get("/models")
async def list_models():
    try:
        genai.configure(api_key=api_key)
        models = genai.list_models()
        # .to_dict() kaldırıldı çünkü Model objesinde bu metod yok
        return {"models": [model.name for model in models]}
    except Exception as e:
        print("❗ HATA:", str(e))
        traceback.print_exc()
        return {"hata": str(e) '''

