from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS


def build_vectorstore(chunks):

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vector_db = FAISS.from_documents(
        documents=chunks,
        embedding=embeddings
    )

    vector_db.save_local("vectorstore/faiss_index")

    return vector_db