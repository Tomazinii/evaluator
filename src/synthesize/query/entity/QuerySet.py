
import datetime
from uu import Error
from uuid import uuid4
from typing import Dict, List
from src.synthesize.query.entity.QueryBase import QueryBase


class QueryCategory:
    id: any
    category_name: str
    interactions: Dict[str, List[QueryBase]] = {}

    def __init__(self,category_name: str, id, interactions: dict):
        self.id = id
        self.category_name = category_name
        self.interactions = interactions

    @staticmethod
    def create(category_name: str):
        query_category = QueryCategory(category_name, id=uuid4(), interactions={})
        return query_category

    def set_interaction(self,interaction_type:str, interaction: List[QueryBase]):
        self.interactions[interaction_type] = interaction


    def __str__(self) -> str:
        return f"id: {self.id} category_name: {self.category_name}"

    def to_json(self):
        return {
            "id": str(self.id),
            "category_name": self.category_name,
            "interactions": {k: [i.to_json() for i in v] for k, v in self.interactions.items()}
        }

class InputConstructQuerySet:

    def __init__(self, id, query_set_name, llm_model, source, created_at, categories):
        self.id = id
        self.query_set_name = query_set_name
        self.llm_model = llm_model
        self.source = source
        self.created_at = created_at
        self.categories = categories




class InputCreateQuerySet:

    def __init__(self, query_set_name, llm_model, source):
        self.id = str(uuid4())
        self.query_set_name = query_set_name
        self.llm_model = llm_model
        self.source = source
        self.created_at = datetime.datetime.now()
        self.categories = {}

class QuerySet:
    id: any
    query_set_name: str
    llm_model: str
    source: any
    created_at: datetime
    categories: Dict[str, QueryCategory]

    def __init__(self, input: InputConstructQuerySet):
        self.id = input.id
        self.query_set_name = input.query_set_name
        self.llm_model = input.llm_model
        self.source = input.source
        self.created_at = input.created_at
        self.categories = input.categories
        

    def to_json(self):
        return {
            "id": str(self.id),
            "query_set_name": self.query_set_name,
            "llm_model": self.llm_model,
            "source": self.source,
            "created_at": self.created_at.isoformat(),
            "categories": {k: v.to_json() for k, v in self.categories.items()}
        }

    @staticmethod
    def create(input: InputCreateQuerySet):

        input_data = InputConstructQuerySet(
            categories=input.categories,
            created_at=input.created_at,
            id=input.id,
            llm_model=input.llm_model,
            query_set_name=input.query_set_name,
            source=input.source
        )

        queryset = QuerySet(input_data)
        return queryset
    
    def set_category(self, categories: Dict[str, QueryCategory]):

        if not isinstance(categories, dict):
            raise Error("type error category")
        
        self.categories = categories

    def get_category(self, category_name: str) -> QueryCategory:

        if self.categories[category_name]:
            return self.categories[category_name]
        raise Error("Category not found")
    

    def __str__(self) -> str:
        return f"QuerySet: {self.to_json()}"
    
