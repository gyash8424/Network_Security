from Network_Security.constants.training_pipeline import SAVED_MODEL_DIR,MODEL_FILE_NAME

import os
import sys

from Network_Security.exception.exception import NetworkSecurityException
from Network_Security.logging.logger import logging

class NetworkModel:
    """
    A wrapper class for combining a preprocessor and a trained machine learning model. 
    This class allows seamless integration of preprocessing and prediction steps.
    """
    def __init__(self,preprocessor,model):
        """
        - preprocessor: A preprocessing object (e.g., Scikit-learn pipeline) that transforms input data.
        - model: A trained machine learning model (e.g., RandomForestClassifier, LogisticRegression).
        """
        try:
            self.preprocessor = preprocessor
            self.model = model
        except Exception as e:
            raise NetworkSecurityException(e,sys)
    
    def predict(self,x):
        try:
            x_transform = self.preprocessor.transform(x)
            y_hat = self.model.predict(x_transform)
            return y_hat
        except Exception as e:
            raise NetworkSecurityException(e,sys)