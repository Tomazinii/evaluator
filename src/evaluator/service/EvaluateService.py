from abc import ABC, abstractmethod
from typing import Any, Dict, List, Union

from src.orchestrator.run_evaluator.entity.RunEvaluatorBase import RunEvaluatorBase

class IEvaluateService(ABC):
    @abstractmethod
    def evaluate(self, input: List[RunEvaluatorBase]) -> Dict[str, Any]:
        """
        Avalia a resposta fornecida em relação à query e à referência, retornando métricas.

        Args:
            query (Union[str, List[str]]): A query ou lista de queries.
            response (str): A resposta gerada pelo sistema.
            reference (Union[str, None]): A resposta de referência esperada.

        Returns:
            Dict[str, Any]: Um dicionário contendo as métricas de avaliação.
        """
        raise NotImplementedError