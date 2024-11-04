import json

def main():
    # Inicializa a estrutura de dados principal
    main_data = {
        "case_name": "legis",
        "pattern": {}
    }

    # Lista de arquivos de entrada
    input_files = [
        'Report_repository-3aba878b-9c7a-47a2-8484-1f40d5636e92-dataset1-crag-hyde', 
        'Report_repository-3aba878b-9c7a-47a2-8484-1f40d5636e92-dataset1-naive-hyde-rag', 
        'Report_repository-3aba878b-9c7a-47a2-8484-1f40d5636e92-dataset1-naive-rag', 
        'Report_repository-3aba878b-9c7a-47a2-8484-1f40d5636e92-dataset1-self-rag', 
        'qwe', 
        'qwe', 
        'qwe', 
        'qwe', 
        'qwe', 
        'qwe', 
        'qwe', 
        'qwe', 
        'qwe', 
        'qwe', 
        'qwe', 
        'qwe', 
        'qwe', 
        'qwe', 
        'qwe', 
        'qwe', 
        'qwe', 
        'qwe', 
        'qwe', 
        'qwe', 
        'qwe', 
        'qwe', 
        'qwe', 
        'qwe', 
        'qwe', 
        'qwe', 
        'qwe', 
        'qwe', 
        'qwe', 
        'qwe', 
        'qwe', 
        'qwe', 
        'qwe', 
                   ]

    # Contador para identificar métricas
    metrics_counter = 1

    for input_file in input_files:
        with open(input_file, 'r') as f:
            data = json.load(f)

        # Obtém as categorias
        categories = data.get('categories', {})
        for category_key, category_value in categories.items():
            category_name = category_value.get('category_name', 'unknown-category')

            # Inicializa a categoria em main_data se não existir
            if category_name not in main_data['pattern']:
                main_data['pattern'][category_name] = {}

            # Itera sobre as interações
            interactions = category_value.get('interactions', {})
            for interaction_key, interaction_value in interactions.items():
                # Inicializa a interação em main_data se não existir
                if interaction_key not in main_data['pattern'][category_name]:
                    main_data['pattern'][category_name][interaction_key] = {}

                # Obtém as métricas
                metrics = interaction_value.get('metrics', {})

                # Armazena as métricas sob 'metricsX'
                metrics_key = f"metrics{metrics_counter}"
                main_data['pattern'][category_name][interaction_key][metrics_key] = metrics

            # Processa 'overall_metrics'
            overall_metrics = data.get('overall_metrics', {})

            # Inicializa 'overall' em main_data se não existir
            if 'overall' not in main_data['pattern'][category_name]:
                main_data['pattern'][category_name]['overall'] = {}

            # Armazena as métricas gerais sob 'metricsX'
            metrics_key = f"metrics{metrics_counter}"
            main_data['pattern'][category_name]['overall'][metrics_key] = overall_metrics

        metrics_counter += 1

    # Escreve o main_data em 'main.json'
    with open('mainss.json', 'w') as f:
        json.dump(main_data, f, indent=4)

print("Ok")
if __name__ == '__main__':
    main()
