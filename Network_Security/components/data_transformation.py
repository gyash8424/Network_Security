# This module handles data transformation, including missing value imputation and feature preprocessing.

import sys
import os
import numpy as np
import pandas as pd
from sklearn.impute import KNNImputer
from sklearn.pipeline import Pipeline

from Network_Security.constants.training_pipeline import TARGET_COLUMN
from Network_Security.constants.training_pipeline import DATA_TRANSFORMATION_IMPUTER_PARAMS

from Network_Security.entity.artifact_entity import (
    DataTransformationArtifact,
    DataValidationArtifact
)

from Network_Security.entity.corfig_entity import DataTransformationConfig
from Network_Security.exception.exception import NetworkSecurityException 
from Network_Security.logging.logger import logging
from Network_Security.utils.main_utils.utils import save_numpy_array_data,save_object

class DataTransformation:
    """
    Handles the data transformation process, including missing value imputation,
    feature transformation, and saving processed data for model training and testing.
    """
    def __init__(self,data_validation_artifact:DataValidationArtifact,
                 data_transformation_config:DataTransformationConfig):
        try:
            self.data_validation_artifact:DataValidationArtifact=data_validation_artifact
            self.data_transformation_config:DataTransformationConfig=data_transformation_config
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    @staticmethod
    def read_data(file_path) -> pd.DataFrame:
        
        try:
            return pd.read_csv(file_path)
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
    def get_data_transformer_object(cls)->Pipeline:
        """
        It initialises a KNNImputer object with the parameters specified in the training_pipeline.py file
        and returns a Pipeline object with the KNNImputer object as the first step.

        Args:
          cls: DataTransformation

        Returns:
          A Pipeline object
        """
        logging.info(
            "Entered get_data_trnasformer_object method of Trnasformation class"
        )
        try:
           imputer:KNNImputer=KNNImputer(**DATA_TRANSFORMATION_IMPUTER_PARAMS)
           logging.info(
                f"Initialise KNNImputer with {DATA_TRANSFORMATION_IMPUTER_PARAMS}"
            )
           processor:Pipeline=Pipeline([("imputer",imputer)])
           return processor
        except Exception as e:
            raise NetworkSecurityException(e,sys)

        
    def initiate_data_transformation(self)->DataTransformationArtifact:
        """
        Executes the data transformation process, including:
        - Reading data
        - Imputing missing values
        - Preparing train and test arrays
        - Saving transformed data and the preprocessor object
        Returns:
            DataTransformationArtifact: Artifact containing paths to transformed data and preprocessor object.
        """

        logging.info("Entered initiate_data_transformation method of DataTransformation class")
        try:
            # Load training and testing datasets
            logging.info("Starting data transformation")
            train_df=DataTransformation.read_data(self.data_validation_artifact.valid_train_file_path)
            test_df=DataTransformation.read_data(self.data_validation_artifact.valid_test_file_path)

            # Separate features and target for training data
            input_feature_train_df=train_df.drop(columns=[TARGET_COLUMN],axis=1)
            target_feature_train_df = train_df[TARGET_COLUMN]
            target_feature_train_df = target_feature_train_df.replace(-1, 0)

            # Separate features and target for testing data
            input_feature_test_df = test_df.drop(columns=[TARGET_COLUMN], axis=1)
            target_feature_test_df = test_df[TARGET_COLUMN]
            target_feature_test_df = target_feature_test_df.replace(-1, 0)

            preprocessor=self.get_data_transformer_object()

            preprocessor_object=preprocessor.fit(input_feature_train_df)
            # Transform features
            transformed_input_train_feature=preprocessor_object.transform(input_feature_train_df)
            transformed_input_test_feature =preprocessor_object.transform(input_feature_test_df)
             
            # Combine features and target into numpy arrays
            train_arr = np.c_[transformed_input_train_feature, np.array(target_feature_train_df) ]
            test_arr = np.c_[ transformed_input_test_feature, np.array(target_feature_test_df) ]

            # Save transformed data and preprocessor object
            save_numpy_array_data( self.data_transformation_config.transformed_train_file_path, array=train_arr )
            save_numpy_array_data( self.data_transformation_config.transformed_test_file_path,array=test_arr)
            save_object( self.data_transformation_config.transformed_object_file_path, preprocessor_object)

            save_object( "final_model/preprocessor.pkl", preprocessor_object)


            # Prepare artifact
            data_transformation_artifact=DataTransformationArtifact(
                transformed_object_file_path=self.data_transformation_config.transformed_object_file_path,
                transformed_train_file_path=self.data_transformation_config.transformed_train_file_path,
                transformed_test_file_path=self.data_transformation_config.transformed_test_file_path
            )
            return data_transformation_artifact


            
        except Exception as e:
            raise NetworkSecurityException(e,sys)
