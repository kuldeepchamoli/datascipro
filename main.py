from src.datascipro import logger 
from src.datascipro.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.datascipro.pipeline.data_validation_pipeline import DataValidationTrainingPipeline
from src.datascipro.pipeline.data_transformation_pipeline import DataTransformationTrainingPipeline
from src.datascipro.pipeline.model_trainer_pipeline import ModelTrainerTrainingPipeline 
from src.datascipro.pipeline.model_evaluation_pipeline import ModelEvaluationTrainingPipeline


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
    data_validation = DataValidationTrainingPipeline()
    data_validation.initiate_data_validation()
    logger.info(f">>>>> stage {STAGE_NAME} COMPLETED <<<<\n\n<<<<")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data Transformation Stage"  # 
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<")  # ✅ use f-string for interpolation
    data_transformation = DataTransformationTrainingPipeline()
    data_transformation.initiate_data_transformation()
    logger.info(f">>>>> stage {STAGE_NAME} COMPLETED <<<<\n\n<<<<")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Model Trainer Stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<")  # ✅ use f-string for interpolation
    model_train = ModelTrainerTrainingPipeline()
    model_train.initiate_model_training()
    logger.info(f">>>>> stage {STAGE_NAME} COMPLETED <<<<\n\n<<<<")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Model Evaluation Stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<")  # ✅ use f-string for interpolation
    model_train = ModelEvaluationTrainingPipeline()
    model_train.initiate_model_evaluation()
    logger.info(f">>>>> stage {STAGE_NAME} COMPLETED <<<<\n\n<<<<")
except Exception as e:
    logger.exception(e)
    raise e