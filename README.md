# FastAPI Production Template

A production-style FastAPI starter template featuring layered architecture, PostgreSQL, SQLAlchemy, Alembic migrations, Dockerized local development, and clean API organization.

This project is designed as a reusable backend foundation for building Python APIs with a structure that scales beyond simple tutorial apps.

## Features

* FastAPI-based REST API
* Dockerized local development
* PostgreSQL integration
* SQLAlchemy ORM
* Alembic database migrations
* Layered architecture (endpoints, services, repositories)
* CRUD example with pagination and filtering
* Swagger/OpenAPI docs
* Pytest-based API tests
* Ruff and Black for linting and formatting
* GitHub Actions CI

## Project Structure

```text
app/
  api/
    v1/
      endpoints/
  core/
  db/
  models/
  repositories/
  schemas/
  services/
alembic/
```

## Folder Overview

* `api` - route definitions and versioned endpoints
* `services` - business logic layer
* `repositories` - data access layer
* `schemas` - request and response models
* `models` - SQLAlchemy ORM models
* `db` - database session and metadata setup
* `core` - application configuration and shared settings
* `alembic` - database migration scripts

## Requirements

* Docker Desktop
* Python 3.12 recommended for local tooling

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/edwardgnt/fastapi-production-template.git
cd fastapi-production-template
```

### 2. Start the application

```bash
docker compose up --build
```

### 3. Open the API

* API root: `http://localhost:8000/`
* Swagger docs: `http://localhost:8000/docs`
* Health check: `http://localhost:8000/api/v1/health/`

## Development Commands

Start the application:

```bash
docker compose up --build
```

Run linting:

```bash
docker compose exec api ruff check .
```

Format code:

```bash
docker compose exec api black .
```

Apply database migrations:

```bash
docker compose exec api alembic upgrade head
```

Run tests:

```bash
docker compose exec api pytest
```

## Database Migrations

Create a new migration:

```bash
docker compose exec api alembic revision --autogenerate -m "describe change"
```

Apply migrations:

```bash
docker compose exec api alembic upgrade head
```

## Example Endpoints

### Health

* `GET /api/v1/health/`

### Items

* `GET /api/v1/items/`
* `GET /api/v1/items/{item_id}`
* `POST /api/v1/items/`
* `PUT /api/v1/items/{item_id}`
* `DELETE /api/v1/items/{item_id}`

`GET /api/v1/items/` supports:

* `skip`
* `limit`
* `search`

## Example Request

### Create an item

```json
{
  "name": "First Item",
  "description": "Testing FastAPI + Postgres"
}
```

## Why This Template Exists

This repository was built as a reusable FastAPI backend foundation for production-style Python API development. It emphasizes clean separation of concerns, database migrations, containerized development, and patterns that translate well from enterprise backend systems.

## Roadmap

* Add standardized error handling
* Add authentication and authorization example
* Add test fixtures and database isolation
* Add a reusable base test setup
* Add example deployment workflow
