from src.synthesize.query.repository.QuerySource import IQuerySource
import os
import pandas as pd

class CSVQuerySourceRepository(IQuerySource):
    
    def get_source_data(self, file_name):
        csv_file_path = os.path.join(os.getcwd(), 'src', 'data_source',f'{file_name}.csv')
        if not os.path.exists(csv_file_path):
            raise FileNotFoundError(f"O arquivo CSV não foi encontrado: {csv_file_path}")
        data = pd.read_csv(csv_file_path)
        if data.empty:
            raise ValueError(f"Nenhum dado encontrado para o filename")
        
        return data.to_string()