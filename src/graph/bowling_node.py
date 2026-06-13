from src.tools.bowling_tool import bowling_tool


def bowling_node(state):

    docs = bowling_tool(
        state["query"]
    )

    state["retrieved_docs"] = docs

    return state