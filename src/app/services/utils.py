import os
from pypdf import PdfReader

def get_path(fileName: str) -> str:
    base_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.abspath(os.path.join(base_dir, "..", "..", ".."))
    return os.path.join(project_root, "input", fileName)

def get_text_from_pdf(path: str) -> str:
    reader = PdfReader(path)
    text = ""
    for page in reader.pages:
        text += (page.extract_text() or "") + "\f"
    return text