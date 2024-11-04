

from typing import Any, Dict


class EvaluatorCategory:
    id: Any
    category_name: str
    interactions: Dict[str, Dict[str, Any]]  # Inclui métricas por conjunto de interações

    def __init__(self, id, category_name, interactions):
        self.id = id
        self.category_name = category_name
        self.interactions = interactions  # {interaction_type: {'evaluations': List[EvaluatorBase], 'metrics': Dict}}

    def to_json(self):
        return {
            "id": str(self.id),
            "category_name": self.category_name,
            "interactions": {
                interaction_type: {
                    'evaluations': [eval_base.to_json() for eval_base in data['evaluations']],
                    'metrics': data['metrics']
                }
                for interaction_type, data in self.interactions.items()
            }
        }