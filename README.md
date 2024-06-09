# Fraud Detection Dashboard

This project is a full-stack application for detecting and preventing fraud using social media data. The application uses React.js for the frontend, Flask for the backend, PostgreSQL for the database, and PySpark for data processing.

## Tech Stack

- **Frontend:** React.js, Recharts, Axios, Socket.IO Client
- **Backend:** Flask, SQLAlchemy, Flask-SocketIO, Flask-Bcrypt, Tweepy, TextBlob
- **Database:** PostgreSQL
- **Data Processing:** PySpark
- **Containerization:** Docker
- **CI/CD:** GitHub Actions

## Setup Instructions

### Backend

1. Navigate to the backend directory:
    ```
    cd backend
    ```

2. Create and activate a virtual environment:
    ```
    python -m venv venv
    source venv/bin/activate   # On Windows, use `venv\\Scripts\\activate`
    ```

3. Install the required dependencies:
    ```
    pip install -r requirements.txt
    ```

4. Create a `.env` file and add your configuration:
    ```
    SECRET_KEY=your_secret_key
    TWITTER_API_KEY=your_twitter_api_key
    TWITTER_API_SECRET_KEY=your_twitter_api_secret_key
    TWITTER_ACCESS_TOKEN=your_twitter_access_token
    TWITTER_ACCESS_TOKEN_SECRET=your_twitter_access_token_secret
    ```

5. Initialize the database:
    ```
    flask db init
    flask db migrate -m "Initial migration."
    flask db upgrade
    ```

6. Run the Flask application:
    ```
    flask run
    ```

### Frontend

1. Navigate to the frontend directory:
    ```
    cd frontend
    ```

2. Install the required dependencies:
    ```
    npm install
    ```

3. Run the React application:
    ```
    npm start
    ```

### Running with Docker

1. Make sure you have Docker installed on your system.

2. Run the following command to build and start the containers:
    ```
    docker-compose up --build
    ```

## PySpark Data Processing

1. Navigate to the `data-processing` directory:
    ```
    cd backend/data-processing
    ```

2. Run the PySpark script:
    ```
    spark-submit pyspark_script.py
    ```

## CI/CD Pipeline

The project includes a GitHub Actions workflow for CI/CD. The workflow is defined in `.github/workflows/deploy.yml`.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- This project uses [React](https://reactjs.org/), [Flask](https://flask.palletsprojects.com/), [PostgreSQL](https://www.postgresql.org/), and [PySpark](https://spark.apache.org/docs/latest/api/python/).
- Special thanks to the open-source community for providing such powerful tools.



