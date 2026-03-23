import os
from app.services.chunker import chunk_by_sentences
from app.services.transcriber import transcribe_video
from app.services.embedder import get_embeddings
from app.services.utils import get_path
from app.services.vector_store import store_embeddings

def upload_video():
    file_name = input("Enter video name from input folder: ").strip()

    if not file_name.lower().endswith(".mp4"):
        file_name += ".mp4"

    path = get_path(file_name)

    if not os.path.isfile(path):
        print(f"[VIDEO] File not found: {path}")
        return
    
    text = transcribe_video(path)
    chunks = chunk_by_sentences(text)
    vectors = get_embeddings(chunks)
    store_embeddings(chunks, vectors, file_name)
