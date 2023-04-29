import os

from sensor.constant.training_pipeline import TRAINING_BUCKET_NAME

#defined common variables for training pipeline.
TARGET_COLUMN = "class"
PIPELINE_NAME = "sensor"
ARTIFACT_DIR:str = "artifact"
FILE_NAME:str = "sensor.csv"

TRAINING_FILE_NAME: str = "train.csv"
TEST_FILE_NAME:str = "test.csv"

PREPROCESSING_OBJECT_FILE_NAME: str = "preprocessing.pkl"
MODEL_FILE_NAME: str = "model.pkl"
SCHEMA_FILE_PATH: str = os.path.join('config', 'schema.yaml')
SCHEMA_DROP_COLS = "drop_columns"

#data ingestion related constants with DATA_INGESTION_VAR_NAME
DATA_INGESTION_COLLECTION_NAME: str = "car"
DATA_INGESTION_DIR_NAME: str = "data_ingestion"
DATA_INGESTIN_FEATURE_STORE_DIR: str = "feature_store"
DATA_INGESTION_INGESTED_DIR: str = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATION: float = 0.2




