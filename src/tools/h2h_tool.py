from src.tools.retriever import retrieve

def h2h_tool(query):

    docs = retrieve(
        f"head to head {query}",
        k=3
    )

    return docs