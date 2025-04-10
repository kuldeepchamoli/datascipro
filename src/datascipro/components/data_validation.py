import os
from src.datascipro import logger
import pandas as pd

from src.datascipro.entity.config_entity import DataValidationConfig

class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    def validate_all_columns(self) -> bool:
        try:
            validation_status = True

            data = pd.read_csv(self.config.unzip_data_dir)
            schema_columns = self.config.all_schema.keys()

            for col in schema_columns:
                if col not in data.columns:
                    validation_status = False
                    logger.warning(f"Missing column in dataset: {col}")

            with open(self.config.STATUS_FILE, 'w') as f:
                f.write(f"Validation status: {validation_status}")

            return validation_status

        except Exception as e:
            logger.exception("Error during column presence validation")
            raise e

