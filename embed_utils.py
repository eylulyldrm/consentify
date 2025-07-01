import os
import PyPDF2
import textwrap
import google.generativeai as genai

def pdf_metnini_oku(pdf_path):

    with open(pdf_path, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        metin = ""
        for sayfa in reader.pages:
            sayfa_metni = sayfa.extract_text()
            if sayfa_metni:
                metin += sayfa_metni + "\n"
    return metin

def metni_embedding_uret(metin, api_key, max_chars=3500):
  
    genai.configure(api_key=api_key)

    parcalar = textwrap.wrap(metin, max_chars)
    tum_embeddingler = []

    for parca in parcalar:
        response = genai.embed_content(
            model="models/embedding-001",  
            content=parca,
            task_type="retrieval_document"
        )
        tum_embeddingler.append(response["embedding"])

    ortalama_embedding = [sum(x) / len(x) for x in zip(*tum_embeddingler)]
    return ortalama_embedding

def tum_pdfleri_embedding_yap(pdf_klasoru, api_key):

    pdf_icerikleri = []
    embeddings = []

    for dosya in os.listdir(pdf_klasoru):
        if dosya.endswith(".pdf"):
            dosya_yolu = os.path.join(pdf_klasoru, dosya)
            metin = pdf_metnini_oku(dosya_yolu)
            embedding = metni_embedding_uret(metin, api_key)
            pdf_icerikleri.append({"dosya": dosya, "metin": metin})
            embeddings.append(embedding)
            print(f" {dosya} için embedding üretildi.")

    return pdf_icerikleri, embeddings
