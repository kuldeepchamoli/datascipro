import os
import zipfile
from urllib import request
from src.datascipro import logger
from src.datascipro.entity.config_entity import (DataIngestionConfig)

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    # Downloading the zip file
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url=self.config.source_URL,
                filename=self.config.local_data_file
            )
            logger.info(f"{filename} downloaded with the following info: \n{headers}")
        else:
            logger.info("File already exists")

    # Extracting the downloaded zip file
    def extract_zip_file(self):
        """
        Extracts the zip file into the specified unzip directory.
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)
        logger.info(f"Extracted zip file to: {unzip_path}")
