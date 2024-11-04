import matplotlib.pyplot as plt
import numpy as np

# Dados fictícios - substitua pelos valores reais conforme necessário
meses = ["naive-rag", "naive-hyde-rag", "crag-hyde", "rag-fusion", "self-rag"]
vagas_simple_query = [0.96803, 0.9730, 0.92906, 0.9630, 0.0]
vagas_complex_query = [0.886, 0.8757, 0.87711, 0.8960, 0.0769230]
vagas_comparion_query = [0.938,  0.87670446, 0.8788, 0.8767, 0.0]
vagas_multi_hop = [0.9237, 0.9362, 0.93872, 0.94219, 0.22222222]
vagas_open_query = [0.85492,0.84832, 0.859199, 0.92240, 0.8586]

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
output_path = "./answer_relevancy_legis.png"
plt.savefig(output_path, format="png")
plt.close(fig)

output_path
