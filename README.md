# Arabic Pronunciation Correction App

This project is a full-stack web application designed to help users improve their Arabic pronunciation. The system provides features like user authentication, audio file analysis, and results display.

## Project Structure
```
project/ 
├── backend/ # Backend Flask application 
├── db/ # PostgreSQL database configuration 
├── frontend/ # React frontend application 
├── docker-compose.yml 
├── README.md
```

## Prerequisites

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

## Getting Started

### Step 1: Clone the Repository

```bash
git clone <repository-url>
cd <repository-directory>
```

### Step 2: Build and Start the Containers
```
docker-compose up --build
```

This will:

- Set up a PostgreSQL database.
- Start the Flask backend on http://localhost:5001.
- Launch the React frontend on http://localhost:3001.

### Step 3: Access the Application
- Frontend: http://localhost:3001
- Backend: http://localhost:5001
- Database: Accessible via port 5432.

## Features

1. User Authentication:
- Register and log in securely.
2. Audio Analysis:
- Upload an audio file and specify the expected text.
- Receive analysis results.

## Environment Variables

Environment variables can be set in the `docker-compose.yml` file. Key variables include:

- POSTGRES_USER
- POSTGRES_PASSWORD
- POSTGRES_DB
- DATABASE_URL

## Database Schema

### Users Table
id: Unique identifier.
username: Unique username.
password_hash: Hashed password.
created_at: Timestamp of account creation.

### Analysis Table
id: Unique identifier.
user_id: Foreign key referencing users.
audio_path: Path to the uploaded audio file.
expected_text: Text provided by the user.
result: Result of the analysis.
created_at: Timestamp of the analysis.

## Development Notes

- Frontend: React application with TypeScript.
- Backend: Flask with Python for API development.
- Database: PostgreSQL with schema initialization in db/init/init.sql.

## Future Enhancements

- Add support for additional languages.
- Implement advanced analysis using machine learning.
- Enable persistent user sessions.

## Troubleshooting

- Ensure Docker is running before executing docker-compose up.
- If a container fails to start, check the logs:
```
docker-compose logs <service-name>
```

## License

This project is licensed under the MIT License.
