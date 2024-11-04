

from typing import Dict, List
from src.evaluator.entity.EvaluateCategory import EvaluatorCategory
from src.evaluator.entity.EvaluatorBase import EvaluatorBase
from src.evaluator.entity.EvaluatorSet import EvaluatorSet
from src.evaluator.service.EvaluateService import IEvaluateService
from src.orchestrator.run_evaluator.entity.RunEvaluateSet import RunEvaluatorSet
from src.orchestrator.run_evaluator.entity.RunEvaluatorBase import RunEvaluatorBase


class EvaluateRunEvaluatorSetUseCase:
    def __init__(self, evaluate_service: IEvaluateService, repository: 'EvaluatorSetRepository'):
        self.evaluate_service = evaluate_service
        self.repository = repository

    async def execute(self, run_evaluator_set: 'RunEvaluatorSet') -> EvaluatorSet:
        """
        Processa o RunEvaluatorSet fornecido, executa o serviço de avaliação em cada conjunto de interações,
        e retorna um EvaluatorSet contendo as métricas.

        Além disso, salva o EvaluatorSet utilizando o repositório fornecido.

        Args:
            run_evaluator_set (RunEvaluatorSet): O conjunto de dados a ser avaliado.

        Returns:
            EvaluatorSet: O conjunto de dados com as métricas de avaliação.
        """
        # Cria um novo EvaluatorSet
        evaluator_set = EvaluatorSet(
            id=run_evaluator_set.id,
            query_set_name=run_evaluator_set.query_set_name,
            llm_model=run_evaluator_set.llm_model,
            source=run_evaluator_set.source,
            created_at=run_evaluator_set.created_at,
            categories={},
            overall_metrics={}
        )

        # Dicionário para acumular métricas gerais
        interaction_accumulated_metrics = {}

        # Lista para acumular todas as interações para cálculo das métricas globais
        all_run_evaluator_bases = []

        for category_name, run_evaluator_category in run_evaluator_set.categories.items():
            interactions_with_metrics = {}

            for interaction_type, run_evaluator_list in run_evaluator_category.interactions.items():
                # Chama o evaluate_service com a lista de RunEvaluatorBase
                # try:
                metrics = await self.evaluate_service.evaluate(run_evaluator_list)
                # except Exception as e:
                #     metrics = {'error': f"Erro ao avaliar as interações: {e}"}

                # Acumula métricas para cálculo global
                for key, value in metrics.items():
                    if key not in interaction_accumulated_metrics:
                        interaction_accumulated_metrics[key] = []
                    if isinstance(value, (int, float)):
                        interaction_accumulated_metrics[key].append(value)

                # Cria EvaluatorBase para cada interação (pode incluir métricas individuais, se necessário)
                evaluator_list = []
                for run_evaluator_base in run_evaluator_list:
                    evaluator_base = EvaluatorBase(
                        id=run_evaluator_base.id,
                        query_type=run_evaluator_base.query_type,
                        reference=run_evaluator_base.reference,
                        query=run_evaluator_base.query,
                        response=run_evaluator_base.response,
                        retrieved_context=run_evaluator_base.retrieved_context,
                        metrics={}  # Métricas individuais podem ser adicionadas se disponíveis
                    )
                    evaluator_list.append(evaluator_base)
                    all_run_evaluator_bases.append(run_evaluator_base)

                # Adiciona as interações e métricas ao dicionário
                interactions_with_metrics[interaction_type] = {
                    'evaluations': evaluator_list,
                    'metrics': metrics
                }

            evaluator_category = EvaluatorCategory(
                id=run_evaluator_category.id,
                category_name=run_evaluator_category.category_name,
                interactions=interactions_with_metrics
            )

            evaluator_set.categories[category_name] = evaluator_category

        # Calcula métricas globais
        overall_metrics = self._calculate_aggregated_metrics(interaction_accumulated_metrics)
        evaluator_set.overall_metrics = overall_metrics

        # Salva o EvaluatorSet usando o repositório
        # self.repository.save(evaluator_set)
        return evaluator_set

    def _calculate_aggregated_metrics(self, accumulated_metrics: Dict[str, List[float]]) -> Dict[str, float]:
        """
        Calcula métricas agregadas (por exemplo, médias) a partir de listas de valores.

        Args:
            accumulated_metrics (Dict[str, List[float]]): Dicionário de métricas acumuladas.

        Returns:
            Dict[str, float]: Dicionário de métricas agregadas.
        """
        aggregated_metrics = {}
        for key, values in accumulated_metrics.items():
            if values:
                aggregated_metrics[key] = sum(values) / len(values)  # Exemplo de média
            else:
                aggregated_metrics[key] = None
        return aggregated_metrics


# class EvaluateRunEvaluatorSetUseCase:
#     def __init__(self, evaluate_service: IEvaluateService, repository: 'EvaluatorSetRepository'):
#         self.evaluate_service = evaluate_service
#         self.repository = repository

#     def execute(self, run_evaluator_set: RunEvaluatorSet) -> EvaluatorSet:
#         """
#         Processa o RunEvaluatorSet fornecido, executa o serviço de avaliação em cada interação,
#         e retorna um EvaluatorSet contendo as métricas.

#         Além disso, salva o EvaluatorSet utilizando o repositório fornecido.

#         Args:
#             run_evaluator_set (RunEvaluatorSet): O conjunto de dados a ser avaliado.

#         Returns:
#             EvaluatorSet: O conjunto de dados com as métricas de avaliação.
#         """
#         # Cria um novo EvaluatorSet
#         evaluator_set = EvaluatorSet(
#             id=run_evaluator_set.id,
#             query_set_name=run_evaluator_set.query_set_name,
#             llm_model=run_evaluator_set.llm_model,
#             source=run_evaluator_set.source,
#             created_at=run_evaluator_set.created_at,
#             categories={},
#             overall_metrics={}
#         )

#         # Dicionário para acumular métricas gerais
#         overall_accumulated_metrics = {}

#         for category_name, run_evaluator_category in run_evaluator_set.categories.items():
#             # Cria o dicionário de interações com métricas por conjunto
#             interactions_with_metrics = {}
#             interaction_accumulated_metrics = {}

#             for interaction_type, run_evaluator_list in run_evaluator_category.interactions.items():
#                 evaluator_list = []
#                 # Dicionário para acumular métricas por conjunto de interações

#                 lista: List[RunEvaluatorBase] = run_evaluator_list
#                 try:
#                     metrics: dict = self.evaluate_service.evaluate(lista)
#                 except Exception as e:
#                         # Trata exceções do serviço de avaliação
#                     metrics = {'error': f"Erro ao avaliar a resposta: {e}"}

#                 for key, value in metrics.items():
#                     # Acumula métricas para o conjunto de interações
#                     if key not in interaction_accumulated_metrics:
#                         interaction_accumulated_metrics[key] = []
#                     if isinstance(value, (int, float)):
#                         interaction_accumulated_metrics[key].append(value)

#                     # Acumula métricas gerais
#                     if key not in overall_accumulated_metrics:
#                         overall_accumulated_metrics[key] = []
#                     if isinstance(value, (int, float)):
#                         overall_accumulated_metrics[key].append(value)


#                 for run_evaluator_base in run_evaluator_list:
#                     try:
#                         # Executa o serviço de avaliação incluindo o retrieved_context
#                         metrics: dict = self.evaluate_service.evaluate(
#                             query=run_evaluator_base.query,
#                             response=run_evaluator_base.response,
#                             reference=run_evaluator_base.reference,
#                             retrieved_context=run_evaluator_base.retrieved_context
#                         )
#                     except Exception as e:
#                         # Trata exceções do serviço de avaliação
#                         metrics = {'error': f"Erro ao avaliar a resposta: {e}"}

#                     # Acumula métricas para cálculo por interação e geral
#                     for key, value in metrics.items():
#                         # Acumula métricas para o conjunto de interações
#                         if key not in interaction_accumulated_metrics:
#                             interaction_accumulated_metrics[key] = []
#                         if isinstance(value, (int, float)):
#                             interaction_accumulated_metrics[key].append(value)

#                         # Acumula métricas gerais
#                         if key not in overall_accumulated_metrics:
#                             overall_accumulated_metrics[key] = []
#                         if isinstance(value, (int, float)):
#                             overall_accumulated_metrics[key].append(value)

#                     # Cria EvaluatorBase com as métricas
#                     evaluator_base = EvaluatorBase(
#                         id=run_evaluator_base.id,
#                         query_type=run_evaluator_base.query_type,
#                         reference=run_evaluator_base.reference,
#                         query=run_evaluator_base.query,
#                         response=run_evaluator_base.response,
#                         retrieved_context=run_evaluator_base.retrieved_context,
#                         metrics=metrics
#                     )

#                     evaluator_list.append(evaluator_base)

#                 # Calcula métricas agregadas para o conjunto de interações
#                 interaction_metrics = self._calculate_aggregated_metrics(interaction_accumulated_metrics)

#                 # Adiciona as interações e métricas ao dicionário
#                 interactions_with_metrics[interaction_type] = {
#                     'evaluations': evaluator_list,
#                     'metrics': interaction_metrics
#                 }

#             # Cria EvaluatorCategory
#             evaluator_category = EvaluatorCategory(
#                 id=run_evaluator_category.id,
#                 category_name=run_evaluator_category.category_name,
#                 interactions=interactions_with_metrics
#             )

#             evaluator_set.categories[category_name] = evaluator_category

#         # Calcula métricas gerais
#         overall_metrics = self._calculate_aggregated_metrics(overall_accumulated_metrics)
#         evaluator_set.overall_metrics = overall_metrics

#         # Salva o EvaluatorSet usando o repositório
#         self.repository.save(evaluator_set)

#         return evaluator_set

#     def _calculate_aggregated_metrics(self, accumulated_metrics: Dict[str, List[float]]) -> Dict[str, float]:
#         """
#         Calcula métricas agregadas (por exemplo, médias) a partir de listas de valores.

#         Args:
#             accumulated_metrics (Dict[str, List[float]]): Dicionário de métricas acumuladas.

#         Returns:
#             Dict[str, float]: Dicionário de métricas agregadas.
#         """
#         aggregated_metrics = {}
#         for key, values in accumulated_metrics.items():
#             if values:
#                 aggregated_metrics[key] = sum(values) / len(values)  # Exemplo de média
#             else:
#                 aggregated_metrics[key] = None
#         return aggregated_metrics
