# This module defines configuration classes used for different stages of the pipeline.
# Each class organizes paths, file names, and parameters required for its respective pipeline stage.

from datetime import datetime
import os
from Network_Security.constants import training_pipeline

#print(training_pipeline.PIPELINE_NAME)

class TrainingPipelineConfig:
    """
    Configuration class for the overall training pipeline.
    
    Attributes:
    - pipeline_name (str): Name of the pipeline.
    - artifact_name (str): Base directory for all artifacts.
    - artifact_dir (str): Path to the directory where artifacts are stored, organized by timestamp.
    - model_dir (str): Directory path for the final trained model.
    - timestamp (str): Timestamp used for organizing pipeline artifacts.
    """
    def __init__(self, timestamp=datetime.now()):
        timestamp=timestamp.strftime("%m_%d_%Y_%H_%M_%S")
        self.pipeline_name=training_pipeline.PIPELINE_NAME
        self.artifact_name=training_pipeline.ARTIFACT_DIR
        self.artifact_dir=os.path.join(self.artifact_name,timestamp)
        self.model_dir=os.path.join("final_model")
        self.timestamp: str=timestamp

class DataIngestionConfig:
    """
    Configuration class for the Data Ingestion stage.
    
    Attributes:
    - data_ingestion_dir (str): Directory for data ingestion artifacts.
    - feature_store_file_path (str): Path to the feature store file.
    - training_file_path (str): Path to the training dataset file.
    - testing_file_path (str): Path to the testing dataset file.
    - train_test_split_ratio (float): Ratio for splitting data into training and testing sets.
    - collection_name (str): Name of the collection in MongoDB.
    - database_name (str): Name of the database in MongoDB.
    """
    def __init__(self, training_pipeline_config:TrainingPipelineConfig):
        self.data_ingestion_dir:str = os.path.join(
            training_pipeline_config.artifact_dir,
            training_pipeline.DATA_INGESTION_DIR_NAME
        )
        self.feature_store_file_path: str = os.path.join(
                self.data_ingestion_dir,
                training_pipeline.DATA_INGESTION_FEATURE_STORE_DIR,
                training_pipeline.FILE_NAME
            )
        self.training_file_path: str = os.path.join(
                self.data_ingestion_dir,
                training_pipeline.DATA_INGESTION_INGESTED_DIR,
                training_pipeline.TRAIN_FILE_NAME
            )
        self.testing_file_path: str = os.path.join(
                self.data_ingestion_dir,
                training_pipeline.DATA_INGESTION_INGESTED_DIR,
                training_pipeline.TEST_FILE_NAME
            )
        self.train_test_split_ratio: float = training_pipeline.DATA_INGESTION_TRAIN_TEST_SPLIT_RATION
        self.collection_name: str = training_pipeline.DATA_INGESTION_COLLECTION_NAME
        self.database_name: str = training_pipeline.DATA_INGESTION_DATABASE_NAME

class DataValidationConfig:
    """
    Configuration class for the Data Validation stage.
    
    Attributes:
    - data_validation_dir (str): Directory for data validation artifacts.
    - valid_data_dir (str): Directory for valid data.
    - invalid_data_dir (str): Directory for invalid data.
    - valid_train_file_path (str): Path to the validated training dataset file.
    - valid_test_file_path (str): Path to the validated testing dataset file.
    - invalid_train_file_path (str): Path to the invalid training dataset file.
    - invalid_test_file_path (str): Path to the invalid testing dataset file.
    - drift_report_file_path (str): Path to the data drift report.
    """
    def __init__(self,training_pipeline_config:TrainingPipelineConfig):
        self.data_validation_dir: str = os.path.join( 
            training_pipeline_config.artifact_dir, 
            training_pipeline.DATA_VALIDATION_DIR_NAME
            )
        self.valid_data_dir: str = os.path.join(
            self.data_validation_dir, 
            training_pipeline.DATA_VALIDATION_VALID_DIR
            )
        self.invalid_data_dir: str = os.path.join(
            self.data_validation_dir, 
            training_pipeline.DATA_VALIDATION_INVALID_DIR
            )
        self.valid_train_file_path: str = os.path.join(
            self.valid_data_dir, 
            training_pipeline.TRAIN_FILE_NAME
            )
        self.valid_test_file_path: str = os.path.join(
            self.valid_data_dir, 
            training_pipeline.TEST_FILE_NAME
            )
        self.invalid_train_file_path: str = os.path.join(
            self.invalid_data_dir, 
            training_pipeline.TRAIN_FILE_NAME
            )
        self.invalid_test_file_path: str = os.path.join(
            self.invalid_data_dir, 
            training_pipeline.TEST_FILE_NAME
            )
        self.drift_report_file_path: str = os.path.join(
            self.data_validation_dir,
            training_pipeline.DATA_VALIDATION_DRIFT_REPORT_DIR,
            training_pipeline.DATA_VALIDATION_DRIFT_REPORT_FILE_NAME,
            )
        
class DataTransformationConfig:
     """
    Configuration class for the Data Transformation stage.
    
    Attributes:
    - data_transformation_dir (str): Directory for data transformation artifacts.
    - transformed_train_file_path (str): Path to the transformed training dataset file.
    - transformed_test_file_path (str): Path to the transformed testing dataset file.
    - transformed_object_file_path (str): Path to the file containing the transformation object.
    """
     def __init__(self,training_pipeline_config:TrainingPipelineConfig):
        self.data_transformation_dir: str = os.path.join( 
            training_pipeline_config.artifact_dir,
            training_pipeline.DATA_TRANSFORMATION_DIR_NAME 
            )
        self.transformed_train_file_path: str = os.path.join( 
            self.data_transformation_dir,
            training_pipeline.DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR,
            training_pipeline.TRAIN_FILE_NAME.replace("csv", "npy")
            )
        self.transformed_test_file_path: str = os.path.join(
            self.data_transformation_dir,  
            training_pipeline.DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR,
            training_pipeline.TEST_FILE_NAME.replace("csv", "npy")
            )
        self.transformed_object_file_path: str = os.path.join( 
            self.data_transformation_dir, 
            training_pipeline.DATA_TRANSFORMATION_TRANSFORMED_OBJECT_DIR,
            training_pipeline.PREPROCESSING_OBJECT_FILE_NAME)

class ModelTrainerConfig:
    """
    Configuration class for the Model Trainer stage.
    
    Attributes:
    - model_trainer_dir (str): Directory for model trainer artifacts.
    - trained_model_file_path (str): Path to the trained model file.
    - expected_accuracy (float): Minimum acceptable accuracy for the model.
    - overfitting_underfitting_threshold (float): Threshold for identifying overfitting or underfitting.
    """
    def __init__(self,training_pipeline_config:TrainingPipelineConfig):
        self.model_trainer_dir: str = os.path.join(
            training_pipeline_config.artifact_dir, training_pipeline.MODEL_TRAINER_DIR_NAME
        )
        self.trained_model_file_path: str = os.path.join(
            self.model_trainer_dir, training_pipeline.MODEL_TRAINER_TRAINED_MODEL_DIR, 
            training_pipeline.MODEL_FILE_NAME
        )
        self.expected_accuracy: float = training_pipeline.MODEL_TRAINER_EXPECTED_SCORE
        self.overfitting_underfitting_threshold = training_pipeline.MODEL_TRAINER_OVER_FIITING_UNDER_FITTING_THRESHOLD