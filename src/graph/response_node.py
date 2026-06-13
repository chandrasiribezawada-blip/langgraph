from langchain_core.messages import SystemMessage, HumanMessage

from src.llm.llm_factory import get_llm
from src.prompts.response_prompt import SYSTEM_PROMPT


def response_node(state):

    confidence = state["confidence_score"]

    if confidence < 0.2:
        state["response"] = (
            "I could not find enough information in the dataset."
        )
        return state

    llm = get_llm()

    prompt = f"""
{SYSTEM_PROMPT}

User Question:
{state['query']}

Retrieved Context:
{state['validated_context']}

Answer:
"""

    response = llm.invoke(
    [
        SystemMessage(content=SYSTEM_PROMPT),
        HumanMessage(
            content=f"""
Question:
{state['query']}

Context:
{state['validated_context'][:3000]}
"""
        )
    ]
)

    state["response"] = response.content

    return state