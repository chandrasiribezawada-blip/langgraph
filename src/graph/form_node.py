from src.tools.form_tool import form_tool

def form_node(state):

    state["retrieved_docs"] = form_tool(
        state["query"]
    )

    return state