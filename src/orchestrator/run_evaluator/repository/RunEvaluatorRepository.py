

from abc import ABC, abstractmethod

from src.orchestrator.run_evaluator.entity.RunEvaluateSet import RunEvaluatorSet


class IRunEvaluatorRepository(ABC):

    @abstractmethod
    def save(self, run_evaluator_set: RunEvaluatorSet):
        """
        Salva o RunEvaluatorSet em um meio de armazenamento persistente.

        Args:
            run_evaluator_set (RunEvaluatorSet): O objeto a ser salvo.
        """
        raise NotImplementedError