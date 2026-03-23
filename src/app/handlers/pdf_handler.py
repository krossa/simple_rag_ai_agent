import os
from app.services.chunker import chunk_by_sentences
from app.services.embedder import get_embeddings
from app.services.vector_store import store_embeddings
from app.services.utils import get_path, get_text_from_pdf

def upload_pdf():
    file_name = input("Enter PDF name from input folder: ").strip()

    if not file_name.lower().endswith(".pdf"):
        file_name += ".pdf"

    path = get_path(file_name)

    if not os.path.isfile(path):
        print(f"[PDF] File not found: {path}")
        return   

    text = get_text_from_pdf(path)
    chunks = chunk_by_sentences(text)
    vectors = get_embeddings(chunks)
    store_embeddings(chunks, vectors, file_name)