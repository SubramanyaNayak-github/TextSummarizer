import os
from box.exceptions import BoxValueError
import yaml
from src.textsummarizer.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any




@ensure_annotations
def read_yaml(path_to_yaml:Path)  -> ConfigBox:

    """
    It Reads YAML Files and returns 
    
    
    Args:
        path_to_yaml (str): Path to YAML file

    Raises:
        ValueError: IF YAML file is not found/ empty
        e : empty file

    Returns:
        ConfigBox : ConfigBox Type
    """

    try:
        with open (path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f'Yaml File : {path_to_yaml} loaded successfully')
            return ConfigBox(content)

    except BoxValueError:
        raise ValueError ('Yaml file is empty') 

    except Exception as e:
        raise e
    

@ensure_annotations
def create_directories(path_to_directories: list,verbose=True):

    """
    It Creates List of Directories
    
    Args:
        path_to_directories(list): list of path of directories
        ignore_log(bool,optional): ignore if multiple directories is created. Default is False
    """

    for path in path_to_directories:
        os.makedirs(path,exist_ok=True)
        if verbose:
            logger.info(f'created directory at path: {path}')


@ensure_annotations
def get_size(path:Path) -> str:

    """
    To Get size in KB

    Args:
        path(Path): path of the file

    Returns:
        str: size in kb
    
    """

    size_in_kb = round(os.path.getsize(path)/1024)

    return f"~ {size_in_kb} KB"




    