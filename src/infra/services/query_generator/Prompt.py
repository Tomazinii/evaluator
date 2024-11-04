

class PromptQueryGenerator:

    def simple_query_prompt(self, data_source: str, n: int):
        prompt = (
        f"Baseando-se nos dados fornecidos abaixo, gere {n} perguntas simples e suas respectivas respostas. "
        f"As perguntas devem ser diretas e objetivas, focadas em obter uma única informação clara. "
        f"Dados: {data_source}\n"
        "Cada pergunta deve ser seguida de uma resposta, sem formatação Markdown. Formato de saída:\n"
        "Query: <aqui a pergunta gerada>\n"
        "Reference: <aqui a resposta gerada>\n"
    )
        return prompt
    

    def complex_query_prompt(self, data_source: str, n: int):
        prompt = (
            f"Com base nos dados a seguir, gere {n} perguntas complexas e suas respostas. "
            f"As perguntas devem explorar múltiplos aspectos dos dados e as respostas devem ser detalhadas, "
            "com explicações que forneçam contexto adicional.\n"
            f"Dados: {data_source}\n"
            "Cada pergunta deve ser seguida de uma resposta, sem formatação Markdown. Formato de saída:\n"
            "Query: <aqui a pergunta gerada>\n"
            "Reference: <aqui a resposta gerada>\n"
        )
        return prompt
    
    
    def multi_hop_query_prompt(self, data_source: str, n: int):
        prompt = (
            f"Com base nos dados a seguir, gere {n} perguntas que envolvam múltiplas etapas de raciocínio. "
            f"As perguntas devem conectar diferentes informações e as respostas devem demonstrar o caminho lógico "
            "que leva à conclusão.\n"
            f"Dados: {data_source}\n"
            "Cada pergunta deve ser seguida de uma resposta, sem formatação Markdown. Formato de saída:\n"
            "Query: <aqui a pergunta gerada>\n"
            "Reference: <aqui a resposta gerada>\n"
        )
        return prompt 
    

    def comparison_query_prompt(self, data_source: str, n: int):
        prompt = (
            f"Com base nos dados a seguir, gere {n} perguntas que envolvam comparações entre diferentes entidades ou conceitos. "
            f"As respostas devem destacar as principais semelhanças e diferenças entre os itens comparados.\n"
            f"Dados: {data_source}\n"
            "Cada pergunta deve ser seguida de uma resposta, sem formatação Markdown. Formato de saída:\n"
            "Query: <aqui a pergunta gerada>\n"
            "Reference: <aqui a resposta gerada>\n"
        )
        return prompt
    

    def multi_turn_query_prompt(self, data_source,n):
        prompt = (
        f"Com base nos dados fornecidos a seguir, gere {n} perguntas do tipos multi turn e suas respectivas respostas."
        f"Os dados são: {data_source}\n"
        "Cada pergunta deve ser seguida de uma resposta, sem formatação Markdown. Formato de saída:\n"
        "Query: <aqui a pergunta gerada>\n"
        "Reference: <aqui a resposta gerada>\n"
    )
        return prompt
    

    def open_query_prompt(self, data_source, n):

        prompt = (
        f"Com base nos dados a seguir, gere {n} perguntas abertas e suas respostas detalhadas. "
        f"As perguntas devem ser amplas e encorajar respostas exploratórias, fornecendo insights ou diferentes interpretações dos dados.\n"
        f"Dados: {data_source}\n"
        "Cada pergunta deve ser seguida de uma resposta, sem formatação Markdown. Formato de saída:\n"
        "Query: <aqui a pergunta gerada>\n"
        "Reference: <aqui a resposta gerada>\n"
    )
        return prompt
    

    def multi_query_prompt(self, data_source, n):
        prompt = (
        f"Com base nos dados a seguir, gere uma interação de múltiplas queries "
        f"com {n} perguntas e respostas integradas.\n"
        f"Dados: {data_source}\n"
        "Cada pergunta deve ser seguida de uma resposta, sem formatação Markdown. Formato de saída:\n"
        "Query: <aqui a pergunta gerada>\n"
        "Reference: <aqui a resposta gerada>\n"
    )
        return prompt