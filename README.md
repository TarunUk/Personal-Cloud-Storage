Serverless Personal Cloud Storage System

A cloud-based file storage application built using AWS serverless architecture. This project allows users to upload and manage files through a scalable cloud infrastructure without managing traditional servers.

Project Overview

The Serverless Personal Cloud Storage System demonstrates how modern cloud services can be integrated to create a scalable and efficient file storage application.

The application uses AWS serverless services to process user requests, store files securely, and host the frontend interface.

Architecture
User
  ↓
Frontend (AWS Amplify)
  ↓
API Gateway
  ↓
AWS Lambda
  ↓
Amazon S3
Flow

User opens the web application.

The frontend sends an API request.

API Gateway triggers the Lambda function.

Lambda processes the request.

File is stored in Amazon S3.

Technologies Used
Cloud Services

AWS Lambda

Amazon API Gateway

Amazon S3

AWS Amplify

Amazon Cognito

DevOps Tools

Docker

GitHub Actions

Programming & Web

Python

HTML

Git

GitHub

Features

Serverless backend architecture

Secure file upload to cloud storage

Scalable cloud infrastructure

CI/CD automation pipeline

Docker containerization support

CI/CD Pipeline

This project includes an automated CI/CD workflow using GitHub Actions.

Pipeline flow:

Developer pushes code
        ↓
GitHub Repository
        ↓
GitHub Actions CI/CD Pipeline
        ↓
Application build & deployment

This improves development efficiency and automates deployment processes.

Docker Support

The project includes a Dockerfile to containerize the application for consistent deployment environments.

To build the Docker image:

docker build -t cloud-storage-app .

To run the container:

docker run cloud-storage-app
Project Structure
personal-cloud-storage
│
├── .github
│   └── workflows
│        └── main.yml
│
├── screenshots
├── frontend.zip
├── index.html
├── lambda_function.py
├── Dockerfile
└── README.md
Learning Outcomes

This project helped in understanding:

Serverless cloud architecture

AWS service integration

API-based backend development

CI/CD automation pipelines

Docker containerization

Author

Tarun Rajput

GitHub: https://github.com/TarunUk
