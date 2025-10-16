import fitz
from docx import Document
import os
import re

def extract_text_from_pdf(path: str) -> str:
    doc = fitz.open(path)
    text = []
    for page in doc:
        text.append(page.get_text("text"))
    return "\n".join(text)

def extract_text_from_docx(path: str) -> str:
    doc = Document(path)
    text = []
    for p in doc.paragraphs:
        if p.text.strip():
            text.append(p.text)
    return "\n".join(text)

def parse_resume(file_path: str) -> str:
    ext = os.path.splitext(file_path)[1].lower()
    if ext == ".pdf":
        text = extract_text_from_pdf(file_path)
    elif ext in [".docx", ".doc"]:
        text = extract_text_from_docx(file_path)
    else:
        raise ValueError("Unsupported file format. Use PDF or DOCX.")
    return text