

from abc import ABC, abstractmethod

from src.synthesize.query.entity.QuerySet import QuerySet


class IQueryRepository(ABC):

    @abstractmethod
    def save(self, input: QuerySet):
        raise NotImplementedError
    
    @abstractmethod
    def find_by_id(self, id) -> QuerySet:
        raise NotImplementedError