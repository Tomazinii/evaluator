
from src.evaluator.entity.EvaluateCategory import EvaluatorCategory
from src.evaluator.entity.EvaluatorBase import EvaluatorBase
from src.evaluator.entity.EvaluatorSet import EvaluatorSet
from src.infra.services.report.ReportService import MatplotlibReportService
from src.report.report.usecases.GenerateReport import GenerateReportUseCase

from src.infra.repository.report.JsonRepository import JSONRepository



from datetime import datetime
from uuid import uuid4

# Supondo que as classes EvaluatorBase, EvaluatorCategory e EvaluatorSet já foram definidas conforme anteriormente

# Criando métricas fake para as interações
fake_metrics_interaction_1 = {
    'accuracy': 1.0,
    'precision': 0.9,
    'recall': 0.95
}

fake_metrics_interaction_2 = {
    'accuracy': 0.8,
    'precision': 0.75,
    'recall': 0.85
}

# Calculando métricas agregadas para o conjunto de interações
def calculate_aggregated_metrics(metrics_list):
    aggregated_metrics = {}
    for key in metrics_list[0].keys():
        values = [metrics[key] for metrics in metrics_list if key in metrics]
        aggregated_metrics[key] = sum(values) / len(values) if values else None
    return aggregated_metrics

interaction_metrics_list = [fake_metrics_interaction_1, fake_metrics_interaction_2]
aggregated_metrics_interaction = calculate_aggregated_metrics(interaction_metrics_list)

# Criando métricas globais (neste caso, iguais às métricas agregadas, pois temos um único tipo de interação)
overall_metrics = aggregated_metrics_interaction

# Criando instâncias de EvaluatorBase
evaluator_base_1 = EvaluatorBase(
    id=str(uuid4()),
    query_type='question_answering',
    reference='Paris is the capital of France.',
    query='What is the capital of France?',
    response='The capital of France is Paris.',
    retrieved_context='France, officially the French Republic, is a country whose territory consists of metropolitan France in Western Europe...',
    metrics=fake_metrics_interaction_1
)

evaluator_base_2 = EvaluatorBase(
    id=str(uuid4()),
    query_type='question_answering',
    reference='Berlin is the capital of Germany.',
    query='What is the capital of Germany?',
    response='The capital of Germany is Berlin.',
    retrieved_context='Germany is a country in Central and Western Europe. It borders Denmark to the north...',
    metrics=fake_metrics_interaction_2
)

# Criando uma lista de avaliações para um tipo de interação
evaluations_list = [evaluator_base_1, evaluator_base_2]

# Criando o dicionário de interações com métricas
interactions = {
    'question_answering': {
        'evaluations': evaluations_list,
        'metrics': aggregated_metrics_interaction
    }
}

# Criando uma categoria
evaluator_category = EvaluatorCategory(
    id=str(uuid4()),
    category_name='General Knowledge',
    interactions=interactions
)

# Criando o dicionário de categorias
categories = {
    'General Knowledge': evaluator_category
}

# Criando o EvaluatorSet
evaluator_set = EvaluatorSet(
    id=str(uuid4()),
    query_set_name='Sample Query Set',
    llm_model='GPT-3',
    source='Generated for Testing',
    created_at=datetime.now(),
    categories=categories,
    overall_metrics=overall_metrics
)

report_service = MatplotlibReportService(output_dir="data")

report_repository = JSONRepository()
usecase = GenerateReportUseCase(report_service=report_service,repository=report_repository)


usecase.execute(evaluator_set=evaluator_set)