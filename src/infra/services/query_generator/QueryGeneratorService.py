import re
from typing import Dict
from src.synthesize.query.entity.QuerySet import QueryCategory
from src.synthesize.query.services.QueryGeneratorServiceInterface import IQueryGeneratorService
from langchain_google_vertexai import ChatVertexAI, VertexAIEmbeddings
from src.infra.services.query_generator.Queries import DirectQuery, FileManipulationQuery

class QueryGeneratorService(IQueryGeneratorService, DirectQuery, FileManipulationQuery):

    def generate(self, data_source, n: int) -> Dict[str, QueryCategory]:
        print("Start simple_query")
        self.simple_query(data_source=data_source, n=n)
        print("Start complex_query")
        self.complex_query(data_source=data_source, n=n)
        print("Start complex_query")
        self.comparison_query(data_source=data_source, n=n)
        print("Start comparison_query")
        self.multi_hop_query(data_source=data_source, n=n)
        print("Start multi_hop_query")
        self.open_query(data_source=data_source, n=n)
        print("Start open_query")
        self.multi_query(data_source=data_source, n=n)
        return self.categories


