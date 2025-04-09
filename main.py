from src.datascipro import logger 
from src.datascipro.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline

STAGE_NAME = "Data Ingestion Stage"  # ✅ define the stage name

logger.info("Welcome to our custom logging datascience project")

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<")  # ✅ use f-string for interpolation
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.initiate_data_ingestion()
    logger.info(f">>>>> stage {STAGE_NAME} COMPLETED <<<<\n\n<<<<")
except Exception as e:
    logger.exception(e)
    raise e
