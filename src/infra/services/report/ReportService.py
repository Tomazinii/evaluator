import os
import matplotlib.pyplot as plt

from src.evaluator.entity.EvaluatorSet import EvaluatorSet
from src.report.report.services.ReportService import ReportService

class MatplotlibReportService(ReportService):
    def __init__(self, output_dir: str = ""):
        """
        Args:
            output_dir (str): O diretório onde os gráficos serão salvos.
        """
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)

    def generate_interaction_graphs(self, evaluator_set: EvaluatorSet) -> None:

        base_dir = os.path.join(os.getcwd(), 'src', 'graphs')
        
        if not os.path.exists(base_dir):
            os.makedirs(base_dir)
        


        for category_name, evaluator_category in evaluator_set.categories.items():
            for interaction_type, data in evaluator_category.interactions.items():
                metrics = data['metrics']
                if not metrics:
                    continue  # Pula se não houver métricas

                # Extrai os nomes e valores das métricas
                metric_names = list(metrics.keys())
                metric_values = [metrics[name] for name in metric_names]

                # Cria o gráfico de barras
                plt.figure(figsize=(10, 6))
                plt.bar(metric_names, metric_values, color='skyblue')
                plt.xlabel('Métricas')
                plt.ylabel('Valores')
                plt.title(f'Métricas para {interaction_type} em {category_name}')
                plt.xticks(rotation=45)
                plt.tight_layout()
  
                # Salva o gráfico como PNG
                filename = f"{category_name}_{interaction_type}_{evaluator_category.id}_metrics.png"
                filepath = os.path.join(base_dir, filename)
    
                plt.savefig(filepath)
                plt.close()

    def generate_global_metrics_graph(self, evaluator_set: 'EvaluatorSet') -> None:
        metrics = evaluator_set.overall_metrics

        
        base_dir = os.path.join(os.getcwd(), 'src', 'graphs')
        
        if not os.path.exists(base_dir):
            os.makedirs(base_dir)
        
        if not metrics:
            return  # Pula se não houver métricas globais

        # Extrai os nomes e valores das métricas
        metric_names = list(metrics.keys())
        metric_values = [metrics[name] for name in metric_names]

        # Cria o gráfico de barras
        plt.figure(figsize=(10, 6))
        plt.bar(metric_names, metric_values, color='coral')
        plt.xlabel('Métricas Globais')
        plt.ylabel('Valores')
        plt.title('Métricas Globais do Sistema')
        plt.xticks(rotation=45)
        plt.tight_layout()

        # Salva o gráfico como PNG
        filename = "global_metrics.png"
        filepath = os.path.join(base_dir, filename)
        plt.savefig(filepath)
        plt.close()