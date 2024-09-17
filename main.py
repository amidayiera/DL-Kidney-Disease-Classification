#WF8: update main.py
from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

# copy from data_ingestion pipeline file
STAGE_NAME = "Data Ingestion Stage"
if __name__ == '__main__':
    try:
        logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<\n\nx=======x")
    except Exception as e:
        logger.exception(e)
        raise e