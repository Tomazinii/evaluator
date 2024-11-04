
import datetime
from typing import Any, Dict

from src.orchestrator.run_evaluator.entity.RunEvaluatorCategory import RunEvaluatorCategory


class RunEvaluatorSet:
    id: Any
    query_set_name: str
    llm_model: str
    source: Any
    created_at: datetime
    categories: Dict[str, RunEvaluatorCategory]

    def __init__(self, id, query_set_name, llm_model, source, created_at, categories):
        self.id = id
        self.query_set_name = query_set_name
        self.llm_model = llm_model
        self.source = source
        self.created_at = created_at
        self.categories = categories

    def to_json(self):
        return {
            "id": str(self.id),
            "query_set_name": self.query_set_name,
            "llm_model": self.llm_model,
            "source": self.source,
            "created_at": self.created_at.isoformat(),
            "categories": {
                k: v.to_json() for k, v in self.categories.items()
            }
        }
    
    def __str__(self) -> str:
        return f""" id: {self.id}
                query_set_name: {self.query_set_name}
                llm_model: {self.llm_model}
                source: {self.source}
                categories: {self.categories}"""