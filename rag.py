import requests
from store import get_db_collection

OLLAMA_API_URL = "http://localhost:11434/api/generate" #Local LLM -Ollama model-URL
MODEL_NAME = "llama3.2:3b"

def generate_answer(prompt):
    """
    Sends a prompt to the local Ollama API and returns the generated answer.
    """
    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False
    }
    
    try:
        response = requests.post(OLLAMA_API_URL, json=payload)
        response.raise_for_status()
        result = response.json()
        return result.get("response", "")
    except requests.exceptions.RequestException as e:
        print(f"Error communicating with Ollama: {e}")
        return "Failed to get response from Ollama. Ensure it is running locally."

def main():
    collection = get_db_collection()
    
    if collection.count() == 0:
        print("The database is empty. Please run ingest.py first.")
        return
        
    print("Welcome to Simple Local RAG Q&A")
    print("Type 'quit' or 'exit' to stop.")
    print("-" * 50)
    
    while True:
        try:
            question = input("\nQuestion: ")
        except (KeyboardInterrupt, EOFError):
            print("\nExiting...")
            break
            
        if question.lower() in ['quit', 'exit', 'q']:
            break
            
        if not question.strip():
            continue
            
        print("\nSearching for context...")
        # Retrieve top 7 relevant chunks
        results = collection.query(
            query_texts=[question],
            n_results=7
        )
        
        if not results['documents'][0]:
            print("No relevant context found.")
            continue
            
        retrieved_chunks = results['documents'][0]
        context = "\n\n---\n\n".join(retrieved_chunks)
        
        print("\nRetrieved context:")
        for i, chunk in enumerate(retrieved_chunks):
            # Print a snippet of each chunk for demonstration
            snippet = chunk[:150].replace('\n', ' ') + "..." if len(chunk) > 150 else chunk.replace('\n', ' ')
            print(f"[{i+1}] {snippet}")
        
        prompt = f"""Use the following context to answer the question. If the answer is not in the context, just say you don't know based on the context.

Context:
{context}

Question:
{question}

Answer:"""

        print("\nAnswer:")
        answer = generate_answer(prompt)
        print(answer)
        print("-" * 50)

if __name__ == "__main__":
    main()
