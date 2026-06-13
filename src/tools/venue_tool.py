from src.tools.retriever import retrieve


def venue_tool(query):

    docs = retrieve(
    f"Venue Report {query}",
    k=5
)

    return docs