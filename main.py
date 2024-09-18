#WF8: update main.py
from src.cnnClassifier import logger
from src.cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.cnnClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from src.cnnClassifier.pipeline.stage_03_model_training import ModelTrainingPipeline

# copy from data_ingestion pipeline file
STAGE_NAME = "Data Ingestion Stage"
if __name__ == '__main__':
    try:
        logger.info(f">>>>>>> started: {STAGE_NAME}  <<<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>> completed: {STAGE_NAME}  <<<<<<<\n\nx=======x")
    except Exception as e:
        logger.exception(e)
        raise e


# copy from prepare_base_model pipeline file
STAGE_NAME = "Prepare Base Model Stage"
if __name__ == '__main__':
    try:
        logger.info(f"\n\n>>>>>>> started: {STAGE_NAME}  <<<<<<<\n\n")
        obj = PrepareBaseModelTrainingPipeline()
        obj.main()
        logger.info(f"\n\n>>>>>>> completed: {STAGE_NAME}  <<<<<<<\n\nx=======x")
    except Exception as e:
        logger.exception(e)
        raise e


STAGE_NAME = "Model Training Stage"
if __name__ == '__main__':
    try:
        logger.info(f"\n\n>>>>>>> started: {STAGE_NAME}  <<<<<<<\n\n")
        obj = ModelTrainingPipeline()
        obj.main()
        logger.info(f"\n\n>>>>>>> completed: {STAGE_NAME} <<<<<<<\n\nx=======x")
    except Exception as e:
        logger.exception(e)
        raise e