from langgraph.graph import StateGraph, END

from src.graph.state import IPLState
from src.graph.web_node import web_node
from src.graph.router import route_query
from src.graph.dream11_node import dream11_node
from src.graph.team_node import team_node
from src.graph.batting_node import batting_node
from src.graph.bowling_node import bowling_node
from src.graph.venue_node import venue_node
from src.graph.records_node import records_node
from src.graph.h2h_node import h2h_node
from src.graph.trend_node import trend_node
from src.graph.form_node import form_node
from src.graph.validation_node import validation_node
from src.graph.response_node import response_node


builder = StateGraph(IPLState)

builder.add_node("router", route_query)

builder.add_node("team", team_node)
builder.add_node("batting", batting_node)
builder.add_node("bowling", bowling_node)
builder.add_node("venue", venue_node)
builder.add_node("records", records_node)
builder.add_node("h2h", h2h_node)
builder.add_node("trend", trend_node)
builder.add_node("form", form_node)
builder.add_node("validation", validation_node)
builder.add_node("response", response_node)
builder.add_node("dream11",dream11_node)
builder.set_entry_point("router")
builder.add_node(
    "web",
    web_node
)

def route_decision(state):

    return state["route"]
def validation_route(state):

    if state["confidence_score"] < 0.2:

        return "web"

    return "response"

builder.add_conditional_edges(
    "router",
    route_decision,
    {
        
            "team":"team",
            "batting":"batting",
            "bowling":"bowling",
            "venue":"venue",
            "records":"records",
            "h2h":"h2h",
            "trend":"trend",
            "form":"form",
            "dream11":"dream11"
        
    }
)

builder.add_edge("team", "validation")
builder.add_edge("batting", "validation")
builder.add_edge("bowling", "validation")
builder.add_edge("venue", "validation")
builder.add_edge("records", "validation")
builder.add_edge("h2h","validation")
builder.add_edge("trend","validation")
builder.add_edge("form","validation")
builder.add_edge("dream11","validation")
builder.add_conditional_edges(
    "validation",
    validation_route,
    {
        "web": "web",
        "response": "response"
    }
)

builder.add_edge("response", END)

graph = builder.compile()