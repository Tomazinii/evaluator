import pandas as pd
from transformers import GPT2Tokenizer

# Carregar o arquivo CSV
df = pd.read_csv("src/data_source/pdi_chunks.csv")

# Concatenar todas as células do CSV em uma única string
conteudo = " ".join(df.astype(str).values.flatten())

# Carregar o tokenizer (aqui, o GPT-2)
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")

# Tokenizar o conteúdo e contar tokens
tokens = tokenizer(conteudo)["input_ids"]
quantidade_de_tokens = len(tokens)

print(f"Quantidade de tokens: {quantidade_de_tokens}")