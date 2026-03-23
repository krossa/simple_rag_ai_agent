import os
from app.services.utils import get_path
from app.handlers.pdf_handler import upload_pdf

_data_folder = "articles"

def load_data():
    path = get_path(_data_folder)

    files = os.listdir(path)

    for file in files:
        upload_pdf(os.path.join(_data_folder, file))

    print(f"Loaded {len(files)} files from {_data_folder}")