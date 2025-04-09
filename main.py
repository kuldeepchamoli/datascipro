from src.datascipro import logger 
from src.datascipro.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.datascipro.pipeline.data_validation_pipeline import DataValidationTrainingPipeline

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


STAGE_NAME = "Data Validation Stage"  # 
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<")  # ✅ use f-string for interpolation
    data_ingestion = DataValidationTrainingPipeline()
    data_ingestion.initiate_data_validation()
    logger.info(f">>>>> stage {STAGE_NAME} COMPLETED <<<<\n\n<<<<")
except Exception as e:
    logger.exception(e)
    raise e
