from src.synthesize.query.usecases.QueryGenerator import QueryGenerator
from src.infra.repository.JSONRepository import JSONRepository
from src.infra.services.query_generator.QueryGeneratorService import QueryGeneratorService
from src.infra.repository.QuerySourceRepository import CSVQuerySourceRepository
from src.synthesize.query.usecases.QueryGenerator import InputQueryGeneratorDto

repository = JSONRepository()
service = QueryGeneratorService()
query_source = CSVQuerySourceRepository()
usecase = QueryGenerator(repository=repository, query_generator_service=service, query_source=query_source)

input_usecase = InputQueryGeneratorDto(
    query_set_name = "teste",
    llm_model_name = "gemini",
    source_path = "pdi_chunks",
    n = 10
)
usecase.execute(input_usecase)