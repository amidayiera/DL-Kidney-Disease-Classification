#WF8: update main.py
from src.cnnClassifier import logger
from src.cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.cnnClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from src.cnnClassifier.pipeline.stage_03_model_training import ModelTrainingPipeline
from src.cnnClassifier.pipeline.stage_04_model_evaluation import ModelEvaluationPipeline

# copy from data_ingestion pipeline file
STAGE_NAME = "Data Ingestion Stage"
if __name__ == '__main__':
    try:
        logger.info(f"\n\n>>>>>>> STARTED: {STAGE_NAME}  <<<<<<<\n\n")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f"\n\n>>>>>>> COMPLETED: {STAGE_NAME} <<<<<<<\n\nx=======x")
    except Exception as e:
        logger.exception(e)
        raise e


# copy from prepare_base_model pipeline file
STAGE_NAME = "Prepare Base Model Stage"
if __name__ == '__main__':
    try:
        logger.info(f"\n\n>>>>>>> STARTED: {STAGE_NAME}  <<<<<<<\n\n")
        obj = PrepareBaseModelTrainingPipeline()
        obj.main()
        logger.info(f"\n\n>>>>>>> COMPLETED: {STAGE_NAME} <<<<<<<\n\nx=======x")
    except Exception as e:
        logger.exception(e)
        raise e



STAGE_NAME = "Model Training Stage"
if __name__ == '__main__':
    try:
        logger.info(f"\n\n>>>>>>> STARTED: {STAGE_NAME}  <<<<<<<\n\n")
        obj = ModelTrainingPipeline()
        obj.main()
        logger.info(f"\n\n>>>>>>> COMPLETED: {STAGE_NAME} <<<<<<<\n\nx=======x")
    except Exception as e:
        logger.exception(e)
        raise e



STAGE_NAME = "Model Evaluation Stage"
if __name__ == '__main__':
    try:
        logger.info(f"\n\n>>>>>>> STARTED: {STAGE_NAME}  <<<<<<<\n\n")
        obj = ModelEvaluationPipeline()
        obj.main()
        logger.info(f"\n\n>>>>>>> COMPLETED: {STAGE_NAME} <<<<<<<\n\nx=======x")
    except Exception as e:
        logger.exception(e)
        raise e
