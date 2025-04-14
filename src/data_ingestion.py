import os
import pandas as pd
from minio import Minio
from sklearn.model_selection import train_test_split
from src.logger import get_logger
from src.custom_exception import CustomException
from config.path_config import *
from utils.common_function import read_yaml, read_json_credentials

logger = get_logger(__name__)

class DataIngestion:
    def __init__(self, config, credentials):
        self.config = config["data_ingestion"]
        self.bucket_name = self.config["bucket_name"]
        self.file_name = self.config["bucket_file_name"]
        self.train_test_ratio = self.config["train_ratio"]

        self.access_key = credentials["access_key"]
        self.secret_key = credentials["secret_key"]

        # Ensure directory exists
        os.makedirs(RAW_DIR, exist_ok=True)
        logger.info(f"Data Ingestion started with bucket: {self.bucket_name}, file: {self.file_name}")

    def download_csv_from_minio(self):
        try:
            client = Minio(
                "localhost:9000",
                access_key=self.access_key,
                secret_key=self.secret_key,
                secure=False
            )

            # Update the file path to 'raw.csv' for consistency
            object_path = os.path.join(RAW_DIR, 'raw.csv')

            client.fget_object(
                bucket_name=self.bucket_name,
                object_name=self.file_name,
                file_path=object_path
            )

            logger.info(f"File '{self.file_name}' downloaded successfully from bucket '{self.bucket_name}' to {object_path}.")

        except Exception as e:
            logger.error("Error while downloading the CSV file")
            raise CustomException("Failed to download the CSV file", e)

    def split_data(self):
        try:
            logger.info("Starting the splitting process")

            if not os.path.exists(RAW_FILE_PATH):
                logger.error(f"The raw data file does not exist at {RAW_FILE_PATH}")
                raise FileNotFoundError(f"The raw data file does not exist at {RAW_FILE_PATH}")

            logger.info(f"Attempting to read raw data from: {RAW_FILE_PATH}")

            data = pd.read_csv(RAW_FILE_PATH)

            logger.info(f"Data shape before split: {data.shape}")

            if data.isnull().sum().sum() > 0:
                logger.warning(f"Data contains {data.isnull().sum().sum()} missing values.")

            train_data, test_data = train_test_split(data, test_size=1 - self.train_test_ratio, random_state=42)

            logger.info(f"Train data shape: {train_data.shape}")
            logger.info(f"Test data shape: {test_data.shape}")

            train_data.to_csv(TRAIN_FILE_PATH, index=False)
            test_data.to_csv(TEST_FILE_PATH, index=False)

            logger.info(f"Train data saved to {TRAIN_FILE_PATH}")
            logger.info(f"Test data saved to {TEST_FILE_PATH}")

        except Exception as e:
            logger.error(f"Error while splitting the data: {str(e)}")
            raise CustomException("Failed to split the data", e)

    def run(self):
        try:
            logger.info("Starting data ingestion process")

            self.download_csv_from_minio()
            self.split_data()

            logger.info("Data ingestion completed successfully")

        except CustomException as ce:
            logger.error(str(ce))

        finally:
            logger.info("Data ingestion Completed")


if __name__ == "__main__":
    config = read_yaml(CONFIG_PATH)
    credentials = read_json_credentials(CREDENTIALS_PATH)
    data_ingestion = DataIngestion(config=config, credentials=credentials)
    data_ingestion.run()
