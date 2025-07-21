# DJ Requests API

A REST API for DJs to receive song requests from customers via a web form. The API allows users to submit requests, list all requests, and delete specific requests. Data is stored in a PostgreSQL database. The application is containerized using Docker.

## Features
- Submit a song request (JSON input)
- List all requests
- Delete a request

## Tech Stack
- Python 3.11+
- FastAPI
- SQLAlchemy (ORM)
- PostgreSQL
- Docker

## Setup

1. **Clone the repository**
2. **Set environment variables** (see `.env.example`)
3. **Build and run with Docker Compose:**
   ```sh
   docker-compose up --build
   ```

## Environment Variables
- `DATABASE_URL` - PostgreSQL connection string (e.g. `postgresql+psycopg2://user:password@db:5432/djrequests`)

## API Endpoints
- `POST /requests` - Submit a new song request
- `GET /requests` - List all requests
- `DELETE /requests/{id}` - Delete a request by ID

## License
MIT 