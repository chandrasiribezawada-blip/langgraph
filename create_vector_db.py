from src.ingestion.loader import load_pdf
from src.ingestion.chunker import create_chunks
from src.ingestion.vector_db import build_vectorstore

print("Loading PDF...")

docs = load_pdf("data/IPL_LangGraph_RAG_Dataset.pdf")

print("Creating Chunks...")

chunks = create_chunks(docs)

print(f"Chunks Created: {len(chunks)}")

print("Building FAISS Index...")

build_vectorstore(chunks)

print("FAISS Index Created Successfully!")