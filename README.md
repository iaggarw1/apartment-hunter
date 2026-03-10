# Apartment Hunter

Agentic service to search for apartments within a target price range and area.

## Architecture

- **API (forward-facing)** — `main.py` is the only public HTTP surface. All client traffic goes through versioned routes (e.g. `/v1/search_nearby`, `/v1/profile`).
- **Gateway (backend)** — `core/gateway.py` runs agentic workflows and talks to microservices (DynamoDB, Redis, Secrets). It is not exposed; the API calls into it when needed.

## Setup

- Python 3.8+
- Copy `.env.example` to `.env` and set `GOOGLE_API_KEY` (Google Places API) for `/v1/search_nearby`.

## Run locally

```bash
pip install -e .
uvicorn main:app --reload --port 8080
```

Optional dev deps (e.g. pytest):

```bash
pip install -e ".[dev]"
```

## Run with Docker

```bash
docker compose up --build
```

API: http://localhost:8080 (health: `/`, v1: `/v1/...`). LocalStack for DynamoDB/Secrets: see `docker-compose.yml` and `localstack/init.sh`.

## Tests

```bash
pip install -e ".[dev]"
pytest
```
