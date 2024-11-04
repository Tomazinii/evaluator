

from src.infra.services.rag_pipeline.RAGPipeline import RAGPipelineService
from src.orchestrator.run_evaluator.usecases.RunEvaluatorUsecase import RunEvaluatorSetUseCase


from src.synthesize.query.usecases.FindQuerySet import FindQuerySet, InputFindQuerySetDto
from src.infra.repository.JSONRepository import JSONRepository

repository = JSONRepository()
usecase = FindQuerySet(repository=repository)

input = InputFindQuerySetDto(
    id="cc1565d3-a0d2-435c-a52e-f3be9fdfbe75"
)
query_set = usecase.execute(input)



rag_pipeline = RAGPipelineService(rag_pipeline_url="http://host.docker.internal:8000/batch")
usecase_run = RunEvaluatorSetUseCase(rag_pipeline=rag_pipeline)

response = usecase_run.execute(query_set)


print(response)