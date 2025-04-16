import os
import pandas
from src.logger import get_logger
from src.custom_exception import CustomException
import yaml
import json
import pandas as pd

logger =get_logger(__name__)

def read_yaml(file_path):
    try:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File is not in the given path.")
        with open(file_path,'r') as yaml_file:
            config = yaml.safe_load(yaml_file)
            logger.info("Successfully read the YAML file")
            return config
    except Exception as e:
        logger.error("Error While reading YAML file")
        raise CustomException("Failed to read YAML file",e)



def read_json_credentials(file_path):
    try:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found at {file_path}")
        with open(file_path, 'r') as file:
            credentials = json.load(file)

            # Normalize key names
            access_key = credentials.get("access_key") or credentials.get("accessKey")
            secret_key = credentials.get("secret_key") or credentials.get("secretKey")

            if not access_key or not secret_key:
                raise ValueError("Missing 'access_key' or 'secret_key' in credentials file.")

            return {
                "access_key": access_key,
                "secret_key": secret_key
            }

    except Exception as e:
        logger.error("Error while reading JSON credentials file")
        raise CustomException("Failed to read JSON credentials file", e)


def load_data(path):
    try:
        logger.info("Loading Data")
        return pd.read_csv(path)
    except Exception as e:
        logger.error(f"Error Loading the data {e}")
        raise CustomException("Failed to load data",e)
