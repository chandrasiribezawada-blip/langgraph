from src.tools.h2h_tool import h2h_tool

def h2h_node(state):

    state["retrieved_docs"] = h2h_tool(
        state["query"]
    )

    return state