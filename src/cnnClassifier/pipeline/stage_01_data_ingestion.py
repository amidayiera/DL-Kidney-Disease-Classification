# update from data_ingestion notebook
from src.cnnClassifier.config.configuration import ConfigurationManager
from src.cnnClassifier.components.data_ingestion import DataIngestion
from src.cnnClassifier import logger


STAGE_NAME = "Data Ingestion Stage"


class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()

# call main function
if __name__ == '__main__':
    try:
        logger.info(f"\n\n>>>>>>> STARTED: {STAGE_NAME}  <<<<<<<\n\n")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f"\n\n>>>>>>> COMPLETED: {STAGE_NAME}  <<<<<<<\n\nx=======x")
    except Exception as e:
        logger.exception(e)
        raise e
