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
from utils.teste import QueryResponseCategory, QueryResponseSet, RunEvaluatorSet


run_evaluator_set = RunEvaluatorSet(query_set_id=uuid4(), query_set_name="teste", query_set_llm="gemini-flash")

category = QueryResponseCategory(category_name="direct-query")


base_dir = os.path.join(os.getcwd(), 'src', 'data')

if not os.path.exists(base_dir):
        os.makedirs(base_dir)

id = "90a83b13-418a-4683-8d0f-6812c8ecf2aa"

file_path = os.path.join(base_dir, f"RunEvaluatorSet-{(id)}")

with open(file_path, 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)


 
interactions_list = []
for element in data["categories"]["direct-query"]["interactions"]["simple-query"]:

    
    interaction = QueryResponseSet.create(
        query=element["query"],
        expected_response=element["reference"],
        generated_response=element["response"],
        expected_context=None,
        query_type="simple-query",
        retriaved_context = element["retrieved_context"],
    )

    interactions_list.append(interaction)


for interaction in interactions_list:
    category.set_interaction(interaction_type=interaction.query_type, interaction=interaction)


run_evaluator_set.set_category(category)

categories = run_evaluator_set.categories.items()

samples = []


for key, value in categories:
    interaction_category = value.interactions.items()
    for interaction_type, interactions in interaction_category:
        for interaction in interactions:
            sample1 = SingleTurnSample(
                user_input=interaction.query,
                retrieved_contexts=interaction.retriaved_context,
                response=interaction.generated_response,
                reference=interaction.expected_response,
            )
            samples.append(sample1)



dataset = EvaluationDataset(samples=samples)

my_run_config = RunConfig(max_workers=3, timeout=120)

evaluator_llm = LangchainLLMWrapper(ChatVertexAI(model_name="gemini-1.5-pro", project="energygpt-421317"))
embeddings_service = VertexAIEmbeddings(model_name="text-multilingual-embedding-002", project="energygpt-421317")

metrics = [Faithfulness(), LLMContextRecall(), LLMContextPrecisionWithoutReference(), ResponseRelevancy()]

results = evaluate(run_config=my_run_config,dataset=dataset, metrics=metrics, llm=evaluator_llm,embeddings=embeddings_service)

print("RESULT",results)


    
