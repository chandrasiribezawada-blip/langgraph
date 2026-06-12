from src.ingestion.loader import load_pdf
from src.ingestion.chunker import create_chunks

docs = load_pdf("data/IPL_LangGraph_RAG_Dataset.pdf")

chunks = create_chunks(docs)

print(f"\nTotal Chunks: {len(chunks)}")

print("\nSample Chunk:\n")
print(chunks[0].page_content)