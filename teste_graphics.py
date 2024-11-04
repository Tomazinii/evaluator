import json
import matplotlib.pyplot as plt
import numpy as np
import os


reports_list = {
    "patters": {

        "naive": [
            "Report-RunEvaluatorSet-90a83b13-418a-4683-8d0f-6812c8ecf2aa-naive-dataset1",
            "Report-RunEvaluatorSet-90a83b13-418a-4683-8d0f-6812c8ecf2aa-naive-dataset2",
            "Report-RunEvaluatorSet-90a83b13-418a-4683-8d0f-6812c8ecf2aa-naive-dataset3"
            ],

        "naivehyde": [
            "Report-RunEvaluatorSet-90a83b13-418a-4683-8d0f-6812c8ecf2aa-naivehyde-dataset1",
            "Report-RunEvaluatorSet-90a83b13-418a-4683-8d0f-6812c8ecf2aa-naivehyde-dataset2",
            "Report-RunEvaluatorSet-90a83b13-418a-4683-8d0f-6812c8ecf2aa-naivehyde-dataset3"
            ],
        "rag-fusion": [
            "Report-RunEvaluatorSet-90a83b13-418a-4683-8d0f-6812c8ecf2aa-rag-fusion-dataset1",
            "Report-RunEvaluatorSet-90a83b13-418a-4683-8d0f-6812c8ecf2aa-naivehyde-dataset2",
            "Report-RunEvaluatorSet-90a83b13-418a-4683-8d0f-6812c8ecf2aa-naivehyde-dataset3"
            ]

    }
}




import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Estrutura dos dados de exemplo
reports_list = {
    "patterns": {
        "naive": [
        "Report-RunEvaluatorSet-3aba878b-9c7a-47a2-8484-1f40d5636e92-naive-rag-dataset1",
        "Report-RunEvaluatorSet-3aba878b-9c7a-47a2-8484-1f40d5636e92-naive-rag-dataset2",
        "Report-RunEvaluatorSet-3aba878b-9c7a-47a2-8484-1f40d5636e92-naive-rag-dataset3"
        ],
        "naivehyde": [
        "Report-RunEvaluatorSet-3aba878b-9c7a-47a2-8484-1f40d5636e92-naive-hyde-rag-dataset1",
        "Report-RunEvaluatorSet-3aba878b-9c7a-47a2-8484-1f40d5636e92-naive-hyde-rag-dataset2",
        "Report-RunEvaluatorSet-3aba878b-9c7a-47a2-8484-1f40d5636e92-naive-hyde-rag-dataset3"
        ],

        "crag": [
        "Report-RunEvaluatorSet-3aba878b-9c7a-47a2-8484-1f40d5636e92-crag-hyde-dataset1",
        "Report-RunEvaluatorSet-3aba878b-9c7a-47a2-8484-1f40d5636e92-crag-hyde-dataset2",
        "Report-RunEvaluatorSet-3aba878b-9c7a-47a2-8484-1f40d5636e92-crag-hyde-dataset3"
        ],
        "ragfusion": [
        "Report-RunEvaluatorSet-3aba878b-9c7a-47a2-8484-1f40d5636e92-rag-fusion-dataset1",
        "Report-RunEvaluatorSet-3aba878b-9c7a-47a2-8484-1f40d5636e92-rag-fusion-dataset2",
        "Report-RunEvaluatorSet-3aba878b-9c7a-47a2-8484-1f40d5636e92-rag-fusion-dataset3",
    ],
        "selfrag": [
        "Report-RunEvaluatorSet-3aba878b-9c7a-47a2-8484-1f40d5636e92-self-rag-dataset1",
        "Report-RunEvaluatorSet-3aba878b-9c7a-47a2-8484-1f40d5636e92-self-rag-dataset2",
        "Report-RunEvaluatorSet-3aba878b-9c7a-47a2-8484-1f40d5636e92-self-rag-dataset3"
        ]

        # Adicione outros patterns conforme necessário
    }
}




# target_metric = "context_recall"
# llm_graph_name = "Revocação de Contexto"

# target_metric = "faithfulness"
# llm_graph_name = "Fidelidade"

# target_metric = "answer_relevancy"
# llm_graph_name = "Relevância de Resposta"

target_metric = "llm_context_precision_without_reference"
llm_graph_name = "Precisão de Contexto"


# Função para calcular a média das métricas para um pattern
def calcular_media_pattern(reports):
    metricas = {
        "simple-query": [],
        "complex-query": [],
        "comparion-query": [],
        "multi-hop-query": [],
        "open_query": []
    }

    for report in reports:
        # Carregar cada JSON, simulado aqui como leitura de um dict
        # Para produção, use `json.load` para ler de arquivos

        base_dir = os.path.join(os.getcwd(), 'src', 'new_reports')
        file_path = os.path.join(base_dir, report)

        with open(file_path, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)

        interactions = data['interactions']

        for query_type, valores in interactions.items():
            metricas[query_type].append(valores)

    # Calcular a média para cada métrica
    medias = {}
    for query_type, valores in metricas.items():
        medias[query_type] = {m: np.mean([v[m] for v in valores]) for m in valores[0].keys()}

    return medias

# Calcular a média para cada pattern e consolidar em um dataset final
datasets_medias = {}
for pattern, reports in reports_list["patterns"].items():
    datasets_medias[pattern] = calcular_media_pattern(reports)

# Exibir o dataset consolidado para revisão
consolidated_df = pd.DataFrame(datasets_medias)


meses = ["naive-rag", "naive-hyde-rag", "crag-hyde", "rag-fusion", "self-rag"]
vagas_simple_query =    [datasets_medias["naive"]["simple-query"][target_metric], datasets_medias["naivehyde"]["simple-query"][target_metric], datasets_medias["crag"]["simple-query"][target_metric], datasets_medias["ragfusion"]["simple-query"][target_metric], datasets_medias["selfrag"]["simple-query"][target_metric]]
vagas_complex_query =   [datasets_medias["naive"]["complex-query"][target_metric], datasets_medias["naivehyde"]["complex-query"][target_metric],datasets_medias["crag"]["complex-query"][target_metric], datasets_medias["ragfusion"]["complex-query"][target_metric],  datasets_medias["selfrag"]["complex-query"][target_metric]]
vagas_comparion_query = [datasets_medias["naive"]["comparion-query"][target_metric] , datasets_medias["naivehyde"]["comparion-query"][target_metric] , datasets_medias["crag"]["comparion-query"][target_metric],  datasets_medias["ragfusion"]["comparion-query"][target_metric] , datasets_medias["selfrag"]["comparion-query"][target_metric]]
vagas_multi_hop =       [datasets_medias["naive"]["multi-hop-query"][target_metric], datasets_medias["naivehyde"]["multi-hop-query"][target_metric], datasets_medias["crag"]["multi-hop-query"][target_metric],datasets_medias["ragfusion"]["multi-hop-query"][target_metric], datasets_medias["selfrag"]["multi-hop-query"][target_metric]]
vagas_open_query =      [datasets_medias["naive"]["open_query"][target_metric], datasets_medias["naivehyde"]["open_query"][target_metric],  datasets_medias["crag"]["open_query"][target_metric],datasets_medias["ragfusion"]["open_query"][target_metric], datasets_medias["selfrag"]["open_query"][target_metric]]

x = np.arange(len(meses))  
largura = 0.10  

fig, ax = plt.subplots(figsize=(12, 6))
ax.bar(x - 2*largura, vagas_simple_query, largura, label='Consulta Simples', color='#92C5F9', edgecolor='#777777', hatch='//')
ax.bar(x - largura, vagas_complex_query, largura, label='Consulta Complexa', color='#AFDC8F', edgecolor='#777777', hatch='\\\\')
ax.bar(x, vagas_comparion_query, largura, label='Consulta de Comparação', color='#F8AE54', edgecolor='#777777', hatch='..')
ax.bar(x + 2*largura, vagas_multi_hop, largura, label='Constulta Multi-etapas', color='#B6A6E9', edgecolor='#777777', hatch='xx')
ax.bar(x + largura, vagas_open_query, largura, label='Consulta Aberta', color='#E0E0E0', edgecolor='#777777', hatch='++')

# Adiciona os rótulos, título e define o intervalo fixo do eixo Y

ax.set_xlabel('Padrão')
ax.set_ylabel('Pontuação')
ax.set_title(f'{llm_graph_name}')
ax.set_xticks(x)
ax.set_xticklabels(meses)
ax.set_ylim(0, 1)  # Define o intervalo do eixo Y entre 0 e 1
ax.legend(ncol=5, loc='upper center', bbox_to_anchor=(0.5, -0.15), frameon=False)

# Aumenta o espaço inferior da figura para acomodar a legenda
plt.subplots_adjust(bottom=0.25)

# Adiciona linhas horizontais em 0.2, 0.4, 0.6 e 0.8
for linha in [0.2, 0.4, 0.6, 0.8]:
    ax.axhline(y=linha, color='gray', linestyle='--', linewidth=0.7)

# Salva o gráfico como PNG
output_path = f"./{llm_graph_name}.png"
plt.savefig(output_path, format="png")
plt.close(fig)

output_path
