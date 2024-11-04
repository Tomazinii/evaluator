import asyncio
from datetime import datetime
from uuid import uuid4
from src.evaluator.usecases.Evaluator import EvaluateRunEvaluatorSetUseCase
from src.infra.services.evaluator.ragas.RagasEvaluateService import RagasEvaluateService
from src.orchestrator.run_evaluator.entity.RunEvaluateSet import RunEvaluatorSet
from src.orchestrator.run_evaluator.entity.RunEvaluatorBase import RunEvaluatorBase
from src.orchestrator.run_evaluator.entity.RunEvaluatorCategory import RunEvaluatorCategory

evaluate_service = RagasEvaluateService()

usecase = EvaluateRunEvaluatorSetUseCase(evaluate_service=evaluate_service, repository="")

run_evaluator_base_1 = RunEvaluatorBase(
    id=str(uuid4()),
    query_type='question_answering',
    reference='Paris is the capital of France.',
    query='What is the capital of France?',
    response='The capital of France is Paris.',
    retrieved_context=['France is a country in Western Europe. Paris is its capital city.']
)

run_evaluator_base_2 = RunEvaluatorBase(
    id=str(uuid4()),
    query_type='question_answering',
    reference='Berlin is the capital of Germany.',
    query='What is the capital of Germany?',
    response='The capital of Germany is Berlin.',
    retrieved_context=['Germany is a country in Central Europe. Berlin is its capital.']
)

# Criando uma lista de interações para um tipo de interação
interactions_list = [run_evaluator_base_1, run_evaluator_base_2]

# Criando o dicionário de interações
interactions = {
    'question_answering': interactions_list
}

# Criando uma categoria
run_evaluator_category = RunEvaluatorCategory(
    id=str(uuid4()),
    category_name='General Knowledge',
    interactions=interactions
)

# Criando o dicionário de categorias
categories = {
    'General Knowledge': run_evaluator_category
}

# Criando o RunEvaluatorSet
run_evaluator_set = RunEvaluatorSet(
    id=str(uuid4()),
    query_set_name='Sample Query Set',
    llm_model='GPT-3',
    source='Generated for Testing',
    created_at=datetime.now(),
    categories=categories
)



result =  asyncio.run(usecase.execute(run_evaluator_set=run_evaluator_set))

print(result)