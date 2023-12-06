from typing import Any
from src.textsummarizer.config.configuration import ConfigurationManager
from src.textsummarizer.components.data_ingestion import DataIngestion 
from src.textsummarizer.logging  import logger
import ssl


ssl._create_default_https_context = ssl._create_unverified_context

class DataIngestionTrainingPipeline:
    def __call__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()