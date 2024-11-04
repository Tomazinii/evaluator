from typing import Dict, List
from uuid import uuid4



class QueryResponseSet:
    id: any
    query: str
    query_type: str
    expected_response: str = None
    expected_context: str = None
    generated_response: str = None
    retriaved_context: List[any] = None

    def __init__(self, id, query, expected_response, expected_context, generated_response, retriaved_context,query_type):
        self.id = id
        self.query = query
        self.expected_response = expected_response
        self.expected_context = expected_context
        self.generated_response = generated_response
        self.retriaved_context = retriaved_context
        self.query_type = query_type

    @staticmethod
    def create(query, expected_response, expected_context,query_type, generated_response = None, retriaved_context = None):
        query_response_set = QueryResponseSet(id=uuid4(), query=query, expected_response=expected_response,expected_context=expected_context, generated_response=generated_response, retriaved_context=retriaved_context, query_type=query_type)
        return query_response_set


class QueryResponseCategory:
    id: any
    category_name: str
    interactions: Dict[str, List[QueryResponseSet]] = {}

    def __init__(self, category_name: str, id = uuid4()):
        self.id = id
        self.category_name = category_name
        

    def set_interaction(self, interaction_type, interaction: QueryResponseSet):
        if interaction_type not in self.interactions:
            self.interactions[interaction_type] = []
        self.interactions[interaction_type].append(interaction)




class RunEvaluatorSet:
    id: any 
    query_set_id: any
    query_set_name: str
    query_set_llm: str
    categories: Dict[str, QueryResponseCategory] = {}


    def __init__(self, query_set_id, query_set_name, query_set_llm, id = uuid4()):
        self.query_set_id = query_set_id
        self.query_set_name = query_set_name
        self.query_set_llm = query_set_llm
        self.id = id
        

    def set_category(self,category: QueryResponseCategory):
        self.categories[category.category_name] = category

