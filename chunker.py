def chunk_text(text: str, chunk_size: int = 1000, overlap: int = 100):
    """
    Simple manual chunking of text.
    Returns a list of string chunks.
    """
    chunks = []
    start = 0
    text_length = len(text)
    
    while start < text_length:
        end = min(start + chunk_size, text_length)
        chunks.append(text[start:end])
        if end == text_length:
            break
        start += chunk_size - overlap
        
    return chunks
