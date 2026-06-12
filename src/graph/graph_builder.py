from langgraph.graph import StateGraph, END

from src.graph.state import IPLState
from src.graph.router import router_node

from src.graph.retriever_node import retriever_node
from src.graph.validation_node import validation_node
from src.graph.response_node import response_node


builder = StateGraph(IPLState)

builder.add_node(
    "router",
    router_node
)

builder.add_node(
    "retriever",
    retriever_node
)

builder.add_node(
    "validator",
    validation_node
)

builder.add_node(
    "response",
    response_node
)

builder.set_entry_point("router")

builder.add_edge(
    "router",
    "retriever"
)

builder.add_edge(
    "retriever",
    "validator"
)

builder.add_edge(
    "validator",
    "response"
)

builder.add_edge(
    "response",
    END
)

graph = builder.compile()