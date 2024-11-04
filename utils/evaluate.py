from datasets import load_dataset
# dataset = load_dataset("explodinggradients/amnesty_qa","english_v3")

from ragas import EvaluationDataset



from ragas.metrics import LLMContextRecall, Faithfulness, NoiseSensitivity, ContextEntityRecall, ResponseRelevancy 
from ragas import evaluate, EvaluationDataset
from ragas.llms import LangchainLLMWrapper
from langchain_google_vertexai import ChatVertexAI, VertexAIEmbeddings

from ragas.run_config import RunConfig


from uuid import uuid4

from ragas import EvaluationDataset, SingleTurnSample
from teste import QueryResponseCategory, QueryResponseSet, RunEvaluatorSet


run_evaluator_set = RunEvaluatorSet(query_set_id=uuid4(), query_set_name="teste", query_set_llm="gemini-flash")

category = QueryResponseCategory(category_name="direct-query")


# interaction = QueryResponseSet.create(
#     query="Where is the Eiffel Tower located?", 
#     expected_response="The Eiffel Tower is located in Paris.",
#     expected_context="",query_type="simple-query", 
#     generated_response = "The Eiffel Tower is located in Paris.", 
#     retriaved_context = ["The Eiffel Tower is located in Paris."])




# interaction = QueryResponseSet.create(
#     query="Quais são os objetivos do PROPDI?",
#     expected_response="Os objetivos do PROPDI são:\n• Proporcionar, por meio da inovação, o desenvolvimento tecnológico do setor elétrico brasileiro, preparando e empoderando tecnicamente as empresas reguladas para a transição energética;\n• Desenvolver e estimular a cultura da inovação no âmbito interno das empresas reguladas que, com base na sua obrigação legal de utilização de recursos em pesquisa, desenvolvimento e inovação, possam ser permanentemente atualizadas com o desenvolvimento tecnológico mundial;\n• Formar competências técnicas voltadas aos processos inovativos no setor elétrico brasileiro; e\n• Desenvolver soluções inovadoras em conjunto e consonância com o setor produtivo nacional, academia e institutos de pesquisa, voltadas às necessidades do setor elétrico.",
#     expected_context="**(Nota Técnica nº 0141/2021 – SPE/ANEEL, de 06/10/2021, Seção III.3.1)**",
#     query_type="simple-query",
#     generated_response="Os objetivos do PROPDI são:\n• Proporcionar, por meio da inovação, o desenvolvimento tecnológico do setor elétrico brasileiro, preparando e empoderando tecnicamente as empresas reguladas para a transição energética;\n• Desenvolver e estimular a cultura da inovação no âmbito interno das empresas reguladas que, com base na sua obrigação legal de utilização de recursos em pesquisa, desenvolvimento e inovação, possam ser permanentemente atualizadas com o desenvolvimento tecnológico mundial;\n• Formar competências técnicas voltadas aos processos inovativos no setor elétrico brasileiro; e\n• Desenvolver soluções inovadoras em conjunto e consonância com o setor produtivo nacional, academia e institutos de pesquisa, voltadas às necessidades do setor elétrico.",
#     retriaved_context=[
#         "### CAPÍTULO III - DOS MÓDULOS DO PROPDI",
#         "### MÓDULO 1: INTRODUÇÃO\n\n### SEÇÃO 1.1. OBJETIVOS DO PROPDI\n\n1. Os Procedimentos do Programa de Pesquisa, Desenvolvimento e Inovação — PROPDI são um guia determinativo de procedimentos dirigidos notadamente às empresas do setor elétrico reguladas pela ANEEL com obrigatoriedade de atendimento à Lei n.º 9.991, de 24 de julho de 2000.\n2. Os objetivos do PROPDI são:\n• Identificar e definir as Diretrizes e procedimentos para elaboração e execução da Estratégia, Portfólio, Programas, e Projetos de Pesquisa, Desenvolvimento e Inovação do Programa de Pesquisa, Desenvolvimento e Inovação— PDI do Setor Elétrico Brasileiro — SEB;\n• Especificar e caracterizar as modalidades de aplicação dos recursos compulsórios no âmbito do Programa regulado pela ANEEL; e\n• Estabelecer as regras e procedimentos operacionais de cumprimento da obrigação de aplicação de recursos em PDI, mediante sistemáticas de execução, monitoramento, avaliação, acompanhamento dos resultados e dos benefícios alcançados, reconhecimento e prestação de contas dos investimentos realizados.",
#         "estratégicas de ação, mas mantendo-se a estrutura dos procedimentos do PROPDI. O PEQuI tratará dos objetivos estratégicos, bem como seus indicadores de impacto e resultado de monitoramento e metas específicas de cumprimento esperadas para as empresas reguladas, e contará com o PROPDI como seu principal instrumento de acompanhamento."
#     ]
# )

interaction = QueryResponseSet.create(
    query="Quais são os objetivos do PROPDI?",
    expected_response= "Os objetivos do PROPDI s\u00e3o:\n\u2022 Identificar e definir as Diretrizes e procedimentos para elabora\u00e7\u00e3o e execu\u00e7\u00e3o da Estrat\u00e9gia, Portf\u00f3lio, Programas, e Projetos de Pesquisa, Desenvolvimento e Inova\u00e7\u00e3o do Programa de Pesquisa, Desenvolvimento e Inova\u00e7\u00e3o\u2014 PDI do Setor El\u00e9trico Brasileiro \u2014 SEB;\n\u2022 Especificar e caracterizar as modalidades de aplica\u00e7\u00e3o dos recursos compuls\u00f3rios no \u00e2mbito do Programa regulado pela ANEEL; e\n\u2022 Estabelecer as regras e procedimentos operacionais de cumprimento da obriga\u00e7\u00e3o de aplica\u00e7\u00e3o de recursos em PDI, mediante sistem\u00e1ticas de execu\u00e7\u00e3o, monitoramento, avalia\u00e7\u00e3o, acompanhamento dos resultados e dos benef\u00edcios alcan\u00e7ados, reconhecimento e presta\u00e7\u00e3o de contas dos investimentos realizados.",
    expected_context="**(Nota Técnica nº 0141/2021 – SPE/ANEEL, de 06/10/2021, Seção III.3.1)**",
    query_type="simple-query",
    generated_response= "**(Nota T\u00e9cnica n\u00ba 0141/2021 \u2013 SPE/ANEEL, de 06/10/2021, Se\u00e7\u00e3o III.3.1)** Os objetivos do PROPDI s\u00e3o:\n\n* **Proporcionar, por meio da inova\u00e7\u00e3o, o desenvolvimento tecnol\u00f3gico do setor el\u00e9trico brasileiro, preparando e empoderando tecnicamente as empresas reguladas para a transi\u00e7\u00e3o energ\u00e9tica;**\n* **Desenvolver e estimular a cultura da inova\u00e7\u00e3o no \u00e2mbito interno das empresas reguladas que, com base na sua obriga\u00e7\u00e3o legal de utiliza\u00e7\u00e3o de recursos em pesquisa, desenvolvimento e inova\u00e7\u00e3o, possam ser permanentemente atualizadas com o desenvolvimento tecnol\u00f3gico mundial;**\n* **Formar compet\u00eancias t\u00e9cnicas voltadas aos processos inovativos no setor el\u00e9trico brasileiro;** e\n* **Desenvolver solu\u00e7\u00f5es inovadoras em conjunto e conson\u00e2ncia com o setor produtivo nacional, academia e institutos de pesquisa, voltadas \u00e0s necessidades do setor el\u00e9trico.** \n",
    retriaved_context = [
        "### CAP\u00cdTULO III - DOS M\u00d3DULOS DO PROPDI",
        "### M\u00d3DULO 1: INTRODU\u00c7\u00c3O\n\n### SE\u00c7\u00c3O 1.1. OBJETIVOS DO PROPDI\n\n1. Os Procedimentos do Programa de Pesquisa, Desenvolvimento e Inova\u00e7\u00e3o \u2014 PROPDI s\u00e3o um guia\r\ndeterminativo de procedimentos dirigidos notadamente \u00e0s empresas do setor el\u00e9trico reguladas pela ANEEL com\r\nobrigatoriedade de atendimento \u00e0 Lei n.\u00ba 9.991, de 24 de julho de 2000.\r\n2. Os objetivos do PROPDI s\u00e3o:\r\n\u2022 Identificar e definir as Diretrizes e procedimentos para elabora\u00e7\u00e3o e execu\u00e7\u00e3o da Estrat\u00e9gia, Portf\u00f3lio,\r\nProgramas, e Projetos de Pesquisa, Desenvolvimento e Inova\u00e7\u00e3o do Programa de Pesquisa,\r\nDesenvolvimento e Inova\u00e7\u00e3o\u2014 PDI do Setor El\u00e9trico Brasileiro \u2014 SEB;\r\n\u2022 Especificar e caracterizar as modalidades de aplica\u00e7\u00e3o dos recursos compuls\u00f3rios no \u00e2mbito do Programa\r\nregulado pela ANEEL; e\r\n\u2022 Estabelecer as regras e procedimentos operacionais de cumprimento da obriga\u00e7\u00e3o de aplica\u00e7\u00e3o de recursos\r\nem PDI, mediante sistem\u00e1ticas de execu\u00e7\u00e3o, monitoramento, avalia\u00e7\u00e3o, acompanhamento dos resultados\r\ne dos benef\u00edcios alcan\u00e7ados, reconhecimento e presta\u00e7\u00e3o de contas dos investimentos realizados.",
        "estrat\u00e9gicas de a\u00e7\u00e3o, mas mantendo-se a estrutura dos procedimentos do PROPDI. O PEQuI tratar\u00e1 dos\r\nobjetivos estrat\u00e9gicos, bem como seus indicadores de impacto e resultado de monitoramento e metas\r\nespec\u00edficas de cumprimento esperadas para as empresas reguladas, e contar\u00e1 com o PROPDI como seu\r\nprincipal instrumento de acompanhamento.\r\nFigura 3 \u2014 Mapa Estrat\u00e9gico do Programa de PDI ANEEL com a representa\u00e7\u00e3o do PEQuI.\r\n39. Vale mencionar tamb\u00e9m o conceito de inova\u00e7\u00e3o adotado no PROPDI. Alguns \u00f3rg\u00e3os de\r\nfomento, tais como FINEP e BNDES, utilizam o conceito de inova\u00e7\u00e3o segundo o Manual de Oslo, que a\r\ndefine como \u201ca introdu\u00e7\u00e3o de um bem ou servi\u00e7o novo, ou significativamente melhorado, no que se refere\r\n\u00e0s suas caracter\u00edsticas ou usos previstos, ou ainda, \u00e0 implementa\u00e7\u00e3o de m\u00e9todos ou processos de\r\nprodu\u00e7\u00e3o, distribui\u00e7\u00e3o, marketing ou organizacionais novos, ou significativamente melhorados\u201d. No caso\r\ndo PROPDI este conceito coincide com o definido na Lei n.\u00ba 13.243/2016, que estabelece o Novo Marco\r\nLegal de CTI, tal como transcrito no par\u00e1grafo 4 desta Nota T\u00e9cnica, sendo que os processos de\r\ndistribui\u00e7\u00e3o, marketing ou organizacionais n\u00e3o s\u00e3o considerados para os fins do programa regulado pela\r\nANEEL.\r\n40. O PDI incorpora, adicionalmente do Novo Marco Legal de CTI e do Decreto n.\u00ba 9.283/2018,\r\nque o regulamenta, v\u00e1rios comandos para criar um ambiente mais favor\u00e1vel \u00e0 pesquisa, desenvolvimento\r\ne inova\u00e7\u00e3o nas empresas, nas universidades e nos institutos de pesquisa. Tais comandos s\u00e3o\r\noportunidades que permitir\u00e3o alavancar economicamente o setor industrial e a sociedade, atrav\u00e9s de\r\nP\r\nM O D E O E P\r\nE I\r\nP\r\nI\r\nP P\r\nI I\r\nN\u00famero: 48547.001418/2021-00\r\nDOCUMENTO ASSINADO DIGITALMENTE.\r\nConsulte a autenticidade deste documento em http://sicnet2.aneel.gov.br/sicnetweb/v.aspx, informando o c\u00f3digo de verifica\u00e7\u00e3o 05D5E9D6006168C7\r\nN\u00famero: 48547.001418/2021-00",
        "aplica\u00e7\u00e3o dos recursos compuls\u00f3rios, al\u00e9m da ado\u00e7\u00e3o de crit\u00e9rios de an\u00e1lise e avalia\u00e7\u00e3o de seu\r\ndesempenho, baseado em resultados e medidos atrav\u00e9s de indicadores pr\u00e9-definidos.\r\nIII.2.1 \u2014 Estrutura e componentes do PROPDI\r\n42. O PROPDI ser\u00e1 composto pelos seguintes m\u00f3dulos:\r\nI. M\u00f3dulo 1: Introdu\u00e7\u00e3o\r\nII. M\u00f3dulo 2: Diretrizes do Programa de PDI ANEEL\r\nIII. M\u00f3dulo 3: Instrumentos de inova\u00e7\u00e3o\r\nIV. M\u00f3dulo 4: Execu\u00e7\u00e3o, Monitoramento e Avalia\u00e7\u00e3o\r\nV. M\u00f3dulo 5: Presta\u00e7\u00e3o de Contas\r\nVI. M\u00f3dulo 6: Comunica\u00e7\u00e3o\r\nVII. M\u00f3dulo 7: Per\u00edodo de Transi\u00e7\u00e3o\r\nM\u00f3dulo 1: Introdu\u00e7\u00e3o\r\n43. O \u201cM\u00f3dulo 1 \u2014 Introdu\u00e7\u00e3o\u201d apresenta uma vis\u00e3o geral dos Procedimentos, com os\r\nobjetivos e a composi\u00e7\u00e3o dos m\u00f3dulos que o integram, al\u00e9m de incluir os acr\u00f4nimos ou abreviaturas\r\nutilizadas.\r\n44. Os objetivos do PROPDI s\u00e3o:\r\na) Identificar e definir as Diretrizes e procedimentos para elabora\u00e7\u00e3o e execu\u00e7\u00e3o da\r\nEstrat\u00e9gia, Portf\u00f3lio, Plano e Projetos de Pesquisa, Desenvolvimento e Inova\u00e7\u00e3o do\r\nPrograma de Pesquisa, Desenvolvimento e Inova\u00e7\u00e3o do setor el\u00e9trico (PDI);\r\nb) Especificar e caracterizar as modalidades de aplica\u00e7\u00e3o dos recursos compuls\u00f3rios no\r\n\u00e2mbito do Programa regulado pela ANEEL; e\r\nc) Estabelecer as regras e os procedimentos operacionais de cumprimento da obriga\u00e7\u00e3o\r\nde aplica\u00e7\u00e3o de recursos em PDI, mediante sistem\u00e1ticas de execu\u00e7\u00e3o, monitoramento,\r\navalia\u00e7\u00e3o, reconhecimento e presta\u00e7\u00e3o de contas dos investimentos realizados.\r\nM\u00f3dulo 2: Diretrizes do PDI ANEEL\r\n45. Para abordar as Diretrizes do PDI, o \u201cM\u00f3dulo 2 \u2014 Diretrizes do PDI ANEEL\u201d discorre\r\ninicialmente sobre seus Objetivos, Princ\u00edpios, Conceitos e Aspectos Legais.\r\n46. No tema propriamente dito, explicita cada uma das Diretrizes, sumarizadas no Item 37\r\ndesta Nota T\u00e9cnica, com car\u00e1ter determinativo e dever\u00e1 ser observado continuamente como balizador\r\nDOCUMENTO ASSINADO DIGITALMENTE.",
        "### III \u2014 DA AN\u00c1LISE\n\n### III.3 \u2014 O PROPDI\n\nIII.3.1 \u2014 Considera\u00e7\u00f5es Iniciais\r\n30. Os Procedimentos do Programa de Pesquisa, Desenvolvimento e Inova\u00e7\u00e3o regulado pela\r\nANEEL (PROPDI) s\u00e3o um guia determinativo de procedimentos dirigidos \u00e0s empresas do setor el\u00e9trico\r\nreguladas pela ANEEL com obrigatoriedade de atendimento \u00e0 Lei n.\u00ba 9.991, de 24 de julho de 2000.\r\n31. Os objetivos do Programa de PDI s\u00e3o:\r\na) Proporcionar, por meio da inova\u00e7\u00e3o, o desenvolvimento tecnol\u00f3gico do setor el\u00e9trico\r\nbrasileiro preparando e empoderando tecnicamente as empresas reguladas para a\r\ntransi\u00e7\u00e3o energ\u00e9tica;\r\nb) Desenvolver e estimular a cultura da inova\u00e7\u00e3o no \u00e2mbito interno das empresas reguladas\r\nque, com base na sua obriga\u00e7\u00e3o legal de utiliza\u00e7\u00e3o de recursos em pesquisa,\r\ndesenvolvimento e inova\u00e7\u00e3o, possam ser permanentemente atualizadas com o\r\ndesenvolvimento tecnol\u00f3gico mundial;\r\nc) Formar compet\u00eancias t\u00e9cnicas voltadas aos processos inovativos no setor el\u00e9trico\r\nbrasileiro; e\r\nDOCUMENTO ASSINADO DIGITALMENTE.\r\nConsulte a autenticidade deste documento em http://sicnet2.aneel.gov.br/sicnetweb/v.aspx, informando o c\u00f3digo de verifica\u00e7\u00e3o 05D5E9D6006168C7\r\nN\u00famero: 48547.001418/2021-00\r\nP. 7 da NOTA T\u00c9CNICA N\u00ba 0141/2021 \u2013 SPE/ANEEL, de 06/10/2021.\r\nd) Desenvolver solu\u00e7\u00f5es inovadoras em conjunto e conson\u00e2ncia com o setor produtivo\r\nnacional, academia e institutos de pesquisa, voltadas \u00e0s necessidades do setor el\u00e9trico.\r\n32. A principal mudan\u00e7a estrutural em rela\u00e7\u00e3o aos procedimentos anteriores regulados pela\r\nANEEL \u00e9 que a Inova\u00e7\u00e3o \u00e9 a principal finalidade do PROPDI, que utilizar\u00e1 como meio os instrumentos\r\npertinentes de pesquisa e desenvolvimento j\u00e1 regulados, acrescidos de outros que possam representar\r\nnovas formas de aplica\u00e7\u00e3o, tais como startups, fundos de investimento, planos de gest\u00e3o da inova\u00e7\u00e3o,\r\ndentre outros.\r\n33. Nesse contexto, o conceito anterior de Programa de P&D, onde os investimentos"
    ],
)

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







my_run_config = RunConfig(max_workers=64, timeout=60)


evaluator_llm = LangchainLLMWrapper(ChatVertexAI(model_name="gemini-1.5-pro", project="energygpt-421317"))
embeddings_service = VertexAIEmbeddings(model_name="text-multilingual-embedding-002", project="energygpt-421317")

metrics = [LLMContextRecall(),Faithfulness(), NoiseSensitivity(), ContextEntityRecall(), ResponseRelevancy()]
results = evaluate(run_config=my_run_config,dataset=dataset, metrics=metrics, llm=evaluator_llm,embeddings=embeddings_service)
print("RESULT",results)
