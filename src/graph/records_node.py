from src.tools.records_tool import records_tool


def records_node(state):

    docs = records_tool(
        state["query"]
    )

    state["retrieved_docs"] = docs

    return state