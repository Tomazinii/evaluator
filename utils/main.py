from uuid import uuid4

from ragas import EvaluationDataset, SingleTurnSample
from teste import QueryResponseCategory, QueryResponseSet, RunEvaluatorSet


run_evaluator_set = RunEvaluatorSet(query_set_id=uuid4(), query_set_name="teste", query_set_llm="gemini-flash")

category = QueryResponseCategory(category_name="direct-query")
interaction = QueryResponseSet.create(query="qual a capital da frança?", expected_response="A capital da frança é parís", expected_context="",query_type="simple-query", generated_response = "A capital da frança é paris", retriaved_context = ["Paris é a capital da frança"])
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






