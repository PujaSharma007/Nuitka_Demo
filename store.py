import chromadb
from chromadb.utils import embedding_functions

CHROMA_PATH = "chroma_db"
COLLECTION_NAME = "rag_collection"

def get_db_collection():
    """
    Initializes and returns the ChromaDB persistent collection.
    """
    client = chromadb.PersistentClient(path=CHROMA_PATH)
    # Using a simple default embedding function
    embedding_func = embedding_functions.DefaultEmbeddingFunction()
    
    collection = client.get_or_create_collection(
        name=COLLECTION_NAME,
        embedding_function=embedding_func
    )
    return collection

def store_chunks(chunks, source_name="document"):
    """
    Stores chunks with metadata into ChromaDB.
    """
    collection = get_db_collection()
    
    documents = []
    metadatas = []
    ids = []
    
    for i, chunk in enumerate(chunks):
        documents.append(chunk)
        metadatas.append({"source": source_name, "chunk_index": i})
        ids.append(f"{source_name}_chunk_{i}")
        
    collection.add(
        documents=documents,
        metadatas=metadatas,
        ids=ids
    )
    print(f"Stored {len(chunks)} chunks in ChromaDB.")
