from src.tools.retriever import retrieve


def retriever_node(state):

    docs = retrieve(
        state["query"],
        k=3
    )

    print(f"\nRetrieved Chunks: {len(docs)}")

    state["retrieved_docs"] = docs

    return state