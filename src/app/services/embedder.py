from sentence_transformers import SentenceTransformer
import numpy as np
from typing import List

_model = SentenceTransformer("all-MiniLM-L6-v2")
_batch_size = 32

def get_embeddings(chunks: List[str]) -> np.ndarray:
    if not chunks:
        return []

    embeddings = _model.encode(
        chunks,
        batch_size=_batch_size,
        normalize_embeddings=True,
        convert_to_numpy=True)

    return embeddings.astype(np.float32)