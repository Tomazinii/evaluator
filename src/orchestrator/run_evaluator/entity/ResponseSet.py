

from typing import Any, AnyStr, List


class ResponseSet:
    id: Any
    response: str
    retrieved_context: List[AnyStr]

    def __init__(self, id, response, retrieved_context):
        self.id = id
        self.response = response
        self.retrieved_context = retrieved_context

    def to_json(self):
        return {
            'id': str(self.id),
            'response': self.response,
            'retrieved_context': self.retrieved_context
        }