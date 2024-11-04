import json
import tiktoken

import os

base_dir = os.path.join(os.getcwd(), 'src', 'data')

if not os.path.exists(base_dir):
    os.makedirs(base_dir)



file_path = os.path.join(base_dir, "RunEvaluatorSet-3aba878b-9c7a-47a2-8484-1f40d5636e92-crag-hyde-dataset1")

with open(file_path, 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)
# Função para extrair todo o texto do JSON
def extract_text(data):
    texts = []
    if isinstance(data, dict):
        for key, value in data.items():
            texts.extend(extract_text(value))
    elif isinstance(data, list):
        for item in data:
            texts.extend(extract_text(item))
    elif isinstance(data, str):
        texts.append(data)
    return texts

# Extrair todo o texto do JSON
all_texts = extract_text(data)

# Concatenar todos os textos
full_text = ' '.join(all_texts)

# Inicializar o tokenizador
enc = tiktoken.get_encoding("cl100k_base")  # Use o modelo apropriado

# Tokenizar o texto
tokens = enc.encode(full_text)

# Imprimir a quantidade total de tokens
print(f"Quantidade total de tokens: {len(tokens)}")
