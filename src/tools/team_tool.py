from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS


from src.tools.retriever import retrieve

def team_tool(query):
    return retrieve(query)