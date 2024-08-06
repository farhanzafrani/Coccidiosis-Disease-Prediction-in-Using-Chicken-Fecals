from src.logger.logging import Logger
from src.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.pipeline.model_development_pipeline import PrepareBaseModelTrainingPipeline
from src.pipeline.model_training_pipeline import ModelTrainingPipeline
from src.pipeline.evaluation_pipeline import EvaluationPipeline


STAGE_NAME = "Data Ingestion stage"
try:
   Logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = DataIngestionTrainingPipeline()
   data_ingestion.main()
   Logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        Logger.exception(e)
        raise e




STAGE_NAME = "Prepare base model"
try: 
   Logger.info(f"*******************")
   Logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   prepare_base_model = PrepareBaseModelTrainingPipeline()
   prepare_base_model.main()
   Logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        Logger.exception(e)
        raise e




STAGE_NAME = "Training"
try: 
   Logger.info(f"*******************")
   Logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   model_trainer = ModelTrainingPipeline()
   model_trainer.main()
   Logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        Logger.exception(e)
        raise e






STAGE_NAME = "Evaluation stage"
try:
   Logger.info(f"*******************")
   Logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   model_evalution = EvaluationPipeline()
   model_evalution.main()
   Logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")

except Exception as e:
        Logger.exception(e)
        raise e