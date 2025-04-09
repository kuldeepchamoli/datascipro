from src.datascipro.constants import  *
from src.datascipro.utils.common import read_yaml,create_directories
from pathlib import Path

from src.datascipro.entity.config_entity import (DataIngestionConfig)

class ConfigurationManager:
    def __init__(self,
                 config_filepath=CONFIG_FILE_PATH,
                 params_filepath=PARAMS_FILE_PATH,
                 schema_filepath=SCHEMA_FILE_PATH):
        """
        Loads configuration, parameters, and schema YAML files.
        Also creates the root artifacts directory.
        """
        #self.config = read_yaml(config_filepath)   # Load main config
        #self.params = read_yaml(params_filepath)   # Load model/experiment params
        #self.schema = read_yaml(schema_filepath)   # Load data schema
        from pathlib import Path

        self.config = read_yaml(Path(config_filepath))
        self.params = read_yaml(Path(params_filepath))
        self.schema = read_yaml(Path(schema_filepath))


        # Ensure the artifacts root directory exists
        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        """
        Extracts the data ingestion-related config section and returns
        a DataIngestionConfig dataclass object.
        """
        config = self.config.data_ingestion
        create_directories([config.root_dir])  # Create dir for data ingestion artifacts

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )
        return data_ingestion_config
