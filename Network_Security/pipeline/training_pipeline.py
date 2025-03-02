import os
import sys

from Network_Security.exception.exception import NetworkSecurityException
from Network_Security.logging.logger import logging

from Network_Security.components.data_ingestion import DataIngestion
from Network_Security.components.data_validation import DataValidation
from Network_Security.components.data_transformation import DataTransformation
from Network_Security.components.model_trainer import ModelTrainer

from Network_Security.entity.corfig_entity import(
    TrainingPipelineConfig,
    DataIngestionConfig,
    DataValidationConfig,
    DataTransformationConfig,
    ModelTrainerConfig
)

from Network_Security.entity.artifact_entity import (
    DataIngestionArtifact,
    DataValidationArtifact,
    DataTransformationArtifact,
    ModelTrainerArtifact
)

from Network_Security.constants.training_pipeline import TRAINING_BUCKET_NAME
from Network_Security.cloud.s3_syncer import S3Sync
from Network_Security.constants.training_pipeline import SAVED_MODEL_DIR
import sys


class TrainingPipeline:
    """
    The TrainingPipeline class orchestrates the end-to-end process of training a machine learning model,
    including data ingestion, validation, transformation, model training, and syncing artifacts to S3.
    """
    def __init__(self):
        self.training_pipeline_config=TrainingPipelineConfig()
        self.s3_sync = S3Sync()
        

    def start_data_ingestion(self):
        """
        Initiates the data ingestion process, which fetches and prepares the data for further processing.
        Returns a DataIngestionArtifact containing details of the ingested data.
        """
        try:
            self.data_ingestion_config=DataIngestionConfig(
                training_pipeline_config=self.training_pipeline_config
                )
            logging.info("Starting data Ingestion")
            data_ingestion=DataIngestion(
                data_ingestion_config=self.data_ingestion_config
                )
            data_ingestion_artifact=data_ingestion.initiate_data_ingestion()
            logging.info(f"Data Ingestion completed and artifact: {data_ingestion_artifact}")
            return data_ingestion_artifact
        
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def start_data_validation(self,data_ingestion_artifact:DataIngestionArtifact):
        """
        Validates the ingested data to ensure it meets quality and format requirements.
        Returns a DataValidationArtifact containing validation results.
        """
        try:
            data_validation_config=DataValidationConfig(
                training_pipeline_config=self.training_pipeline_config
                )
            data_validation=DataValidation(
                data_ingestion_artifact=data_ingestion_artifact,
                data_validation_config=data_validation_config
                )
            logging.info("Initiating the data Validation")
            data_validation_artifact=data_validation.initiate_data_validation()
            return data_validation_artifact
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def start_data_transformation(self,data_validation_artifact:DataValidationArtifact):
        """
        Transforms the validated data into a format suitable for model training.
        Returns a DataTransformationArtifact containing transformed data details.
        """
        try:
            data_transformation_config = DataTransformationConfig(
                training_pipeline_config=self.training_pipeline_config
                )
            data_transformation = DataTransformation(
                data_validation_artifact=data_validation_artifact,
            data_transformation_config=data_transformation_config
            )
            
            data_transformation_artifact = data_transformation.initiate_data_transformation()
            return data_transformation_artifact
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def start_model_trainer(self,data_transformation_artifact:DataTransformationArtifact)->ModelTrainerArtifact:
        """
        Trains a machine learning model using the transformed data.
        Returns a ModelTrainerArtifact containing details of the trained model.
        """
        try:
            self.model_trainer_config: ModelTrainerConfig = ModelTrainerConfig(
                training_pipeline_config=self.training_pipeline_config
                )

            model_trainer = ModelTrainer(
                data_transformation_artifact=data_transformation_artifact,
                model_trainer_config=self.model_trainer_config
                )

            model_trainer_artifact = model_trainer.initiate_model_trainer()

            return model_trainer_artifact

        except Exception as e:
            raise NetworkSecurityException(e, sys)
    
    ## local artifact is going to s3 bucket    
    def sync_artifact_dir_to_s3(self):
        try:
            aws_bucket_url = f"s3://{TRAINING_BUCKET_NAME}/artifact/{self.training_pipeline_config.timestamp}"
            self.s3_sync.sync_folder_to_s3(
                folder = self.training_pipeline_config.artifact_dir,
                aws_bucket_url=aws_bucket_url
                )
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        

    ## local final model is going to s3 bucket 
    def sync_saved_model_dir_to_s3(self):
        try:
            aws_bucket_url = f"s3://{TRAINING_BUCKET_NAME}/final_model/{self.training_pipeline_config.timestamp}"
            self.s3_sync.sync_folder_to_s3(
                folder = self.training_pipeline_config.model_dir,
                aws_bucket_url=aws_bucket_url
                )
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    
    
    def run_pipeline(self):
        """
        Executes the entire training pipeline, including data ingestion, validation, transformation,
        model training, and syncing artifacts and models to S3.
        """
        try:
            # Start data ingestion
            data_ingestion_artifact=self.start_data_ingestion()
            # Perform data validation
            data_validation_artifact=self.start_data_validation(data_ingestion_artifact=data_ingestion_artifact)
            # Transform the data
            data_transformation_artifact=self.start_data_transformation(data_validation_artifact=data_validation_artifact)
            # Train the model
            model_trainer_artifact=self.start_model_trainer(data_transformation_artifact=data_transformation_artifact)
            
            # Sync local artifacts and models to S3
            self.sync_artifact_dir_to_s3()
            self.sync_saved_model_dir_to_s3()
            
            return model_trainer_artifact
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    
