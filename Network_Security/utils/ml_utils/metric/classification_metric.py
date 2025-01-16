from Network_Security.entity.artifact_entity import ClassificationMetricArtifact
from Network_Security.exception.exception import NetworkSecurityException
from sklearn.metrics import f1_score,precision_score,recall_score
import sys

# Function to calculate classification metrics
def get_classification_score(y_true,y_pred)->ClassificationMetricArtifact:
    """
    Calculates classification metrics (F1 score, Precision, Recall) based on the true and predicted labels.
    Returns ClassificationMetricArtifact: An object containing F1 score, Precision, and Recall.
    """
    try:
            
        model_f1_score = f1_score(y_true, y_pred)
        model_recall_score = recall_score(y_true, y_pred)
        model_precision_score=precision_score(y_true,y_pred)

        # Create a ClassificationMetricArtifact to store the results
        classification_metric =  ClassificationMetricArtifact(f1_score=model_f1_score,
                    precision_score=model_precision_score, 
                    recall_score=model_recall_score)
        return classification_metric
    except Exception as e:
        raise NetworkSecurityException(e,sys)