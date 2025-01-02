# Quran Pronunciation Correction App

This project is a full-stack web application designed to help users improve their Quran pronunciation. The system provides features like user authentication, audio file analysis, and results display.

## Comment
- 12/22 Only first and last Surah has already been added to the database. Even if you access to Surahs page except first and last Surah page, you cannnot find the Surah; you probably find first or last Surah.

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

2. User Administration
- They can sign up, login and logout.
- They cannot access to the service if they are not logged in.

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

3. Token
- SECRET_KEY
- REFRESH_SECRET_KEY
- TOKEN_EXPIRE_HOURS

## Database Schema

### Phrases Table
id: Unique identifier.
surah_id: Surah number.
ayah_id: Ayah number.
text: Arbic phrase.
phoneme: IPA.
audio_path: The path to the storage which audios are stored.


### Users Table
id: Unique identifier.
username: User name.
email: Email address.
hashed_password: Hash of password.
role: User or admin.

## Development Notes

- Frontend: React application with TypeScript.
- Backend: Flask with Python for API development.
- Database: MySQL with schema initialization in db/init.sql, db/my.cnf, db/users.sql.

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
