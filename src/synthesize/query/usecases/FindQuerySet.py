

from pydantic import BaseModel
from src.shared.usecases.UsecaseInterface import IUsecase
from src.synthesize.query.entity.QuerySet import QuerySet
from src.synthesize.query.repository.QueryRepository import IQueryRepository


class InputFindQuerySetDto(BaseModel):
    id: str

class FindQuerySet(IUsecase):

    def __init__(self, repository: IQueryRepository):
        self.repository = repository

    def execute(self, input: InputFindQuerySetDto) -> QuerySet:
        query_set = self.repository.find_by_id(input.id)
        return query_set