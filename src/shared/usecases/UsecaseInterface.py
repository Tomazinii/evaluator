

from abc import ABC, abstractmethod


class IUsecase(ABC):
    @abstractmethod
    def execute(self, input):
        raise NotImplementedError