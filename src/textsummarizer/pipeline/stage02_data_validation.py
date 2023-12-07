from src.textsummarizer.config.configuration import ConfigurationManager
from src.textsummarizer.components.data_validation import DataValidation
from src.textsummarizer.logging  import logger

class DataValidationTrainingPipeline:
    def __call__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_ingestion = DataValidation(config=data_validation_config)
        data_ingestion.validate_all_files_exist()
        