from src.tools.batting_tool import batting_tool
from src.tools.form_tool import form_tool
from src.tools.venue_tool import venue_tool

def dream11_node(state):

    query = state["query"]

    batting_docs = batting_tool(query)

    form_docs = form_tool(query)

    venue_docs = venue_tool(query)

    combined_context = f"""
BATTING DATA:
{batting_docs}

FORM DATA:
{form_docs}

VENUE DATA:
{venue_docs}
"""

    state["retrieved_docs"] = combined_context

    return state