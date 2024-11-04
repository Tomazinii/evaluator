import matplotlib.pyplot as plt
import numpy as np

# Dados fictícios - substitua pelos valores reais conforme necessário
meses = ["naive-rag", "naive-hyde-rag", "crag-hyde", "rag-fusion", "self-rag"]
vagas_simple_query =    [0.0, 0.0, 0.0, 0.0, 0.0]
vagas_complex_query =   [0.0, 0.0, 0.0, 0.0, 0.0]
vagas_comparion_query = [0.199999, 0.5533, 0.19999, 0.47777,0.1999]
vagas_multi_hop =       [0.8666, 1.0, 0.99999,0.9999, 0.86666]
vagas_open_query =      [0.291666, 0.5294, 0.2916, 0.199, 0.29166]

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
ax.set_title('llm_context_precision_without_reference')
ax.set_xticks(x)
ax.set_xticklabels(meses)
ax.set_ylim(0, 1)  # Define o intervalo do eixo Y entre 0 e 1
ax.legend()

# Salva o gráfico como PNG
output_path = "./llm_context_precision_without_reference_decisoes.png"
plt.savefig(output_path, format="png")
plt.close(fig)

output_path
