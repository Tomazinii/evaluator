from typing import Any, List, Union


class RunEvaluatorBase:
    id: Any
    query_type: str
    reference: Union[str, None]
    query: Union[str, List[str]]
    response: str
    retrieved_context: List[Any]

    def __init__(self, id, query_type, reference, query, response, retrieved_context):
        self.id = id
        self.query_type = query_type
        self.reference = reference
        self.query = query
        self.response = response
        self.retrieved_context = retrieved_context

    def to_json(self):
        return {
            'id': str(self.id),
            'reference': self.reference,
            'query': self.query,
            'query_type': self.query_type,
            'response': self.response,
            'retrieved_context': self.retrieved_context
        }