import numpy as np

def cosine_similarity(vec1, vec2):
   
    vec1 = np.array(vec1)
    vec2 = np.array(vec2)
    return np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))

def en_yakin_pdfyi_bul(soru_embedding, pdf_embedding_list, pdf_icerikleri):

    max_sim = -1
    secilen_index = -1
    for i, pdf_emb in enumerate(pdf_embedding_list):
        sim = cosine_similarity(soru_embedding, pdf_emb)
        if sim > max_sim:
            max_sim = sim
            secilen_index = i
    return pdf_icerikleri[secilen_index]
