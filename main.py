import sys
import ingest
import rag

def main():
    print("=== Main RAG Application ===")
    print("1. Ingest Data (Reads PDFs from data/ and stores in chroma_db/)")
    print("2. Run RAG Q&A (Queries existing chroma_db/)")
    print("3. Exit")
    
    while True:
        choice = input("\nSelect an option (1, 2, or 3): ").strip()
        
        if choice == '1':
            print("\n--- Starting Ingestion ---")
            ingest.main()
            print("--- Ingestion Complete ---\n")
        elif choice == '2':
            print("\n--- Starting Q&A ---")
            rag.main()
        elif choice == '3' or choice.lower() in ['q', 'quit', 'exit']:
            print("Exiting application...")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nExiting application...")
        sys.exit(0)
