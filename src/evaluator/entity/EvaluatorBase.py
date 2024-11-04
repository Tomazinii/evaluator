from typing import Any, Dict, List, Union

class EvaluatorBase:
    id: Any
    query_type: str
    reference: Union[str, None]
    query: Union[str, List[str]]
    response: str
    retrieved_context: str
    metrics: Dict[str, Any]

    def __init__(self, id, query_type, reference, query, response, retrieved_context, metrics):
        self.id = id
        self.query_type = query_type
        self.reference = reference
        self.query = query
        self.response = response
        self.retrieved_context = retrieved_context
        self.metrics = metrics

    def to_json(self):
        return {
            'id': str(self.id),
            'reference': self.reference,
            'query': self.query,
            'query_type': self.query_type,
            'response': self.response,
            'retrieved_context': self.retrieved_context,
            'metrics': self.metrics
        }