import pandas as pd

df = pd.read_csv('decisoes_chunks.csv')
chunks = [row['conteudo'] for index, row in df.iterrows()]
print(len(chunks))
batch_size = 11000

total_batches = (len(chunks) + batch_size - 1) // batch_size

print(f"---->Dividindo os chunks em {total_batches} lotes.")
print(len(chunks))

for i in range(total_batches):
    start = i * batch_size
    end = start + batch_size
    batch = chunks[start:end]
    
    print(f"Inserindo lote {i + 1}/{total_batches}")
    pd.DataFrame([{'conteudo': chunk} for chunk in batch]).to_csv(f'decisoes_chunks_{i + 1}.csv', index=False, encoding='utf-8')