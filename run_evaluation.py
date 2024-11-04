


import asyncio
from src.evaluator.usecases.Evaluator import EvaluateRunEvaluatorSetUseCase
from src.infra.repository.run_evalutor.JSONRunEvaluatorRepository import JsonFileRunEvaluatorSetRepository
from src.infra.services.evaluator.ragas.RagasEvaluateService import RagasEvaluateService
from src.infra.services.report.ReportService import MatplotlibReportService
from src.report.report.usecases.GenerateReport import GenerateReportUseCase
from src.infra.repository.report.JsonRepository import JSONRepository as JSONRepositoryReport


evaluator_service = RagasEvaluateService()

evaluator = EvaluateRunEvaluatorSetUseCase(evaluate_service=evaluator_service,repository="")
run_evaluator_set = JsonFileRunEvaluatorSetRepository().find_by_id("90a83b13-418a-4683-8d0f-6812c8ecf2aa")
evaluator_set =  asyncio.run(evaluator.execute(run_evaluator_set=run_evaluator_set))
report_service = MatplotlibReportService(output_dir="data")
report_repository = JSONRepositoryReport(dataset_num="testando-simple-query", pattern="naive")
usecase = GenerateReportUseCase(report_service=report_service, repository=report_repository)

report = usecase.execute(evaluator_set=evaluator_set)


