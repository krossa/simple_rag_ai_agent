import re

def chunk_by_sentences(text, max_words=300):
    sentences = split_sentences(text)
    
    chunks = []
    current = []
    count = 0

    for sentence in sentences:
        words = sentence.split()
        
        if count + len(words) > max_words:
            chunks.append(" ".join(current))
            current = []
            count = 0
        
        current.append(sentence)
        count += len(words)

    if current:
        chunks.append(" ".join(current))

    return chunks

def split_sentences(text: str):
    return re.split(r'(?<=[.!?]) +', text)