from src.data_ingestion import DataIngestion
from utils.common_function import read_json_credentials,read_yaml
from config.path_config import CONFIG_PATH,CREDENTIALS_PATH
from src.data_preprocessing import DataProcessor
from config.path_config import *
from src.model_training import ModelTraining


if __name__ == '__main__':

    ## Data Ingestion
    config = read_yaml(CONFIG_PATH)
    credentials = read_json_credentials(CREDENTIALS_PATH)
    data_ingestion = DataIngestion(config=config, credentials=credentials)
    data_ingestion.run()

    ## Data Processing
    processor = DataProcessor(TRAIN_FILE_PATH,TEST_FILE_PATH,PROCESSED_DIR,CONFIG_PATH)
    processor.process()


    ## Model Training
    trainer = ModelTraining(
        train_path =PROCESSED_TRAIN_DATA_PATH,
        test_path = PROCESSED_TEST_DATA_PATH,
        model_output_path = MODEL_OUTPUT_PATH)
    trainer.run()
