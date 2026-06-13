from src.tools.retriever import retrieve


def batting_tool(query):

    docs = retrieve(
        f"batting stats {query}",
        k=3
    )

    return docs