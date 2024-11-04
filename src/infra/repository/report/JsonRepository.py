from src.evaluator.entity.EvaluatorSet import EvaluatorSet
from src.report.report.repository.ReportRepository import IReportRepository
import os

import json


class JSONRepository(IReportRepository):
    def __init__(self, dataset_num, pattern) -> None:
        self.dataset_num = dataset_num
        self.pattern = pattern
        
    def save(self, input: EvaluatorSet):
        base_dir = os.path.join(os.getcwd(), 'src', 'data')
        if not os.path.exists(base_dir):
            os.makedirs(base_dir)
        
        file_path = os.path.join(base_dir,f"Report_repository-{str(input.id)}-{self.dataset_num}-{self.pattern}")

        with open(file_path, 'w') as json_file:
            json.dump(input.to_json(), json_file, indent=4)
    
