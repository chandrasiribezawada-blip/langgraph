def validation_node(state):

    docs = state["retrieved_docs"]

    if not docs:
        state["validated_context"] = ""
        state["confidence_score"] = 0.0
        return state

    state["validated_context"] = "\n\n".join(docs)

    # Temporary confidence score
    context = state["retrieved_docs"]

    if len(str(context)) < 100:

        state["confidence_score"] = 0.1

    else:

        state["confidence_score"] = 0.9

    return state