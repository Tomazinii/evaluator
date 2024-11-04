from src.orchestrator.run_evaluator.entity.ResponseSet import ResponseSet
from src.orchestrator.run_evaluator.entity.RunEvaluateSet import RunEvaluatorSet
from src.orchestrator.run_evaluator.entity.RunEvaluatorBase import RunEvaluatorBase
from src.orchestrator.run_evaluator.entity.RunEvaluatorCategory import RunEvaluatorCategory
from src.orchestrator.run_evaluator.repository.RunEvaluatorRepository import IRunEvaluatorRepository
from src.orchestrator.services.rag_pipeline import IRAGPipeline, InputRagPipelineDto
from src.synthesize.query.entity.QuerySet import QuerySet


class RunEvaluatorSetUseCase:
    def __init__(self, rag_pipeline: IRAGPipeline, repository: IRunEvaluatorRepository):
        self.rag_pipeline = rag_pipeline
        self.repository = repository

    def execute(self, query_set: QuerySet) -> RunEvaluatorSet:
        """
        Processa o QuerySet fornecido, executa cada query usando a pipeline RAG,
        e retorna um RunEvaluatorSet contendo as respostas.

        Args:
            query_set (QuerySet): O QuerySet a ser processado.

        Returns:
            RunEvaluatorSet: O RunEvaluatorSet com as respostas.
        """
        # Cria um novo RunEvaluatorSet
        run_evaluator_set = RunEvaluatorSet(
            id=query_set.id,
            query_set_name=query_set.query_set_name,
            llm_model=query_set.llm_model,
            source=query_set.source,
            created_at=query_set.created_at,
            categories={}
        )

        for category_name, query_category in query_set.categories.items():
            # Cria RunEvaluatorCategory
            run_evaluator_category = RunEvaluatorCategory(
                id=query_category.id,
                category_name=query_category.category_name,
                interactions={}
            )

            for interaction_type, query_list in query_category.interactions.items():
                run_evaluator_list = []
                print("interaction_type:", interaction_type)
                for index, query_base in enumerate(query_list):
                    print("Query complete: ", index)
                    try:
                        # Executa a query usando a pipeline RAG e obtém um ResponseSet
                        input_response_set = InputRagPipelineDto(
                            user_input = query_base.query
                        )
                        response_set: ResponseSet = self.rag_pipeline.execute(input_response_set)

                        
                    except Exception as e:
                        # Trata exceções da pipeline RAG
                        response_set = ResponseSet(
                            id=query_base.id,
                            response=f"Erro ao executar a query: {e}",
                            retrieved_context=""
                        )

                    # Cria RunEvaluatorBase com os dados do ResponseSet
                    run_evaluator_base = RunEvaluatorBase(
                        id=query_base.id,
                        query_type=query_base.query_type,
                        reference=query_base.reference,
                        query=query_base.query,
                        response=response_set.response,
                        retrieved_context=response_set.retrieved_context
                    )

                    run_evaluator_list.append(run_evaluator_base)

                run_evaluator_category.interactions[interaction_type] = run_evaluator_list

            run_evaluator_set.categories[category_name] = run_evaluator_category
        self.repository.save(run_evaluator_set)
        return run_evaluator_set