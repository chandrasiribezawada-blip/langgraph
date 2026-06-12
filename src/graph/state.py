from typing import TypedDict, List
class IPLState(TypedDict):
    query: str
    route: str
    retrieved_docs: List[str]
    validated_context: str
    confidence_score: float
    response: str