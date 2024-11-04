

from typing import Any, Dict, List

from langchain_google_vertexai import ChatVertexAI
from src.evaluator.service.EvaluateService import IEvaluateService
from ragas import EvaluationDataset, RunConfig, SingleTurnSample, evaluate
from src.orchestrator.run_evaluator.entity.RunEvaluatorBase import RunEvaluatorBase
from ragas.metrics import LLMContextRecall, Faithfulness, ContextEntityRecall, LLMContextPrecisionWithoutReference, ResponseRelevancy
from ragas.llms import LangchainLLMWrapper
import os

from langchain_openai import ChatOpenAI
from langchain_openai import OpenAIEmbeddings



class RagasEvaluateService(IEvaluateService):
        
    def __init__(self, llm_model_name: str = 'gpt-4', metrics: List[Any] = None):
        """
        Initialize the RagasEvaluateService with the desired LLM and metrics.

        Args:
            llm_model_name (str): The name of the OpenAI model to use.
            metrics (List[Any]): List of Ragas metric instances to use for evaluation.
        """

        self.llm_model_name = llm_model_name
        self.evaluator_llm = LangchainLLMWrapper(ChatVertexAI(model_name="gemini-1.5-pro", project="energygpt-421317", temperature=0.3))
        # self.evaluator_llm = LangchainLLMWrapper(ChatOpenAI(model="gpt-4o"))
        self.metrics = metrics or [LLMContextRecall(llm=self.evaluator_llm), Faithfulness(llm=self.evaluator_llm),LLMContextPrecisionWithoutReference(llm=self.evaluator_llm), ContextEntityRecall(llm=self.evaluator_llm), ResponseRelevancy(llm=self.evaluator_llm)]

        

        self.my_run_config = RunConfig(max_workers=4)

    
    async def evaluate(self, run_evaluator_bases: List[RunEvaluatorBase]) -> Dict[str, Any]:
        """
        Evaluates a list of RunEvaluatorBase instances using Ragas.

        Args:
            run_evaluator_bases (List[RunEvaluatorBase]): List of interactions to be evaluated.

        Returns:
            Dict[str, Any]: Aggregated metrics for the dataset.
        """
        # Create SingleTurnSample instances from RunEvaluatorBase


        samples = []
        for run_eval_base in run_evaluator_bases:
            sample = SingleTurnSample(
                user_input=run_eval_base.query,
                retrieved_contexts=run_eval_base.retrieved_context,
                response=run_eval_base.response,
                reference=run_eval_base.reference
            )
            samples.append(sample)
        
        # Create EvaluationDataset
        dataset = EvaluationDataset(samples=samples)
        
        # Evaluate using Ragas
        results = evaluate(run_config=self.my_run_config, dataset=dataset, metrics=self.metrics, llm=self.evaluator_llm)

        
        df_resultados = results.to_pandas().to_dict(orient='list')

        data = {
                'faithfulness': float(df_resultados['faithfulness'][0]),
                'context_recall': float(df_resultados['context_recall'][0]),
                'llm_context_precision_without_reference': float(df_resultados['llm_context_precision_without_reference'][0]),
                'context_entity_recall': float(df_resultados['context_entity_recall'][0]),  
                'answer_relevancy': float(df_resultados['answer_relevancy'][0])  
        }
        print()
        
        return data
        