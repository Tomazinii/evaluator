from abc import ABC, abstractmethod
from typing import Dict
from src.orchestrator.run_evaluator.entity.ResponseSet import ResponseSet
from pydantic import BaseModel


class InputRagPipelineDto(BaseModel):
    user_input: str


class IRAGPipeline(ABC):
    @abstractmethod
    def execute(self, input: InputRagPipelineDto) -> ResponseSet:
        raise NotImplementedError