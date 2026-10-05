import os
import fitz  # PyMuPDF
from chunker import chunk_text
from store import store_chunks

DATA_DIR = "data"

def read_pdf(file_path):
    """
    Extracts text from a PDF file using PyMuPDF.
    """
    doc = fitz.open(file_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def main():
    if not os.path.exists(DATA_DIR):
        print(f"Directory '{DATA_DIR}' does not exist.")
        return
        
    files = [f for f in os.listdir(DATA_DIR) if f.endswith(".pdf")]
    
    if not files:
        print(f"No PDF files found in '{DATA_DIR}'. Please add a document.pdf.")
        return
        
    for file in files:
        file_path = os.path.join(DATA_DIR, file)
        print(f"Reading {file_path}...")
        
        # 1. Read PDF
        text = read_pdf(file_path)
        print(f"Extracted {len(text)} characters.")
        
        # 2. Chunk text
        chunks = chunk_text(text, chunk_size=1000, overlap=100)
        print(f"Created {len(chunks)} chunks.")
        
        # 3. Store in DB
        store_chunks(chunks, source_name=file)
        
if __name__ == "__main__":
    main()
