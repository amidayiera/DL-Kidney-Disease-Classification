# update from data_ingestion notebook
from src.cnnClassifier.config.configuration import ConfigurationManager
from src.cnnClassifier.components.model_training import Training
from src.cnnClassifier import logger


STAGE_NAME = "Model Training Stage"


class ModelTrainingPipeline:
    def __init__(self):
        pass

    def main (self):
        config = ConfigurationManager()
        training_config = config.get_training_config()
        training = Training(config=training_config)
        training.get_base_model()
        training.train_valid_generator()
        training.train()

if __name__ == '__main__':
    try:
        logger.info(f"\n\n>>>>>>> STARTED: {STAGE_NAME}  <<<<<<<\n\n")
        obj = ModelTrainingPipeline()
        obj.main()
        logger.info(f"\n\n>>>>>>> COMPLETED: {STAGE_NAME} <<<<<<<\n\nx=======x")
    except Exception as e:
        logger.exception(e)
        raise e
