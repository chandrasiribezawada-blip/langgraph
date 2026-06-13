from src.tools.retriever import retrieve


def bowling_tool(query):

    docs = retrieve(
        f"bowling stats {query}",
        k=3
    )

    return docs