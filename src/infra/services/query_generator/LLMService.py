
from langchain_google_vertexai import ChatVertexAI, VertexAIEmbeddings

class LLMService:
    
    def __init__(self, llm_model_name="gemini-1.5-pro") -> None:
        self.llm = ChatVertexAI(model_name=llm_model_name, project="energygpt-421317")
    
    def invoke(self, prompt):
        return self.llm.invoke(prompt).content
        
    
 