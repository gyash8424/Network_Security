import os
import sys
import numpy as np
import pandas as pd

"""
defining common constant variable for training pipeline
"""
TARGET_COLUMN = "Result"    # The target variable for prediction.
PIPELINE_NAME: str = "NetworkSecurity"  # Name of the pipeline.
ARTIFACT_DIR: str = "Artifacts" # Directory to store all pipeline artifacts.
FILE_NAME: str = "phisingData.csv"  # Name of the input dataset file.

# Filenames for training and testing datasets after splitting.  
TRAIN_FILE_NAME: str = "train.csv"
TEST_FILE_NAME: str = "test.csv"

# Schema file path for data validation.
SCHEMA_FILE_PATH = os.path.join("data_schema", "schema.yaml")

# Directory for saving the trained model.
SAVED_MODEL_DIR =os.path.join("saved_models")
MODEL_FILE_NAME = "model.pkl"


"""
Data Ingestion related constant start with DATA_INGESTION VAR NAME
"""
DATA_INGESTION_COLLECTION_NAME: str = "Network_Data"    # Directory for saving the trained model.
DATA_INGESTION_DATABASE_NAME: str = "Data_Science_Project"  # MongoDB database name.
DATA_INGESTION_DIR_NAME: str = "data_ingestion" # Directory name for data ingestion artifacts.
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store" # Directory for feature store.
DATA_INGESTION_INGESTED_DIR: str = "ingested"   # Directory for ingested data.
DATA_INGESTION_TRAIN_TEST_SPLIT_RATION: float = 0.2


"""
Data Validation related constant start with DATA_VALIDATION VAR NAME
"""
DATA_VALIDATION_DIR_NAME: str = "data_validation"   # Directory for data validation artifacts.
DATA_VALIDATION_VALID_DIR: str = "validated"    # Directory for valid datasets.
DATA_VALIDATION_INVALID_DIR: str = "invalid"    # Directory for invalid datasets.
DATA_VALIDATION_DRIFT_REPORT_DIR: str = "drift_report"   # Directory for drift reports.
DATA_VALIDATION_DRIFT_REPORT_FILE_NAME: str = "report.yaml" # Filename for the data drift report.
PREPROCESSING_OBJECT_FILE_NAME: str = "preprocessing.pkl"   # Preprocessing object file name.

"""
Data Transformation related constant start with DATA_TRANSFORMATION VAR NAME
"""
DATA_TRANSFORMATION_DIR_NAME: str = "data_transformation"
DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR: str = "transformed"
DATA_TRANSFORMATION_TRANSFORMED_OBJECT_DIR: str = "transformed_object"

# Parameters for KNN imputer to handle missing values.
DATA_TRANSFORMATION_IMPUTER_PARAMS: dict = {
    "missing_values": np.nan,
    "n_neighbors": 3,
    "weights": "uniform",
}
DATA_TRANSFORMATION_TRAIN_FILE_PATH: str = "train.npy"

DATA_TRANSFORMATION_TEST_FILE_PATH: str = "test.npy"

"""
Model Trainer ralated constant start with MODE TRAINER VAR NAME
"""

MODEL_TRAINER_DIR_NAME: str = "model_trainer"
MODEL_TRAINER_TRAINED_MODEL_DIR: str = "trained_model"
MODEL_TRAINER_TRAINED_MODEL_NAME: str = "model.pkl"
MODEL_TRAINER_EXPECTED_SCORE: float = 0.6
MODEL_TRAINER_OVER_FIITING_UNDER_FITTING_THRESHOLD: float = 0.05

# Cloud storage bucket name for training artifacts.
TRAINING_BUCKET_NAME = "network123security"