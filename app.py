import streamlit as st

from src.graph.graph_builder import graph

# ----------------------------
# PAGE CONFIG
# ----------------------------

st.set_page_config(
    page_title="IPL Intelligence Assistant",
    page_icon="🏏",
    layout="wide"
)

# ----------------------------
# QUERY HISTORY
# ----------------------------

if "history" not in st.session_state:
    st.session_state.history = []

# ----------------------------
# HEADER
# ----------------------------

st.title("🏏 IPL Agentic RAG System")

st.caption(
    "Multi-Agent Retrieval-Augmented Generation using LangGraph"
)


# ----------------------------
# USER INPUT
# ----------------------------

query = st.text_input(
    "Ask an IPL Question",
    placeholder="Example: Who has scored the most runs in IPL history?"
)

# ----------------------------
# SUBMIT BUTTON
# ----------------------------

if st.button("Submit"):

    if query.strip():

        with st.spinner("Thinking..."):

            result = graph.invoke(
                {
                    "query": query,
                    "route": "",
                    "retrieved_docs": [],
                    "validated_context": "",
                    "confidence_score": 0.0,
                    "response": "",
                    "source": "dataset"
                }
            )

        # ----------------------------
        # SAVE QUERY HISTORY
        # ----------------------------

        st.session_state.history.append(
            {
                "query": query,
                "route": result.get("route", "unknown")
            }
        )

        # ----------------------------
        # ROUTE
        # ----------------------------

        st.subheader("Route")
        st.success(result.get("route", "unknown"))

        # ----------------------------
        # EXECUTION FLOW
        # ----------------------------

        st.subheader("Execution Flow")

        if result.get("route") == "dream11":

            st.code("""
Router
 ↓
Dream11 Agent
 ↓
Batting Agent
 ↓
Form Agent
 ↓
Venue Agent
 ↓
Validation Agent
 ↓
LLM
""")

        else:

            st.code(
                f"Router → {result.get('route', 'unknown')} Agent → Validation Agent → LLM"
            )

        # ----------------------------
        # CONFIDENCE
        # ----------------------------

        st.subheader("Confidence Score")
        st.info(result.get("confidence_score", 0.0))

        st.subheader("Confidence Meter")
        st.progress(
            float(
                result.get(
                    "confidence_score",
                    0.0
                )
            )
        )

        # ----------------------------
        # SOURCE
        # ----------------------------

        st.subheader("Source")

        st.success(
            result.get(
                "source",
                "dataset"
            )
        )

        # ----------------------------
        # ANSWER
        # ----------------------------

        st.subheader("Answer")

        st.write(
            result.get(
                "response",
                "No response generated."
            )
        )

        # ----------------------------
        # CONTEXT
        # ----------------------------

        with st.expander("Retrieved Context"):

            st.write(
                result.get(
                    "validated_context",
                    "No context found."
                )
            )

    else:

        st.warning("Please enter a question.")

# ----------------------------
# SIDEBAR
# ----------------------------

st.sidebar.title("Query History")

if st.session_state.history:

    for item in reversed(st.session_state.history):

        st.sidebar.write(
            f"• {item['query']} → {item['route']}"
        )

st.sidebar.write(
    f"Total Queries: {len(st.session_state.history)}"
)

st.sidebar.divider()

# ----------------------------
# PROJECT STATS
# ----------------------------

st.sidebar.subheader("Project Stats")

st.sidebar.write("Nodes: 12")
st.sidebar.write("Agents: 10")
st.sidebar.write("Retrieval: FAISS")
st.sidebar.write("Fallback: Tavily Search")
st.sidebar.write("Vector DB: FAISS")
st.sidebar.write("LLM: Groq")
st.sidebar.write("Framework: LangGraph")

st.sidebar.divider()

st.sidebar.subheader("Architecture")

st.sidebar.write(
    """
Router
↓
Specialized Agent
↓
Validation
↓
Dataset Response

or

Validation
↓
Web Search Agent
↓
LLM Response
"""
)