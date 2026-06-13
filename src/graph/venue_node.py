from src.tools.venue_tool import venue_tool


def venue_node(state):

    docs = venue_tool(
        state["query"]
    )

    state["retrieved_docs"] = docs

    return state