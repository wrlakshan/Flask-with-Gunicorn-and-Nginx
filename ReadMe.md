## Setup Instructions

1. Create a virtual environment using Python 3:

    ```bash
    python3 -m venv env
    ```

2. Activate the virtual environment:

    ```bash
    source env/bin/activate
    ```

3. Install Flask using pip:

    ```bash
    pip install Flask
    ```

4. Save the installed packages to a requirements file:

    ```bash
    pip freeze > requirements.txt
    ```

5. Install the dependencies from the requirements file:

    ```bash
    pip install -r ToDo/requirements.txt
    ```

6. Deactivate the virtual environment:

    ```bash
    deactivate
    ```

## Running the Application

To run the Flask application, follow these steps:

1. Activate the virtual environment:

    ```bash
    source env/bin/activate
    ```

2. Run the application using Python:

    ```bash
    python3 todo.py
    ```

    OR

    Run the application using Gunicorn:

    ```bash
    cd ToDo
    gunicorn --bind 0.0.0.0:5000 wsgi:app
    ```

3. Access the application by navigating to `http://localhost:5000` in your web browser.

## Running with Docker

To run the application using Docker, you can use docker-compose:

1. Ensure Docker and docker-compose are installed on your system.

2. Build and run the Docker containers:

    ```bash
    docker-compose up -d --build
    ```

This will start the Flask application in a Docker container. You can access the application by navigating to `http://127.0.0.1:8084/` in your web browser.
