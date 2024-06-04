# Air Quality Sensor Data Management API

This project provides a RESTful API to manage air quality sensor data. The API supports functionality to create, read, update, and delete sensor data, with authentication and authorization mechanisms in place. The API is designed to handle concurrent access by multiple clients and ensures high data availability.

## Features

- **CRUD Operations**: Create, read, update, and delete sensor data.
- **Authentication**: Secure access using JWT (JSON Web Tokens).
- **Authorization**: Ensure only authorized users can modify data.
- **API Documentation**: Comprehensive documentation using Swagger (OpenAPI).
- **Error Handling**: Proper error handling with appropriate HTTP status codes and messages.

## Technologies Used

- **Django**: High-level Python web framework.
- **Django REST Framework**: Powerful toolkit for building Web APIs.
- **SimpleJWT**: JSON Web Token authentication for Django REST Framework.
- **drf-yasg**: Automated generation of real Swagger/OpenAPI 2.0 specifications from a Django Rest Framework API.

## Getting Started

### Prerequisites

- Python 3.x
- pip (Python package installer)

### Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/Sam-Po/EcoTrack
    ```

2. **Create a virtual environment**:
    ```sh
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. **Install the required packages**:
    ```sh
    pip install -r requirements.txt
    ```

4. **Apply migrations**:
    ```sh
    python manage.py makemigrations
    python manage.py migrate
    ```

5. **Create a superuser**:
    ```sh
    python manage.py createsuperuser
    ```

6. **Run the development server**:
    ```sh
    python manage.py runserver
    ```

### API Endpoints

#### Authentication

- **Obtain Token**: `/api/token/` [POST]
- **Refresh Token**: `/api/token/refresh/` [POST]

#### Sensors

- **List Sensors**: `/api/sensors/` [GET]
- **Create Sensor**: `/api/sensors/` [POST]
- **Retrieve Sensor**: `/api/sensors/{id}/` [GET]
- **Update Sensor**: `/api/sensors/{id}/` [PUT]
- **Delete Sensor**: `/api/sensors/{id}/` [DELETE]

#### Sensor Data

- **List Sensor Data**: `/api/sensordata/` [GET]
- **Create Sensor Data**: `/api/sensordata/` [POST]
- **Retrieve Sensor Data**: `/api/sensordata/{id}/` [GET]
- **Update Sensor Data**: `/api/sensordata/{id}/` [PUT]
- **Delete Sensor Data**: `/api/sensordata/{id}/` [DELETE]

### API Documentation

Access the Swagger documentation at:
