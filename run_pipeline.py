


# from src.evaluator.usecases.Evaluator import EvaluateRunEvaluatorSetUseCase
# from src.infra.repository.JSONRepository import JSONRepository
# from src.infra.repository.report.JsonRepository import JSONRepository as JSONRepositoryReport
# from src.infra.services.evaluator.ragas.RagasEvaluateService import RagasEvaluateService
# from src.infra.services.rag_pipeline.RAGPipeline import RAGPipelineService
# from src.infra.services.report.ReportService import MatplotlibReportService
# from src.orchestrator.run_evaluator.usecases.RunEvaluatorUsecase import RunEvaluatorSetUseCase
# from src.report.report.usecases.GenerateReport import GenerateReportUseCase
# from src.synthesize.query.usecases.FindQuerySet import FindQuerySet, InputFindQuerySetDto
# import asyncio
# query_set_repository = JSONRepository()

# query_set_source = FindQuerySet(repository=query_set_repository)

# input_find = InputFindQuerySetDto(
#     id="90a83b13-418a-4683-8d0f-6812c8ecf2aa" 
# )

# query_set = query_set_source.execute(input_find)

# rag_pipeline = RAGPipelineService(rag_pipeline_url="http://host.docker.internal:8000/naive-rag")

# orchestrator = RunEvaluatorSetUseCase(rag_pipeline=rag_pipeline)

# run_evaluator_set = orchestrator.execute(query_set=query_set)

# evaluator_service = RagasEvaluateService()

# evaluator = EvaluateRunEvaluatorSetUseCase(evaluate_service=evaluator_service,repository="")

# evaluator_set =  asyncio.run(evaluator.execute(run_evaluator_set=run_evaluator_set))

# report_service = MatplotlibReportService(output_dir="data")

# report_repository = JSONRepositoryReport()
# usecase = GenerateReportUseCase(report_service=report_service,repository=report_repository)


# report = usecase.execute(evaluator_set=evaluator_set)
