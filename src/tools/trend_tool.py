from src.tools.retriever import retrieve

def trend_tool(query):

    docs = retrieve(
        f"season performance trend {query}",
        k=3
    )

    return docs