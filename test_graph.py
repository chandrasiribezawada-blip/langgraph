from src.graph.graph_builder import graph

query = input("Ask a question: ")

result = graph.invoke(
    {
        "query": query,
        "route": "",
        "response": ""
    }
)

print("\nResponse:\n")
print(result["response"])