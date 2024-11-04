from src.synthesize.query.entity.QueryBase import QueryBase
from uuid import uuid4
from src.synthesize.query.entity.QuerySet import QueryCategory
from src.infra.services.query_generator.LLMService import LLMService
from src.infra.services.query_generator.Prompt import PromptQueryGenerator
from src.infra.services.query_generator.ExtractQuestionResponse import ExtractQuestionResponse 
from typing import Dict

class BaseQuery:
    def __init__(self):
        self.llm = LLMService()
        self.prompt = PromptQueryGenerator()
        self.extract = ExtractQuestionResponse()
        self.categories: Dict[str, QueryCategory]  = {}
        
        

class DirectQuery(BaseQuery):
    
    def __init__(self):
        super().__init__()
        self.category_name = "direct-query"
        
        
    def simple_query(self, data_source, n=1):
            prompt = self.prompt.simple_query_prompt(data_source, n)
            response = self.llm.invoke(prompt)
            extract_qr = self.extract.extract_questions_and_answers(response)

            if self.category_name not in self.categories:
                self.categories[self.category_name] = QueryCategory.create(category_name=self.category_name)
            query_base = [QueryBase(query=element["Query"], query_type="simple-query", reference=element["Reference"], id=uuid4()) for element in extract_qr]
            self.categories[self.category_name].set_interaction(interaction_type="simple-query", interaction=query_base)
            

    def complex_query(self, data_source, n=1):
        
        prompt = self.prompt.complex_query_prompt(data_source, n)
        response = self.llm.invoke(prompt)
        extract_qr = self.extract.extract_questions_and_answers(response)

        if self.category_name not in self.categories:
            self.categories[self.category_name] = QueryCategory.create(category_name=self.category_name)
        query_base = [QueryBase(query=element["Query"], query_type="complex-query", reference=element["Reference"], id=uuid4()) for element in extract_qr]
        self.categories[self.category_name].set_interaction(interaction_type="complex-query", interaction=query_base)

    
    def multi_hop_query(self, data_source, n=1):
        prompt = self.prompt.multi_hop_query_prompt(data_source, n)
        response = self.llm.invoke(prompt)
        extract_qr = self.extract.extract_questions_and_answers(response)

        if self.category_name not in self.categories:
            self.categories[self.category_name] = QueryCategory.create(category_name=self.category_name)
        query_base = [QueryBase(query=element["Query"], query_type="multi-hop-query", reference=element["Reference"], id=uuid4()) for element in extract_qr]
        self.categories[self.category_name].set_interaction(interaction_type="multi-hop-query", interaction=query_base)

    
    def comparison_query(self, data_source, n=1):
        prompt = self.prompt.comparison_query_prompt(data_source, n)
        response = self.llm.invoke(prompt)
        extract_qr = self.extract.extract_questions_and_answers(response)

        if self.category_name not in self.categories:
            self.categories[self.category_name] = QueryCategory.create(category_name=self.category_name)
        query_base = [QueryBase(query=element["Query"], query_type="comparion-query", reference=element["Reference"], id=uuid4()) for element in extract_qr]
        self.categories[self.category_name].set_interaction(interaction_type="comparion-query", interaction=query_base)


    def multi_turn_query(self, data_source, n=1):
        pass

    def open_query(self, data_source, n=1):
        prompt = self.prompt.open_query_prompt(data_source, n)
        response = self.llm.invoke(prompt)
        extract_qr = self.extract.extract_questions_and_answers(response)

        if self.category_name not in self.categories:
            self.categories[self.category_name] = QueryCategory.create(category_name=self.category_name)
        query_base = [QueryBase(query=element["Query"], query_type="open_query", reference=element["Reference"], id=uuid4()) for element in extract_qr]
        self.categories[self.category_name].set_interaction(interaction_type="open_query", interaction=query_base)


    def multi_query(self, data_source, n=1):
        prompt = self.prompt.multi_query_prompt(data_source, n)
        response = self.llm.invoke(prompt)
        extract_qr = self.extract.extract_questions_and_answers(response)

        if self.category_name not in self.categories:
            self.categories[self.category_name] = QueryCategory.create(category_name=self.category_name)
        query_base = [QueryBase(query=element["Query"], query_type="multi-query", reference=element["Reference"], id=uuid4()) for element in extract_qr]
        self.categories[self.category_name].set_interaction(interaction_type="multi-query", interaction=query_base)



class FileManipulationQuery(BaseQuery):

    def input_file_query(self):
        pass

    def input_file_command(self):
        pass

    def input_file_summary(self):
        pass
    
    
class CommandsAndTaskInput:

    def input_command(self):
        pass

    def command_to_action(self):
        pass

    def command_search(self):
        pass

    def multi_command(self):
        pass
    

class FeedbackInteraction:

    def clarification_request(self):
        pass

    
class MultiModalInteraction:

    def image(self):
        pass

    def input_audio(self):
        pass


class ConversationControlInteraction:
    
    def topic_change_input(self):
        pass
    
    def return_to_previous_topic(self):
        pass