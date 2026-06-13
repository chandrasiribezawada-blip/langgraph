import streamlit as st

from src.graph.graph_builder import graph

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
# UI
# ----------------------------

st.title(
    "🏏 IPL Agentic RAG System"
)
st.caption(
    "Multi-Agent Retrieval-Augmented Generation using LangGraph"
)

query = st.text_input(
    "Ask an IPL question"
)

if st.button("Submit"):

    with st.spinner("Thinking..."):

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

    # ----------------------------
    # SAVE QUERY HISTORY
    # ----------------------------

    st.session_state.history.append(
        {
            "query": query,
            "route": result["route"]
        }
    )

    st.subheader("Route")
    st.success(result["route"])
    st.subheader("Execution Flow")

    st.code(
    f"Router → {result['route']} Agent → Validation → LLM Response")
    st.subheader("Confidence")
    st.info(result["confidence_score"])

    st.subheader("Answer")
    st.write(result["response"])

# ----------------------------
# SIDEBAR HISTORY
# ----------------------------

st.sidebar.title("Query History")

for item in reversed(st.session_state.history):

    st.sidebar.write(
        f"{item['query']} → {item['route']}"
    )
    
st.sidebar.divider()

st.sidebar.subheader("Project Stats")

st.sidebar.write("Nodes: 10")
st.sidebar.write("Agents: 8")
st.sidebar.write("Vector DB: FAISS")
st.sidebar.write("LLM: Groq")
st.sidebar.write("Framework: LangGraph")