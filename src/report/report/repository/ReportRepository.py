

from abc import ABC, abstractmethod

from src.evaluator.entity.EvaluatorSet import EvaluatorSet


class IReportRepository(ABC):

    @abstractmethod
    def save(self, input: EvaluatorSet):
        raise NotImplementedError