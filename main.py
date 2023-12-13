from src.textsummarizer.pipeline.stage01_data_ingestion import DataIngestionTrainingPipeline
from src.textsummarizer.pipeline.stage02_data_validation import DataValidationTrainingPipeline
from src.textsummarizer.pipeline.stage03_data_transformation import DataTransformationTrainingPipeline
from src.textsummarizer.pipeline.stage04_model_trainer import ModelTrainerTrainingPipeline
from src.textsummarizer.pipeline.stage05_model_evaluation import ModelEvaluationTrainingPipeline
from src.textsummarizer.logging import logger
import ssl





#------------------------------------------------ Data Ingestion ----------------------------------------------------------------



ssl._create_default_https_context = ssl._create_unverified_context

STAGE_NAME = 'Data Ingestion Stage'

try:
    logger.info('>>>>>>> {} is started <<<<<<<'.format(STAGE_NAME))
    data_ingestion  = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info('>>>>>>> {} is completed <<<<<<<'.format(STAGE_NAME))

except Exception as e:
    logger.exception(e)
    raise e 


#------------------------------------------------ Data Validation ----------------------------------------------------------------



STAGE_NAME = 'Data VAlidation Stage'


try:
    logger.info('>>>>>>> {} is started <<<<<<<'.format(STAGE_NAME))
    data_validation  = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info('>>>>>>> {} is completed <<<<<<<'.format(STAGE_NAME))


except Exception as e:
    logger.exception(e)
    raise e



#------------------------------------------------ Data Transformation ----------------------------------------------------------------



STAGE_NAME = 'Data Transformation Stage'


try:
    logger.info('>>>>>>> {} is started <<<<<<<'.format(STAGE_NAME))
    data_transformation  = DataTransformationTrainingPipeline()
    data_transformation.main()
    logger.info('>>>>>>> {} is completed <<<<<<<'.format(STAGE_NAME))


except Exception as e:
    logger.exception(e)
    raise e





#------------------------------------------------ Model Trainer ----------------------------------------------------------------


STAGE_NAME = 'Model Training Stage'


try:
    logger.info('>>>>>>> {} is started <<<<<<<'.format(STAGE_NAME))
    model_trainer  = ModelTrainerTrainingPipeline()
    model_trainer.main()
    logger.info('>>>>>>> {} is completed <<<<<<<'.format(STAGE_NAME))

except Exception as e:
    logger.exception(e)
    raise e



#------------------------------------------------ Model Evaluation ----------------------------------------------------------------


STAGE_NAME = 'Model Evaluation Stage'


try:
    logger.info('>>>>>>> {} is started <<<<<<<'.format(STAGE_NAME))
    model_evaluation = ModelEvaluationTrainingPipeline()
    model_evaluation.main()
    logger.info('>>>>>>> {} is completed <<<<<<<'.format(STAGE_NAME))

except Exception as e:
    logger.exception(e)
    raise e