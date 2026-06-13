from src.tools.batting_tool import batting_tool


def batting_node(state):

    docs = batting_tool(
        state["query"]
    )

    state["retrieved_docs"] = docs

    return state