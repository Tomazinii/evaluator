import matplotlib.pyplot as plt
import numpy as np

# Dados fictícios - substitua pelos valores reais conforme necessário
meses = ["naive-rag", "naive-hyde-rag", "crag-hyde", "rag-fusion", "self-rag"]
vagas_simple_query =    [0.952072, 0.94003, 0.952072, 0.952072, 0.952072]
vagas_complex_query =   [0.88447, 0.884472,0.877470, 0.884472,  0.8844728]
vagas_comparion_query = [0.8765, 0.8737194,0.887114,  0.87429949,0.87981]
vagas_multi_hop =       [0.897725, 0.87700, 0.877,0.884514, 0.8770]
vagas_open_query =      [0.870, 0.87019,  0.87700, 0.870067, 0.87382868]

# Configurações do gráfico
x = np.arange(len(meses))  # A posição de cada mês
largura = 0.10  # Ajuste na largura de cada barra para acomodar a nova barra

fig, ax = plt.subplots(figsize=(12, 6))
ax.bar(x - 2*largura, vagas_simple_query, largura, label='Simple query', color='#4184F3')
ax.bar(x - largura, vagas_complex_query, largura, label='Complex query', color='#EA4335')
ax.bar(x, vagas_comparion_query, largura, label='Comparion-query', color='#FBBC04')
ax.bar(x + 2*largura, vagas_multi_hop, largura, label='Multi-hop query', color='#34A853')
ax.bar(x + largura, vagas_open_query, largura, label='Open query', color='#6336A8')

# Adiciona os rótulos, título e define o intervalo fixo do eixo Y
ax.set_xlabel('Patterns')
ax.set_ylabel('Score')
ax.set_title('answer_relevancy')
ax.set_xticks(x)
ax.set_xticklabels(meses)
ax.set_ylim(0, 1)  # Define o intervalo do eixo Y entre 0 e 1
ax.legend()

# Salva o gráfico como PNG
output_path = "./numero_de_vagas_empresa_X.png"
plt.savefig(output_path, format="png")
plt.close(fig)

output_path
