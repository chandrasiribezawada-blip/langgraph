def router_node(state):

    query = state["query"].lower()

    if "team" in query or "mi" in query or "csk" in query:
        state["route"] = "team"

    elif "player" in query or "runs" in query:
        state["route"] = "player"

    elif "record" in query:
        state["route"] = "records"

    else:
        state["route"] = "team"

    return state