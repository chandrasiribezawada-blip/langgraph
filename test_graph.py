from src.graph.graph_builder import graph

query = input(
    "Ask a question: "
)

result = graph.invoke(
    {
        "query": query,
        "route": "",
        "retrieved_docs": [],
        "validated_context": "",
        "confidence_score": 0.0,
        "response": ""
    }
)

print("\nRoute:")
print(result["route"])

print("\nConfidence:")
print(result["confidence_score"])

print("\nResponse:")
print(result["response"])