## 📌 Overview

The **Hotel Reservation MLOps Project** is an end-to-end machine learning pipeline designed to predict whether a hotel booking is likely to be canceled. Using historical reservation data, the model identifies patterns and risk factors associated with cancellations, enabling hotels to proactively manage overbooking, optimize resource allocation, and improve customer retention.

This project goes beyond traditional data science by implementing full MLOps practices — including data preprocessing, model training, experiment tracking, versioning, and deployment using modern tools like MLflow, Docker, and Flask. The system is built for scalability and automation, making it suitable for production environments in the hospitality industry.

### 🎯 Use Cases

This solution supports several key business areas for hotel operators:

1. **Revenue Management**: Predicting potential cancellations allows hotels to safely overbook rooms, reducing the risk of lost revenue due to no-shows.
2. **Targeted Marketing**: When a customer is flagged as likely to cancel, personalized offers or discounts can be sent to encourage them to keep their reservation.
3. **Fraud Detection**: The system can help identify suspicious or fraudulent booking behaviors, enabling hotels to take preventative action and block repeat offenders.
4. **Customer Experience**: By understanding cancellation patterns, hotels can improve their services and customer interactions, leading to higher satisfaction and loyalty.

### 🗃️ Dataset Description

The online hotel reservation channels have dramatically changed booking possibilities and customers’ behavior. A significant number of hotel reservations are canceled or result in no-shows. Common reasons for cancellations include changes in plans or scheduling conflicts, often facilitated by flexible cancellation policies. While this flexibility benefits guests, it introduces challenges and potential revenue loss for hotel operators.

You can access the dataset here: [Hotel Reservations Classification Dataset](https://www.kaggle.com/datasets/ahsan81/hotel-reservations-classification-dataset/data)

Below are the available features in the dataset:

- `Booking_ID`: Unique identifier for each booking
- `no_of_adults`: Number of adults included in the booking
- `no_of_children`: Number of children included in the booking
- `no_of_weekend_nights`: Number of weekend nights (Saturday or Sunday) booked or stayed
- `no_of_week_nights`: Number of weekday nights (Monday to Friday) booked or stayed
- `type_of_meal_plan`: Type of meal plan selected. Possible values include [e.g., "Meal Plan 1," "Meal Plan 2," "Meal Plan 3," etc.]
- `required_car_parking_space`: Indicates whether a parking space is required.
- `room_type_reserved`: Type of room reserved (e.g., "Room_Type_1," "Room_Type_2," "Room_Type_3," etc.)
- `lead_time`: Number of days between booking and arrival
- `arrival_year`: Year of arrival
- `arrival_month`: Month of arrival
- `arrival_date`: Day of the month for arrival
- `market_segment_type`: Market segment type. Possible values include [e.g., "Online", "Offline," "Corporate," etc.]
- `repeated_guest`: Indicates whether the customer is a repeated guest
- `no_of_previous_cancellations`: Number of bookings previously canceled by the customer
- `no_of_previous_bookings_not_canceled`: Number of bookings previously completed by the customer
- `no_of_special_requests`: Number of special requests made by the customer
- `booking_status`: Target variable indicating if the booking was canceled

### 🛠️ Create and Activate a Virtual Environment

Before running the project, it's recommended to create a virtual environment to isolate dependencies.

#### 🪟 On Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### 📦 Install Dependencies

With the virtual environment activated, install the required packages using the following command:

```bash
pip install -r requirements.txt
```

or

```bash
pip install -r requirements.txt --no-cache-dir
```

### requirements

```text
pandas==2.2.3
numpy==2.2.4
minio==7.2.15
scikit-learn==1.6.1
pyyaml==6.0.2
imbalanced-learn==0.13.0
lightgbm==4.6.0
scipy==1.15.2
mlflow==2.21.3
flask==3.1.0
psycopg2-binary==2.9.10
```

## 📁 Project Structure

```
.
├── artifacts                  # Stores model files, raw/processed data
│   ├── models                # Model files
│   ├── processed             # Processed data
│   └── raw                   # Raw data
│
├── config                    # Configuration files and parameter settings
│   ├── __init__.py           # Initialization script for config
│   ├── config.yaml           # YAML configuration file
│   ├── credentials.json      # Credentials for external services
│   ├── model_params.py       # Model-specific parameter settings
│   └── path_config.py        # Path configuration for directories
│
├── custom_jenkins          # Jenkins-related files
│   └── Dockerfile           # Dockerfile for Jenkins container
│
├── logs                    # Application logs
│
├── mlruns                  # MLflow tracking logs and runs
│
├── notebook                # Jupyter notebooks for EDA and testing
│   ├── notebook.ipynb      # Jupyter notebook for analysis
│   └── train.csv           # Training data for the notebook
│
├── pipeline               # Pipeline execution scripts
│   ├── __init__.py        # Initialization script for pipeline
│   └── training_pipeline.py # Training pipeline script
│
├── src                    # Core source code for ML components
│   ├── __init__.py        # Initialization script for src
│   ├── custom_exception.py # Custom exceptions
│   ├── data_ingestion.py  # Data ingestion script
│   ├── data_preprocessing.py # Data preprocessing script
│   ├── logger.py          # Custom logging configuration
│   └── model_training.py  # Model training script
│
├── static                 # Static files for UI
│   ├── background.jpg     # Background image
│   └── style.css         # CSS styling
│
├── templates             # HTML templates
│   └── index.html        # Main HTML template
│
├── utils                # Utility functions
│   ├── __init__.py      # Initialization script for utils
│   └── common_function.py # Common utility functions
│
├── .env                  # Environment variables
├── .gitignore           # Git ignored files
├── application.py       # FastAPI app entrypoint
├── db.py               # Database connection logic
├── docker-compose.yml  # Docker orchestration file
├── Dockerfile         # Docker image definition
├── Jenkinsfile        # Jenkins pipeline configuration
├── README.md         # Project documentation
├── requirements.txt  # Project dependencies
└── setup.py         # Package installation script
```

### 🔽 Data Ingestion with MinIO

[MinIO](https://min.io/) serves as our local S3-compatible object storage service for managing datasets in this project.

#### 📦 Installation Steps (Windows)

  **Download MinIO**

- Visit the [MinIO Windows Download Page](https://min.io/download#/windows)
- Download the latest MinIO server binary for Windows

#### 🚀 Running MinIO Server

1. **Start the Server**

   ```powershell
   minio server ~/minio --console-address ":9001"
   ```

2. **Access MinIO**
   - Console URL: <http://localhost:9001>
   - API Endpoint: <http://localhost:9000>
   - Default credentials:
     - Username: `minioadmin`
     - Password: `minioadmin`

### 🔄 Data Preprocessing Pipeline

The project implements a comprehensive data preprocessing pipeline (`DataProcessor` class) that handles various aspects of data preparation. Here's an overview of the main preprocessing steps:

#### 1. Basic Preprocessing

- Removes `Booking_ID` column
- Eliminates duplicate entries
- Separates features into categorical and numerical columns (defined in config)

#### 2. Categorical Data Handling

- Applies Label Encoding to categorical features
- Maintains mapping dictionaries for feature value encoding
- Processes columns like `type_of_meal_plan`, `room_type_reserved`, `market_segment_type`

#### 3. Numerical Data Processing

- Handles skewness in numerical features
- Applies log transformation when skewness exceeds configured threshold
- Processes columns like `lead_time`, `no_of_previous_cancellations`

#### 4. Class Imbalance Handling

- Uses SMOTE (Synthetic Minority Over-sampling Technique)
- Balances the dataset for better model training
- Creates synthetic samples for minority class

#### 5. Feature Selection

- Employs Random Forest for feature importance ranking
- Selects top features based on importance scores
- Reduces dimensionality while maintaining predictive power

#### 6. Data Pipeline Flow

```
Raw Data → Basic Preprocessing → Categorical Encoding →
Numerical Processing → Class Balancing → Feature Selection → Processed Data


The processed data is saved in the `artifacts/processed` directory, ready for model training.
```

### 🤖 Model Training Pipeline

The project uses LightGBM classifier with MLflow tracking for model training and experimentation. Here's an overview of the training pipeline:

#### 1. Data Loading and Splitting

- Loads processed training and test datasets
- Separates features (X) and target variable (booking_status)
- Prepares train-test splits for model training

#### 2. Model Training with LightGBM

- Initializes LightGBM classifier
- Performs hyperparameter tuning using RandomizedSearchCV
- Parameters configured in `config/model_params.py`
- Key hyperparameters include:
  - Learning rate
  - Number of leaves
  - Feature fraction
  - Bagging fraction
  - Max depth

#### 3. Model Evaluation

- Calculates key classification metrics:
  - Accuracy Score
  - Precision Score
  - Recall Score
  - F1 Score
- Logs all metrics to MLflow for tracking

#### 4. MLflow Integration

- Tracks experiments with MLflow
- Logs artifacts:
  - Training dataset
  - Testing dataset
  - Final model
- Records parameters and metrics
- Enables experiment comparison and model versioning

#### Usage Example

```python
from src.model_training import ModelTraining

trainer = ModelTraining(
    train_path=PROCESSED_TRAIN_DATA_PATH,
    test_path=PROCESSED_TEST_DATA_PATH,
    model_output_path=MODEL_OUTPUT_PATH
)
trainer.run()
```

#### MLflow UI Access

To view experiments in MLflow UI:

```bash
mlflow ui --port 5005
```

Then visit: <http://localhost:5005>

The trained model is saved in the `artifacts/models` directory and can be used for making predictions via the FastAPI service.

### 🔄 Training Pipeline

The project implements an end-to-end training pipeline that orchestrates data ingestion, processing, and model training. The pipeline is defined in `pipeline/training_pipeline.py`.

#### Pipeline Components

1. **Data Ingestion**

```python
# Initialize and run data ingestion
config = read_yaml(CONFIG_PATH)
credentials = read_json_credentials(CREDENTIALS_PATH)
data_ingestion = DataIngestion(config=config, credentials=credentials)
data_ingestion.run()
```

2. **Data Processing**

```python
# Process the ingested data
processor = DataProcessor(
    TRAIN_FILE_PATH,
    TEST_FILE_PATH,
    PROCESSED_DIR,
    CONFIG_PATH
)
processor.process()
```

3. **Model Training**

```python
# Train and evaluate the model
trainer = ModelTraining(
    train_path=PROCESSED_TRAIN_DATA_PATH,
    test_path=PROCESSED_TEST_DATA_PATH,
    model_output_path=MODEL_OUTPUT_PATH
)
trainer.run()
```

#### Running the Pipeline

To execute the complete training pipeline:

```bash
python pipeline/training_pipeline.py
```

This will:

- Download data from MinIO storage
- Process and prepare the data for training
- Train the LightGBM model with hyperparameter tuning
- Log experiments to MLflow
- Save the trained model to the artifacts directory

The pipeline uses configuration files to manage parameters and paths:

- `config/config.yaml`: General configuration
- `config/credentials.json`: MinIO credentials
- `config/path_config.py`: System paths

### 💾 Database Integration

The project uses PostgreSQL to store hotel reservation predictions and their outcomes. Database operations are handled in `db.py`.

#### Database Configuration

Create a `.env` file with the following database credentials:

```ini
DB_HOST=localhost
DB_PORT=5432
DB_NAME=hotel_prediction_db
DB_USER=postgres
DB_PASSWORD=123456
```

#### Database Schema

The `reservations` table structure:

```sql
CREATE TABLE reservations (
    id SERIAL PRIMARY KEY,
    lead_time INTEGER,
    no_of_special_request INTEGER,
    avg_price_per_room FLOAT,
    arrival_month INTEGER,
    arrival_date INTEGER,
    market_segment_type INTEGER,
    no_of_week_nights INTEGER,
    no_of_weekend_nights INTEGER,
    type_of_meal_plan INTEGER,
    room_type_reserved INTEGER,
    prediction INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### **Create Database and Table**

   ```bash
   psql -U postgres
   CREATE DATABASE hotel_prediction_db;
   \c hotel_prediction_db
   ```

   Then run the schema SQL above.

#### Features

- Secure connection handling with environment variables
- Automatic connection closing with context managers
- Error handling and logging
- Parameterized queries for SQL injection prevention
- Default fallback values for configuration

### 🌐 Flask Web Application

The project includes a Flask web application (`application.py`) that serves predictions from the trained model.

#### Application Features

- RESTful endpoint for hotel booking cancellation predictions
- Form-based input for booking details
- Database integration for storing predictions
- Model inference using joblib

#### API Endpoint

**Endpoint:** `/`

- **Methods:** GET, POST
- **Input Features:**
  - `lead_time`: Time between booking and arrival
  - `no_of_special_request`: Number of special requests
  - `avg_price_per_room`: Average price per room
  - `arrival_month`: Month of arrival
  - `arrival_date`: Date of arrival
  - `market_segment_type`: Market segment type (encoded)
  - `no_of_week_nights`: Number of weekday nights
  - `no_of_weekend_nights`: Number of weekend nights
  - `type_of_meal_plan`: Type of meal plan (encoded)
  - `room_type_reserved`: Room type (encoded)

### 🐳 Docker Setup

This project is containerized using Docker to ensure consistent development and deployment environments.

#### Dockerfile Structure

Our Dockerfile uses a multi-stage approach for optimal production deployment:

```dockerfile
# Base image
FROM python:slim

# Environment configuration
ENV PYTHONDONTWRITEBYTECODE=1  # Prevents Python from writing pyc files
ENV PYTHONUNBUFFERED=1         # Ensures Python output is sent straight to terminal

# Working directory
WORKDIR /app

# System dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    libgomp1 \    # Required for LightGBM
    libpq-dev \   # PostgreSQL development headers
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Dependencies installation
COPY [requirements.txt](http://_vscodecontentref_/0) .
RUN pip install --no-cache-dir -r [requirements.txt](http://_vscodecontentref_/1)

# Application code
COPY . .
EXPOSE 5000
CMD ["python", "application.py"]
```

### 🛠️ Building the Image

```bash
docker build -t hotel-reservation:latest .
```

### 🏃 Running the Container

```bash
docker run -d -p 5000:5000 hotel-reservation:latest
```

### 🧱 Docker Setup

The project uses **Docker Compose** to orchestrate the FLASK app and a PostgreSQL database.

#### 📄 `docker-compose.yml`

```yaml
version: "3.9"

services:
  app:
    build: .
    ports:
      - "5000:5000"
    depends_on:
      - db
    environment:
      DB_HOST: ${DB_HOST}
      DB_PORT: ${DB_PORT}
      DB_NAME: ${DB_NAME}
      DB_USER: ${DB_USER}
      DB_PASSWORD: ${DB_PASSWORD}
    env_file:
      - .env

  db:
    image: postgres:15
    restart: always
    environment:
      POSTGRES_DB: ${DB_NAME}
      POSTGRES_USER: ${DB_USER}
      POSTGRES_PASSWORD: ${DB_PASSWORD}
    volumes:
      - postgres_data:/var/lib/postgresql/data
    ports:
      - "5432:5432"

volumes:
  postgres_data:

```

### 🏗️ Building and Running the Docker Compose

### 🔁 CI/CD Pipeline (Jenkins)

This project uses a Jenkins pipeline to automate the following tasks:

- Clone the GitHub repository
- Set up a virtual environment and install dependencies
- Build a Docker image
- Log in to Docker Hub
- Push the Docker image to Docker Hub

#### 📄 `Jenkinsfile`

```groovy
pipeline {
    agent any

    environment {
        VENV_DIR = 'venv'
        DOCKER_IMAGE = 'ahmadmajde22/hotel-reservation-app'
        DOCKER_TAG = 'latest'
        DOCKER_HUB_CREDENTIALS = 'docker-hub-credentials' // Jenkins credentials ID
    }

    stages {
        stage('Cloning GitHub repo to Jenkins') {
            steps {
                script {
                    echo 'Cloning GitHub repo to Jenkins...'
                    checkout scmGit(
                        branches: [[name: '*/main']],
                        extensions: [],
                        userRemoteConfigs: [[
                            credentialsId: 'jenkins-github-token',
                            url: 'https://github.com/AhmadMajde22/Hotel-Reservations.git'
                        ]]
                    )
                }
            }
        }

        stage('Creating Virtual Environment') {
            steps {
                script {
                    echo 'Creating Virtual Environment...'
                    sh '''
                    python3 -m venv ${VENV_DIR}
                    . ${VENV_DIR}/bin/activate
                    pip install --upgrade pip
                    pip install -e .
                    '''
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    echo 'Building Docker Image...'
                    sh '''
                    docker build -t ${DOCKER_IMAGE}:${DOCKER_TAG} .
                    '''
                }
            }
        }

        stage('Login to Docker Hub') {
            steps {
                script {
                    echo 'Logging into Docker Hub...'
                    withCredentials([usernamePassword(
                        credentialsId: 'docker-hub-credentials',
                        usernameVariable: 'DOCKER_USERNAME',
                        passwordVariable: 'DOCKER_PASSWORD'
                    )]) {
                        sh '''
                        echo $DOCKER_PASSWORD | docker login -u $DOCKER_USERNAME --password-stdin
                        '''
                    }
                }
            }
        }

        stage('Push Docker Image to Docker Hub') {
            steps {
                script {
                    echo 'Pushing Docker Image to Docker Hub...'
                    sh '''
                    docker push ${DOCKER_IMAGE}:${DOCKER_TAG}
                    '''
                }
            }
        }
    }
}
```

### 🎥 Demo Video

Check out a demonstration of the Hotel Reservation MLOps Project in action:

[![Hotel Reservation MLOps Demo](https://img.youtube.com/vi/ZRFNb0MvJ44/0.jpg)](https://youtu.be/ZRFNb0MvJ44)

The demo showcases:

- Flask web application for predictions
- Database integration with PostgreSQL
