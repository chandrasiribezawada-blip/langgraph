from src.tools.trend_tool import trend_tool

def trend_node(state):

    state["retrieved_docs"] = trend_tool(
        state["query"]
    )

    return state