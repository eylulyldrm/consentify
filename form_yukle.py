
import os
import fitz  # PyMuPDF kütühanesi indirdim

def pdf_icerigini_oku(dosya_yolu):
    with fitz.open(dosya_yolu) as doc:
        metin = ""
        for sayfa in doc:
            metin += sayfa.get_text()
    return metin.strip()

def tum_formlari_yukle(klasor_yolu="onam"):
    formlar = []
    for dosya in os.listdir(klasor_yolu):
        if dosya.endswith(".pdf"):
            tam_yol = os.path.join(klasor_yolu, dosya)
            icerik = pdf_icerigini_oku(tam_yol)
            formlar.append({
                "dosya_adi": dosya,
                "icerik": icerik
            })
    return formlar
