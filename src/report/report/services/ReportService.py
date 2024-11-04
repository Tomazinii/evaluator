

from abc import ABC, abstractmethod

from src.evaluator.entity.EvaluatorSet import EvaluatorSet

class ReportService(ABC):
    @abstractmethod
    def generate_interaction_graphs(self, evaluator_set: EvaluatorSet) -> None:
        """
        Gera gráficos para cada tipo de interação e salva as imagens em formato PNG.

        Args:
            evaluator_set (EvaluatorSet): O conjunto de dados avaliados.
        """
        raise NotImplementedError

    @abstractmethod
    def generate_global_metrics_graph(self, evaluator_set: EvaluatorSet) -> None:
        """
        Gera um gráfico para as métricas globais e salva a imagem em formato PNG.

        Args:
            evaluator_set (EvaluatorSet): O conjunto de dados avaliados.
        """
        raise NotImplementedError