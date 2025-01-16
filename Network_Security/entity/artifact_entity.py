# This module defines various artifacts used across the data pipeline.
# Each artifact represents the output of a specific pipeline stage.

from dataclasses import dataclass

@dataclass
class DataIngestionArtifact:
    """
    Artifact for the Data Ingestion stage.
    
    Attributes:
    - trained_file_path (str): Path to the training dataset file.
    - test_file_path (str): Path to the testing dataset file.
    """
    trained_file_path: str 
    test_file_path : str


@dataclass
class DataValidationArtifact:
    """
    Artifact for the Data Validation stage.
    
    Attributes:
    - validation_status (bool): Status indicating whether validation was successful.
    - valid_train_file_path (str): Path to the validated training dataset file.
    - valid_test_file_path (str): Path to the validated testing dataset file.
    - invalid_train_file_path (str): Path to the invalid training dataset file.
    - invalid_test_file_path (str): Path to the invalid testing dataset file.
    - drift_report_file_path (str): Path to the drift report file.
    """
    validation_status:bool
    valid_train_file_path:str
    valid_test_file_path:str
    invalid_train_file_path:str
    invalid_test_file_path:str
    drift_report_file_path:str

@dataclass
class DataTransformationArtifact:
    """
    Artifact for the Data Transformation stage.
    
    Attributes:
    - transformed_object_file_path (str): Path to the transformation object file (e.g., scaler or encoder).
    - transformed_train_file_path (str): Path to the transformed training dataset file.
    - transformed_test_file_path (str): Path to the transformed testing dataset file.
    """
    transformed_object_file_path: str
    transformed_train_file_path: str
    transformed_test_file_path: str

@dataclass
class ClassificationMetricArtifact:
    """
    Artifact for classification metrics.
    
    Attributes:
    - f1_score (float): F1 score of the classification model.
    - precision_score (float): Precision score of the classification model.
    - recall_score (float): Recall score of the classification model.
    """
    f1_score: float
    precision_score: float
    recall_score: float
    
@dataclass
class ModelTrainerArtifact:
    """
    Artifact for the Model Training stage.
    
    Attributes:
    - trained_model_file_path (str): Path to the trained model file.
    - train_metric_artifact (ClassificationMetricArtifact): Metrics for the training dataset.
    - test_metric_artifact (ClassificationMetricArtifact): Metrics for the testing dataset.
    """
    trained_model_file_path: str
    train_metric_artifact: ClassificationMetricArtifact
    test_metric_artifact: ClassificationMetricArtifact