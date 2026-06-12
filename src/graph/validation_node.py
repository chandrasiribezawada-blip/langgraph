def validation_node(state):

    docs = state["retrieved_docs"]

    if not docs:
        state["validated_context"] = ""
        state["confidence_score"] = 0.0
        return state

    state["validated_context"] = "\n\n".join(docs)

    # Temporary confidence score
    state["confidence_score"] = 0.9

    return state