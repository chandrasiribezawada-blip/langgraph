from src.ingestion.loader import load_pdf

docs = load_pdf("data/IPL_LangGraph_RAG_Dataset.pdf")

print(f"\nPages Loaded: {len(docs)}")

print("\nFirst Page Preview:\n")
print(docs[0].page_content[:1000])