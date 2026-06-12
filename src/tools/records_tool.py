from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS


from src.tools.retriever import retrieve

def records_tool(query):
    return retrieve(query)