import os

# Path for Data INGESTION
RAW_DIR = "artifacts/raw"
RAW_FILE_PATH = os.path.join(RAW_DIR, 'raw.csv')
TRAIN_FILE_PATH = os.path.join(RAW_DIR, 'train.csv')
TEST_FILE_PATH = os.path.join(RAW_DIR, 'test.csv')

# Ensure the raw directory exists
os.makedirs(RAW_DIR, exist_ok=True)

# Paths for configuration and credentials
CONFIG_PATH = "config/config.yaml"
CREDENTIALS_PATH = "config/credentials.json"


#Data Processing

PROCESSED_DIR = "artifacts/processed"
PROCESSED_TRAIN_DATA_PATH = os.path.join(PROCESSED_DIR,'processed_train.csv')
PROCESSED_TEST_DATA_PATH = os.path.join(PROCESSED_DIR,'processed_test.csv')


##Model Training

MODEL_OUTPUT_PATH = "artifacts/models/lgbm.pkl"
