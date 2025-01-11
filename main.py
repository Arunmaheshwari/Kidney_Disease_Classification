from src.Kidney_Disease_Classifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from src.Kidney_Disease_Classifier import logger
from src.Kidney_Disease_Classifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline



STAGE_NAME = "Data Ingestion stage"


try:
    logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<\n\nx=============x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Prepare base model"

if __name__ == "__main__":
    try:
        logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<<<<")
        obj = PrepareBaseModelTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<\n\nx=============x")
    except Exception as e:
        logger.exception(e)
        raise e