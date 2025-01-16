# Network Security - ML Model Pipeline

## Table of Contents
1. [Motivation](#motivation)
2. [Project Description](#project-description)
3. [Pipeline Stages](#pipeline-stages)
4. [Tech Stack](#tech-stack)
5. [Screenshots](#screenshots)
---
## Motivation
With the increasing prevalence of cyber frauds and threats, user privacy has become more essential than ever. Hackers often attempt to gain sensitive information through phishing attacks. This project aims to protect users from such threats by identifying phishing websites. It can easily be integrated as a tool in larger applications or used for surveillance purposes by enterprises or individual users.

## Project Description
This repository contains a machine learning pipeline for classifying network data as phishing or legitimate. The pipeline involves multiple stages, including data ingestion, data validation, data transformation, model training, and prediction. The project is built to handle large-scale network data and make real-time predictions.

The project involves building and deploying a machine learning model to classify network data. The pipeline ensures automated data handling, model training, and prediction, all while maintaining version control and model management.

## Pipeline Stages
1. **Data Ingestion**: Extracts data MongoDB and loads it as pandas dataframe.
2. **Data Validation**: Validates the data for any inconsistencies, missing values, or anomalies.
3. **Data Transformation**: Transforms the data into a format suitable for training.
4. **Model Training**: Trains machine learning models using the processed data.
5. **Model Evaluation**: Evaluates the model using metrics like F1-Score, Precision, and Recall.
6. **Prediction**: Uses the trained model to predict outcomes on new data.
7. **Artifact Synchronization**: Synchronizes the model and pipeline artifacts to an AWS S3 bucket.

## Tech Stack

- **Python**: The primary programming language for data processing, model training, and API development.
- **FastAPI**: For building the RESTful API for handling data ingestion and predictions.
- **MLflow**: For model tracking, versioning, and managing machine learning experiments.
- **DagsHub**: For version control and managing machine learning experiments.
- **AWS**: For storing models and artifacts in S3.
- **MongoDB**: Used to store network data for training the models.
- **Docker**: Containerizes the application for easy deployment and consistent environments.
- **GitHub Actions**: Automates CI/CD pipeline to test, build, and deploy the project.
- **scikit-learn**: For building and evaluating machine learning models.

## Screenshots
