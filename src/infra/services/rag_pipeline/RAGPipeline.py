from uuid import uuid4
from src.orchestrator.run_evaluator.entity.ResponseSet import ResponseSet
from src.orchestrator.services.rag_pipeline import IRAGPipeline, InputRagPipelineDto
import requests


class RAGPipelineService(IRAGPipeline):
    
    def __init__(self, rag_pipeline_url: str):
        """
        Inicializa o RAGPipelineService com o endpoint da pipeline RAG.

        Args:
            rag_pipeline_url (str): URL do endpoint HTTP da pipeline RAG.
        """
        self.rag_pipeline_url = rag_pipeline_url


    def execute(self, input: InputRagPipelineDto) -> ResponseSet:
        """
        Executa a pipeline RAG via requisição HTTP para a query fornecida.

        Args:
            input (InputRagPipelineDto): Dados de entrada contendo a query.

        Returns:
            ResponseSet: Resultado contendo a resposta gerada e o contexto recuperado.
        """
        try:
            # Monta o payload da requisição
            payload = {
                "query": input.user_input
            }

            response = requests.post(self.rag_pipeline_url, json=payload)

            response.raise_for_status()

            response_data = response.json()

            response_text = response_data.get('response', '')
            retrieved_context = response_data.get('retrieved_context', '')

            return ResponseSet(
                id=str(uuid4()),
                response=response_text,
                retrieved_context=retrieved_context
            )

        except requests.exceptions.RequestException as e:
            # Trata erros de requisição HTTP
            return ResponseSet(
                id=str(uuid4()),
                response=f"Erro ao executar a query via HTTP: {e}",
                retrieved_context=""
            )
        except ValueError as e:
            # Trata erros de decodificação JSON
            return ResponseSet(
                id=str(uuid4()),
                response=f"Erro ao decodificar a resposta JSON: {e}",
                retrieved_context=""
            )
        except Exception as e:
            # Trata quaisquer outros erros
            return ResponseSet(
                id=str(uuid4()),
                response=f"Erro inesperado ao executar a query: {e}",
                retrieved_context=""
            )