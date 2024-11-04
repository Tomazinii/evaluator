
from typing import Any, Dict, List
from src.evaluator.service.EvaluateService import IEvaluateService
from src.orchestrator.run_evaluator.entity.RunEvaluatorBase import RunEvaluatorBase


class AresEvaluateService(IEvaluateService):

    def __init__(self, llm_model_name: str = 'gpt-4', metrics: List[Any] = None):
        pass
    
    def evaluate(self, run_evaluator_bases: List[RunEvaluatorBase]) -> Dict[str, Any]:
        pass