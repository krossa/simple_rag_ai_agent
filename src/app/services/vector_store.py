import chromadb
from chromadb.config import Settings
from functools import lru_cache
from typing import List
import numpy as np
from pathlib import Path
from app.services.embedder import get_embeddings

@lru_cache(maxsize=1)
def get_chroma_client():
    return chromadb.PersistentClient(
        path=str("chroma_db")
    )

@lru_cache(maxsize=1)
def get_collection():
    client = get_chroma_client()
    return client.get_or_create_collection(name="documents")

def store_embeddings(
    chunks: List[str],
    embeddings: np.ndarray,
    source: str
):    
    collection = get_collection()

    if len(chunks) != len(embeddings):
        raise ValueError("Chunks and embeddings must match")

    ids = [f"{source}_{i}" for i in range(len(chunks))]

    metadata = [
        {"source": source, "chunk_id": i}
        for i in range(len(chunks))
    ]

    collection.add(
        ids=ids,
        embeddings=embeddings.tolist(),
        documents=chunks,
        metadatas=metadata
    )

def query(query: str, n_results: int = 3) -> List[str]:
    collection = get_collection()

    query_embedding = get_embeddings([query])[0].tolist()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=n_results
    )

    return {
        "documents": results["documents"][0],
        "metadatas": results["metadatas"][0]
    }