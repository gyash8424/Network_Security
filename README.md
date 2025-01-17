# Network Security - ML Model Pipeline

## Table of Contents
1. [Motivation](#motivation)
2. [Project Description](#project-description)
3. [Video Walkthrough](#video-walkthrough-of-the-project)
4. [Pipeline Stages](#pipeline-stages)
5. [Tech Stack](#tech-stack)
6. [Screenshots](#screenshots)
---
## Motivation
With the increasing prevalence of cyber frauds and threats, user privacy has become more essential than ever. Hackers often attempt to gain sensitive information through phishing attacks. This project aims to protect users from such threats by identifying phishing websites. It can easily be integrated as a tool in larger applications or used for surveillance purposes by enterprises or individual users.

## Project Description
This repository contains a machine learning pipeline for classifying network data as phishing or legitimate. The pipeline involves multiple stages, including data ingestion, data validation, data transformation, model training, and prediction. The project is built to handle large-scale network data and make real-time predictions.

The project involves building and deploying a machine learning model to classify network data. The pipeline ensures automated data handling, model training, and prediction, all while maintaining version control and model management.

## Video walkthrough of the project
[LinkedIn](https://www.linkedin.com/posts/yash-gupta-0712b324b_machinelearning-cybersecurity-ai-activity-7285966626150080513-IH_i?utm_source=share&utm_medium=member_desktop)

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
- **FastAPI**: For building the RESTful API for model training and predictions.
- **MLflow**: For model tracking, versioning, and managing machine learning experiments.
- **DagsHub**: For version control and managing machine learning experiments and for hosting MLflow remotely.
- **AWS**: For storing models and artifacts in S3 container, docker image in ECR and running the application on EC2 instance.
- **MongoDB**: Used to store network data for training the models.
- **Docker**: Containerizes the application for easy deployment and consistent environments.
- **GitHub Actions**: Automates CI/CD pipeline to test, build, and deploy the project.
- **scikit-learn**: For building and evaluating machine learning models.

## Screenshots

### Dev Phase
![Dev Phase](https://github.com/user-attachments/assets/ad4c5755-0c6f-43a9-95c7-7ac11905d99e)
### Testing Phase
![Testing Phase](https://github.com/user-attachments/assets/5b972789-c8ee-40bd-a8e2-c3a96ed65a52)
### MLflow version tracking hosted on Dagshub
![MLflow version tracking hosted on Dagshub](https://github.com/user-attachments/assets/3c0e0599-5d4e-4ec8-99ac-a6c216d71f28)
### AWS Integration
![AWS Integration](https://github.com/user-attachments/assets/282e41ff-8fc5-4c7d-9e40-a832fc1ccce9)
## Automation with GitHub Actions
![Automation with GitHub Actions](https://github.com/user-attachments/assets/4b554a7b-6432-4867-a7f0-bef5939a75c7)






