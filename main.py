from src.textsummarizer.pipeline.stage01_data_ingestion import DataIngestionTrainingPipeline
from src.textsummarizer.logging import logger
import ssl


ssl._create_default_https_context = ssl._create_unverified_context

STAGE_NAME = 'Data Ingestion Stage'

try:
    logger.info(f'>>>>>>> {STAGE_NAME} is started <<<<<<<')
    data_ingestion  = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f'>>>>>>> {STAGE_NAME} is completed <<<<<<<\n\n================================')

except Exception as e:
    logger.exception(e)
    raise e 