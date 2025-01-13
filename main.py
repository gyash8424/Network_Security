from Network_Security.components.data_ingestion import DataIngestion
from Network_Security.components.data_validation import DataValidation
from Network_Security.exception.exception import NetworkSecurityException
from Network_Security.logging.logger import logging
from Network_Security.entity.corfig_entity import DataIngestionConfig, DataValidationConfig
from Network_Security.entity.corfig_entity import TrainingPipelineConfig


import sys

if __name__ == '__main__':
    try:
        trainingpipelineconfig = TrainingPipelineConfig()
        dataingestionconfig = DataIngestionConfig(trainingpipelineconfig)

        data_ingestion = DataIngestion(dataingestionconfig)

        logging.info("Initiate the data ingestion")
        dataingestionartifact = data_ingestion.initiate_data_ingestion()
        #print(dataingestionartifact)
        
        data_validation_config = DataValidationConfig(trainingpipelineconfig)
        data_validation = DataValidation(dataingestionartifact, data_validation_config)
        logging.info("Data Validation initiated")

        data_validation_artifact = data_validation.initiate_data_validation()
        print(data_validation_artifact)
        
        
    except Exception as e:
        raise NetworkSecurityException(e,sys)
