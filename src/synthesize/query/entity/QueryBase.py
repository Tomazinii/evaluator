from typing import List, Union


class QueryBase:
    id: any
    query_type: str
    reference: Union[str, None]
    query: Union[str, List[str]]

    def __init__(self, query, query_type , id, reference):
        self.id = id 
        self.reference = reference
        self.query = query
        self.query_type = query_type

    def to_json(self):
        return {
            'id': str(self.id),
            'reference': self.reference,
            'query': self.query,
            'query_type': self.query_type
        }