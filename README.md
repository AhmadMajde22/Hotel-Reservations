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

## 📁 Project Structure

The project is organized into the following directory structure:

├── artifacts/                  # Stores model files, raw/processed data
│   ├── models/                 # Model files
│   ├── processed/              # Processed data
│   └── raw/                    # Raw data
│
├── config/                     # Configuration files and parameter settings
│   ├── init.py                 # Initialization script for config
│   ├── config.yaml             # YAML configuration file
│   ├── credentials.json        # Credentials for accessing external services
│   ├── model_params.py         # Model-specific parameter settings
│   └── path_config.py          # Path configuration for directories and files
│
├── custom_jenkins/             # Jenkins-related files
│   └── Dockerfile              # Dockerfile for Jenkins container
│
├── logs/                       # Application logs
│
├── mlruns/                     # MLflow tracking logs and runs
│   └── ...                     # Auto-generated experiment artifacts
│
├── notebook/                   # Jupyter notebooks for exploratory data analysis (EDA) and testing
│   ├── notebook.ipynb          # Jupyter notebook for analysis
│   └── train.csv               # Training data for the notebook
│
├── pipeline/                   # Pipeline execution scripts
│   ├── init.py                 # Initialization script for pipeline
│   └── training_pipeline.py    # Training pipeline script
│
├── src/                        # Core source code for ML components
│   ├── init.py                 # Initialization script for src
│   ├── custom_exception.py     # Custom exceptions used across the project
│   ├── data_ingestion.py       # Script for data ingestion
│   ├── data_preprocessing.py   # Data preprocessing script
│   ├── logger.py               # Custom logging configuration
│   └── model_training.py       # Script for model training
│
├── static/                     # Static files for UI
│   ├── background.jpg          # Background image for the UI
│   └── style.css               # CSS for styling the UI
│
├── templates/                  # HTML templates for the web interface
│   └── index.html              # Main HTML template for the app
│
├── utils/                      # Utility functions
│   ├── init.py                 # Initialization script for utils
│   └── common_function.py      # Common functions used across the project
│
├── .env                        # Environment variables
├── .gitignore                  # Git ignored files
├── application.py              # FastAPI app entrypoint
├── db.py                       # Database connection logic
├── docker-compose.yml          # Docker orchestration file
├── Dockerfile                  # Docker image definition
├── Jenkinsfile                 # Jenkins pipeline configuration
├── README.md                   # Project documentation
├── requirements.txt            # Project dependencies
└── setup.py                    # Package installation script
