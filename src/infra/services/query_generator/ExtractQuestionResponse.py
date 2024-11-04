
import re

class ExtractQuestionResponse:
    
    @staticmethod
    def extract_questions_and_answers(response):
        # Regex simplificado para capturar perguntas e respostas sem formatação markdown
        pattern = r"Query:\s*(.*?)\s*Reference:\s*(.*?)\s*(?=Query:|$)"
        matches = re.findall(pattern, response, re.DOTALL)
        # Transformar a lista de correspondências em um dicionário de perguntas e respostas
        qa_pairs = [{"Query": question.strip(), "Reference": answer.strip()} for question, answer in matches]
        return qa_pairs