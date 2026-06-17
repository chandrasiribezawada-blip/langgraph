def route_query(state):

    query = state["query"].lower()

    if any(word in query for word in
           ["runs","kohli","rohit","batting"]):

        state["route"] = "batting"

    elif any(word in query for word in
             ["wickets","bowling","bumrah","chahal"]):

        state["route"] = "bowling"

    elif any(word in query for word in
             ["venue","pitch","stadium"]):

        state["route"] = "venue"

    elif any(word in query for word in
             ["head to head","vs"]):

        state["route"] = "h2h"

    elif any(word in query for word in
             ["trend","consistent","season"]):

        state["route"] = "trend"
    elif any(word in query for word in
        ["dream11", "fantasy", "captain", "vice captain"]):

        state["route"] = "dream11"
    
    elif any(word in query for word in
             ["form","dream11","captain"]):

        state["route"] = "form"

    elif any(word in query for word in
             ["record","highest","most"]):

        state["route"] = "records"
    
    else:

        state["route"] = "team"

    return state