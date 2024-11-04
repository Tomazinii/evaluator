

from src.evaluator.entity.EvaluatorSet import EvaluatorSet
from src.report.report.repository.ReportRepository import IReportRepository
from src.report.report.services.ReportService import ReportService


class GenerateReportUseCase:
    def __init__(self, report_service: ReportService, repository: IReportRepository):
        self.report_service = report_service
        self.repository = repository

    def execute(self, evaluator_set: EvaluatorSet) -> None:
        """
        Gera os relatórios (gráficos) para o EvaluatorSet fornecido.

        Args:
            evaluator_set (EvaluatorSet): O conjunto de dados avaliados.
        """

        self.repository.save(evaluator_set)

        # Gera gráficos para cada tipo de interação
        # self.report_service.generate_interaction_graphs(evaluator_set)

        # Gera gráfico para as métricas globais
        # self.report_service.generate_global_metrics_graph(evaluator_set)