

from abc import ABC, abstractmethod
from typing import Dict

from src.synthesize.query.entity.QuerySet import QueryCategory


class IQueryGeneratorService(ABC):

    @abstractmethod
    def generate(self, data_source: str, n:int) -> Dict[str, QueryCategory]:
        raise NotImplementedError