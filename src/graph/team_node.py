from src.tools.team_tool import team_tool


def team_node(state):

    docs = team_tool(
        state["query"]
    )

    state["retrieved_docs"] = docs

    return state