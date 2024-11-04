


import datetime
import json
import os
from uuid import uuid4
from src.orchestrator.run_evaluator.entity.RunEvaluateSet import RunEvaluatorSet
from src.orchestrator.run_evaluator.entity.RunEvaluatorBase import RunEvaluatorBase
from src.orchestrator.run_evaluator.entity.RunEvaluatorCategory import RunEvaluatorCategory
from src.orchestrator.run_evaluator.repository.RunEvaluatorRepository import IRunEvaluatorRepository


class JsonFileRunEvaluatorSetRepository(IRunEvaluatorRepository):
    def __init__(self, pattern = None, dataset_num = None):
        self.pattern = pattern
        self.dataset_num = dataset_num


    def save(self, run_evaluator_set: RunEvaluatorSet):
        try:
            base_dir = os.path.join(os.getcwd(), 'src', 'data')
            
            if not os.path.exists(base_dir):
                os.makedirs(base_dir)
            
            file_path = os.path.join(base_dir, f"RunEvaluatorSet-{(run_evaluator_set.id)}-{self.pattern}-{self.dataset_num}")

            # with open(file_path, 'w') as json_file:
            #     json.dump(input.to_json(), json_file, indent=4)
        
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(run_evaluator_set.to_json(), f, ensure_ascii=False, indent=4)
        except Exception as e:
            raise Exception(f"Erro ao salvar RunEvaluatorSet em arquivo JSON: {e}")
        


    def find_by_id(self, id: str) -> RunEvaluatorSet:
        try:
            base_dir = os.path.join(os.getcwd(), 'src', 'data')

            if not os.path.exists(base_dir):
                os.makedirs(base_dir)
            if(self.dataset_num == None or self.pattern == None):
                file_path = os.path.join(base_dir, f"RunEvaluatorSet-{(id)}")
            else:
                file_path = os.path.join(base_dir, f"RunEvaluatorSet-{(id)}-{self.pattern}-{self.dataset_num}")

            with open(file_path, 'r', encoding='utf-8') as json_file:
                data = json.load(json_file)

            # Parseando o JSON e criando o objeto RunEvaluatorSet
            run_evaluator_set_id = data['id']
            query_set_name = data['query_set_name']
            llm_model = data['llm_model']
            source = data['source']
            created_at_str = data['created_at']
            created_at = datetime.datetime.fromisoformat(created_at_str)

            categories_data = data['categories']
            categories = {}
            for category_key, category_value in categories_data.items():
                category_id = category_value['id']
                category_name = category_value['category_name']
                interactions_data = category_value['interactions']

                interactions = {}
                for interaction_key, interaction_list in interactions_data.items():
                    interaction_objects = []
                    for interaction_dict in interaction_list:
                        interaction_id = interaction_dict['id']
                        query_type = interaction_dict['query_type']
                        reference = interaction_dict.get('reference', None)
                        query = interaction_dict['query']
                        response = interaction_dict['response']
                        retrieved_context = interaction_dict['retrieved_context']

                        run_evaluator_base = RunEvaluatorBase(
                            id=interaction_id,
                            query_type=query_type,
                            reference=reference,
                            query=query,
                            response=response,
                            retrieved_context=retrieved_context
                        )
                        interaction_objects.append(run_evaluator_base)

                    interactions[interaction_key] = interaction_objects

                run_evaluator_category = RunEvaluatorCategory(
                    id=category_id,
                    category_name=category_name,
                    interactions=interactions
                )

                categories[category_key] = run_evaluator_category

            run_evaluator_set = RunEvaluatorSet(
                id=run_evaluator_set_id,
                query_set_name=query_set_name,
                llm_model=llm_model,
                source=source,
                created_at=created_at,
                categories=categories
            )

            return run_evaluator_set

        except Exception as e:
            raise Exception(f"Erro ao carregar RunEvaluatorSet do arquivo JSON: {e}")

