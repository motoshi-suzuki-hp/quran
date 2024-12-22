# Quran Pronunciation Correction App

This project is a full-stack web application designed to help users improve their Quran pronunciation. The system provides features like user authentication, audio file analysis, and results display.

## Project Structure
```
project/ 
├── backend/ # Backend Flask application 
├── db/ # MySQL database configuration 
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
docker-compose down --volumes                                                                       (git)-[develop]
docker-compose build --no-cache
docker-compose up
```

This will:

- Set up a MySQL database.
- Start the Flask backend on http://localhost:5001.
- Launch the React frontend on http://localhost:3001.

### Step 3: Access the Application
- Frontend: http://localhost:3001
- Backend: http://localhost:5001
- Database: Accessible via port 3306.

## Features

1. Audio Analysis:
- Record their voice and specify the expected text.
- Receive analysis results.

## Environment Variables

Environment variables used in the `docker-compose.yml` file can be set in the `.env` file. 
(I can share .env file with you, so plese contact me if you need.)
Key variables include:

1. Backend Service
- HUGGINGFACE_TOKEN
- DB_HOST
- DB_PORT
- DB_USER
- DB_PASSWORD
- DB_NAME

2. Database Service
- MYSQL_ROOT_PASSWORD
- MYSQL_DATABASE

## Database Schema

### Phrases Table
id: Unique identifier.
text: Arbic phrase
phoneme: IPA

## Development Notes

- Frontend: React application with TypeScript.
- Backend: Flask with Python for API development.
- Database: MySQL with schema initialization in db/init.sql, db/my.cnf.

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
