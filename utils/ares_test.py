

from ares import ARES

synth_config = { 
    "document_filepaths": ["nq_labeled_output.tsv"],
    "few_shot_prompt_filenames": ["nq_few_shot_prompt_for_synthetic_query_generation.tsv"],
    "synthetic_queries_filenames": ["synthetic_queries_1.tsv"], 
    "model_choice": "gpt-3.5-turbo-1106",
    "documents_sampled": 1000,
    "vllm": False,
    "host_url": "None"
}

ares = ARES(synthetic_query_generator=synth_config)
results = ares.generate_synthetic_data()
print(results)