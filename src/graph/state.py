from typing import TypedDict


class IPLState(TypedDict):

    query: str

    route: str

    retrieved_docs: list

    validated_context: str

    confidence_score: float

    response: str
    
    source: str