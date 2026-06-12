from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

db = FAISS.load_local(
    "vectorstore/faiss_index",
    embeddings,
    allow_dangerous_deserialization=True
)

query = "What is the purpose of this IPL dataset?"

results = db.similarity_search(query, k=3)

for i, doc in enumerate(results, start=1):
    print(f"\nResult {i}")
    print("=" * 50)
    print(doc.page_content)