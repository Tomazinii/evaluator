
from typing import Any, Dict, List
from typing import Any, List

from src.orchestrator.run_evaluator.entity.RunEvaluatorBase import RunEvaluatorBase


class RunEvaluatorCategory:
    id: Any
    category_name: str
    interactions: Dict[str, List[RunEvaluatorBase]]

    def __init__(self, id, category_name, interactions):
        self.id = id
        self.category_name = category_name
        self.interactions = interactions

    def to_json(self):
        return {
            "id": str(self.id),
            "category_name": self.category_name,
            "interactions": {
                k: [i.to_json() for i in v] for k, v in self.interactions.items()
            }
        }