from datetime import datetime
from typing import Dict, List
from uuid import UUID
from src.synthesize.query.entity.QueryBase import QueryBase
from src.synthesize.query.entity.QuerySet import InputConstructQuerySet, QueryCategory, QuerySet
from src.synthesize.query.repository.QueryRepository import IQueryRepository
import os

import json


class JSONRepository(IQueryRepository):
    
    def __init__(self) -> None:
        super().__init__()
        
    def save(self, input: QuerySet):
        base_dir = os.path.join(os.getcwd(), 'src', 'data')
        
        if not os.path.exists(base_dir):
            os.makedirs(base_dir)
        
        file_path = os.path.join(base_dir, str(input.id))

        with open(file_path, 'w') as json_file:
            json.dump(input.to_json(), json_file, indent=4)
    

    def parse_query_base(self, query_base_data: dict) -> QueryBase:
        """Converte um dicionário JSON em uma instância de QueryBase."""

        

        return QueryBase(
            id=UUID(query_base_data['id']),
            query=query_base_data['query'],
            query_type=query_base_data['query_type'],
            reference=query_base_data.get('reference', None)
        )
    
    
    def parse_query_category(self, category_data: dict) -> QueryCategory:
        """Converte um dicionário JSON em uma instância de QueryCategory."""

        interactions = {
            interaction_type: [self.parse_query_base(qb) for qb in interaction_list]
            for interaction_type, interaction_list in category_data['interactions'].items()
        }
        return QueryCategory(
            id=UUID(category_data['id']),
            category_name=category_data['category_name'],
            interactions=interactions
        )

    def parse_query_set(self, data: dict) -> QuerySet:
        """Converte o JSON completo em uma instância de QuerySet."""


        categories = {
            category_name: self.parse_query_category(category_data)
            for category_name, category_data in data['categories'].items()
        }


        input = InputConstructQuerySet(
            id=data['id'],
            query_set_name=data['query_set_name'],
            llm_model=data['llm_model'],
            source=data['source'],
            created_at=datetime.fromisoformat(data['created_at']),
            categories=categories
        )

        return QuerySet(input)

    def find_by_id(self, id) -> QuerySet:
        base_dir = os.path.join(os.getcwd(), 'src', 'data')
        
        if not os.path.exists(base_dir):
            os.makedirs(base_dir)

 
        
        file_path = os.path.join(base_dir, str(id))

        with open(file_path, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)


     

        query_set = self.parse_query_set(data)

        return query_set
        
