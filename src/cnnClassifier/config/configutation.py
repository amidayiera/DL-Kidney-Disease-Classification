# update config from data_ingestion notebook

from src.cnnClassifier.constants import *
from src.cnnClassifier.utils.common import read_yaml, create_directories

from src.cnnClassifier.entity.config_entity import DataIngestionConfig

class ConfigurationManager:
    def __init__(  
        self,
        config_filepath = CONFIG_FILE_PATH, 
        params_filepath = PARAMS_FILE_PATH):

        self.config = read_yaml(config_filepath) #return a dict (configbox)
        self.params = read_yaml(params_filepath)

        create_directories([self.config.artifacts_root])  # create artifacts directory


    # data_ingestion configuration
    def get_data_ingestion_config(self) -> DataIngestionConfig:  #custom entity is defined as function return type
        config = self.config.data_ingestion #extract from config.yaml 

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir 
        )

        return data_ingestion_config
    

