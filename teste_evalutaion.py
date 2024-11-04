import asyncio
from typing import List
from datasets import load_dataset
from ragas import EvaluationDataset
from ragas.metrics import LLMContextRecall, Faithfulness, NoiseSensitivity, ContextEntityRecall, ResponseRelevancy ,context_recall,LLMContextPrecisionWithoutReference
from ragas import evaluate, EvaluationDataset
from ragas.llms import LangchainLLMWrapper
from langchain_google_vertexai import ChatVertexAI, VertexAIEmbeddings
from ragas.run_config import RunConfig
from langchain_openai import ChatOpenAI
import os
import json
from uuid import uuid4
from ragas import EvaluationDataset, SingleTurnSample


import numpy as np



my_run_config = RunConfig(max_workers=15, timeout=120)
evaluator_llm = LangchainLLMWrapper(
    ChatVertexAI(model_name="gemini-1.5-pro", project="energygpt-421317", location="us-central1")
)
embeddings_service = VertexAIEmbeddings(
    model_name="text-multilingual-embedding-002", project="energygpt-421317", location="us-central1"
)
metrics = [Faithfulness(), LLMContextRecall(), LLMContextPrecisionWithoutReference(), ResponseRelevancy()]



case_name = "Legis"




data_source_list = [
    "RunEvaluatorSet-3aba878b-9c7a-47a2-8484-1f40d5636e92-crag-hyde-dataset1",
    "RunEvaluatorSet-3aba878b-9c7a-47a2-8484-1f40d5636e92-crag-hyde-dataset2",
    "RunEvaluatorSet-3aba878b-9c7a-47a2-8484-1f40d5636e92-crag-hyde-dataset3",
    "RunEvaluatorSet-3aba878b-9c7a-47a2-8484-1f40d5636e92-naive-hyde-rag-dataset1",
    "RunEvaluatorSet-3aba878b-9c7a-47a2-8484-1f40d5636e92-naive-hyde-rag-dataset2",
    "RunEvaluatorSet-3aba878b-9c7a-47a2-8484-1f40d5636e92-naive-hyde-rag-dataset3",
    "RunEvaluatorSet-3aba878b-9c7a-47a2-8484-1f40d5636e92-naive-rag-dataset1",
    "RunEvaluatorSet-3aba878b-9c7a-47a2-8484-1f40d5636e92-naive-rag-dataset2",
    "RunEvaluatorSet-3aba878b-9c7a-47a2-8484-1f40d5636e92-naive-rag-dataset3",
    "RunEvaluatorSet-3aba878b-9c7a-47a2-8484-1f40d5636e92-rag-fusion-dataset1",
    "RunEvaluatorSet-3aba878b-9c7a-47a2-8484-1f40d5636e92-rag-fusion-dataset2",
    "RunEvaluatorSet-3aba878b-9c7a-47a2-8484-1f40d5636e92-rag-fusion-dataset3",
    "RunEvaluatorSet-3aba878b-9c7a-47a2-8484-1f40d5636e92-self-rag-dataset1",
    "RunEvaluatorSet-3aba878b-9c7a-47a2-8484-1f40d5636e92-self-rag-dataset2",
    "RunEvaluatorSet-3aba878b-9c7a-47a2-8484-1f40d5636e92-self-rag-dataset3",
]

for source in data_source_list:
    base_dir = os.path.join(os.getcwd(), 'src', 'data')
    if not os.path.exists(base_dir):
            os.makedirs(base_dir)


report_data = {}



def repository(source, data_dict):
        try:
            base_dir = os.path.join(os.getcwd(), 'src', 'new_reports')
            
            if not os.path.exists(base_dir):
                os.makedirs(base_dir)
            
            file_path = os.path.join(base_dir, f"Report-{source}")

            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(data_dict, f, ensure_ascii=False, indent=4)
        except Exception as e:
            raise Exception(f"Erro ao salvar RunEvaluatorSet em arquivo JSON: {e}")



def mean(num: List):
    value = np.nanmean(num)
    return value


async def main():
    for source in data_source_list:
        print(f"start - {source}")
        base_dir = os.path.join(os.getcwd(), 'src', 'data')
        file_path = os.path.join(base_dir, source)

        with open(file_path, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)


        # interactions_type = list(data["categories"]["direct-query"]["interactions"].keys())
        interactions_type = ["simple-query","complex-query","comparion-query", "multi-hop-query","open_query"]

        interaction_dict = {
            source: case_name,
            "interactions":  {}
        }

        for interaction_type in interactions_type:
            print(f"{interaction_type}:")

            interactions_list = []
            samples = []


            for element in data["categories"]["direct-query"]["interactions"][interaction_type]:
                interaction = {
                    "query": element["query"],
                    "expected_response": element["reference"],
                    "generated_response": element["response"],
                    "query_type" : "simple-query",
                    "retrieved_context": element["retrieved_context"],
                }

                interactions_list.append(interaction)
            for interaction_element in interactions_list:
                sample = SingleTurnSample(
                            user_input=interaction_element["query"],
                            retrieved_contexts=interaction_element["retrieved_context"],
                            response=interaction_element["generated_response"],
                            reference=interaction_element["expected_response"],
                        )
            
                samples.append(sample)


            dataset = EvaluationDataset(samples=samples)
            result = evaluate(run_config=my_run_config,dataset=dataset, metrics=metrics, llm=evaluator_llm,embeddings=embeddings_service)
            df_resultados = result.to_pandas().to_dict(orient='list')

            result_dict = {
                    'faithfulness': float(mean(num=df_resultados['faithfulness'])),
                    'context_recall': float(mean(df_resultados['context_recall'])),
                    'llm_context_precision_without_reference': float(mean(df_resultados['llm_context_precision_without_reference'])),
                    'answer_relevancy': float(mean(df_resultados['answer_relevancy']))  
            }
            print(result_dict)
            interaction_dict["interactions"].update({interaction_type: result_dict})

        repository(source=source, data_dict=interaction_dict)


asyncio.run(main())