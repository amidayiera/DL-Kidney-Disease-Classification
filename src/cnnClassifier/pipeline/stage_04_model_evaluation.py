# update from data_ingestion notebook
from src.cnnClassifier.config.configuration import ConfigurationManager
from src.cnnClassifier.components.model_evaluation_mlflow import Evaluation
from src.cnnClassifier import logger


STAGE_NAME = "Model Evaluation Stage"


class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def main (self):
        config = ConfigurationManager()
        eval_config = config.get_evaluation_config()
        evaluation = Evaluation(eval_config)
        evaluation.evaluation()
        #evaluation.log_into_mlflow()

if __name__ == '__main__':
    try:
        logger.info(f"\n\n>>>>>>> STARTED: {STAGE_NAME}  <<<<<<<\n\n")
        obj = ModelEvaluationPipeline()
        obj.main()
        logger.info(f"\n\n>>>>>>> COMPLETED: {STAGE_NAME} <<<<<<<\n\nx=======x")
    except Exception as e:
        logger.exception(e)
        raise e
