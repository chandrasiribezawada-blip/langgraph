from src.tools.web_search_tool import web_search

def web_node(state):

    query = state["query"]

    results = web_search(query)

    state["validated_context"] = results

    state["source"] = "web"

    return state