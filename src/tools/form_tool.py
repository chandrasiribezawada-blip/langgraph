from src.tools.retriever import retrieve

def form_tool(query):

    docs = retrieve(
        f"recent form last 5 matches {query}",
        k=3
    )

    return docs