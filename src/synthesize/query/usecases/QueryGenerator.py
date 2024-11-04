from typing import Any, Dict
from pydantic import BaseModel
from src.shared.usecases.UsecaseInterface import IUsecase
from src.synthesize.query.entity.QuerySet import InputCreateQuerySet, QueryCategory, QuerySet
from src.synthesize.query.repository.QueryRepository import IQueryRepository
from src.synthesize.query.repository.QuerySource import IQuerySource
from src.synthesize.query.services.QueryGeneratorServiceInterface import IQueryGeneratorService




class InputQueryGeneratorDto(BaseModel):
    query_set_name: str
    llm_model_name: str
    source_path: Any = None
    n: int = 1 #number of synthetic queries
    


class QueryGenerator(IUsecase):


    def __init__(self, repository: IQueryRepository, query_source: IQuerySource , query_generator_service: IQueryGeneratorService):
        self.repository = repository
        self.query_source = query_source
        self.query_generator_service = query_generator_service


    def execute(self, input: InputQueryGeneratorDto) -> None:
        data_source: str = self.query_source.get_source_data(input.source_path)
        categories: Dict[str, QueryCategory] = self.query_generator_service.generate(data_source=data_source, n = input.n)
        input_query_set = InputCreateQuerySet(
            query_set_name=input.query_set_name,
            llm_model=input.llm_model_name,
            source=input.source_path
        )
        query_set = QuerySet.create(input=input_query_set)
        query_set.set_category(categories)
        self.repository.save(query_set)



