# update from base_model notebook
from src.cnnClassifier.config.configutation import ConfigurationManager
from src.cnnClassifier.components.prepare_base_model import PrepareBaseModel
from src.cnnClassifier import logger

STAGE_NAME = "Prepare Base Model Stage"

class PrepareBaseModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        prepare_base_model_config = config.get_prepare_base_model_config()
        prepare_base_model = PrepareBaseModel(config=prepare_base_model_config)
        prepare_base_model.get_base_model()
        prepare_base_model.update_base_model()

# call main function
if __name__ == '__main__':
    try:
        logger.info(f"\n\n>>>>>>> STARTED: {STAGE_NAME}  <<<<<<<\n\n")
        obj = PrepareBaseModelTrainingPipeline()
        obj.main()
        logger.info(f"\n\n>>>>>>> COMPLETED: {STAGE_NAME} <<<<<<<\n\nx=======x")
    except Exception as e:
        logger.exception(e)
        raise e

