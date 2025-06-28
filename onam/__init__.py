from pathlib import Path
from PyPDF2 import PdfReader

def tum_formlari_yukle(klasor_adi):
    pdf_klasoru = Path(__file__).resolve().parent.parent / klasor_adi
    formlar = []

    for pdf_yolu in pdf_klasoru.glob("*.pdf"):
        try:
            reader = PdfReader(str(pdf_yolu))
            metin = ""
            for sayfa in reader.pages:
                metin += sayfa.extract_text() or ""
            formlar.append({
                "dosya_adi": pdf_yolu.name,
                "icerik": metin.strip()
            })
        except Exception as e:
            print(f"Hata: {pdf_yolu.name} okunamadı. {e}")
    return formlar
