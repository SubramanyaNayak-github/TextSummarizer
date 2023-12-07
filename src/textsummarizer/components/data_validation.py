import urllib.request as request
from urllib.request import urlretrieve
import os
import zipfile
from src.textsummarizer.logging import logger 
from src.textsummarizer.utils.common import get_size 
from pathlib import Path
from src.textsummarizer.entity import DataValidationConfig
import ssl



class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config


    def validate_all_files_exist(self) -> str:
        try:
            validation_status = None

            all_files = os.listdir(os.path.join('artifacts','data_ingestion','samsum_dataset'))

            for files in all_files:

                if files not in self.config.ALL_REQUIRED_FILES:
                    validation_status = 'All required data files are not present'
                    with open (self.config.STATUS_FILE,'w') as f:
                        f.write(f'Validation Status : {validation_status}')

                else:
                    validation_status = 'All required data files are present'
                    with open (self.config.STATUS_FILE,'w') as f:
                        f.write(f'Validation Status : {validation_status}')

            return validation_status
        
        except Exception as e:
            raise e