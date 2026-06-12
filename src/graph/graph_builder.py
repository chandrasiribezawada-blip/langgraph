from langgraph.graph import StateGraph, END

from src.graph.state import IPLState
from src.graph.router import router_node
from src.tools.team_tool import team_tool
from src.tools.player_tool import player_tool
from src.tools.records_tool import records_tool


def team_node(state):
    state["response"] = team_tool(state["query"])
    return state


def player_node(state):
    state["response"] = player_tool(state["query"])
    return state


def records_node(state):
    state["response"] = records_tool(state["query"])
    return state


builder = StateGraph(IPLState)

builder.add_node("router", router_node)
builder.add_node("team", team_node)
builder.add_node("player", player_node)
builder.add_node("records", records_node)

builder.set_entry_point("router")


def route_decision(state):
    return state["route"]


builder.add_conditional_edges(
    "router",
    route_decision,
    {
        "team": "team",
        "player": "player",
        "records": "records"
    }
)

builder.add_edge("team", END)
builder.add_edge("player", END)
builder.add_edge("records", END)

graph = builder.compile()