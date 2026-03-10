"""
Forward-facing API layer. This is the only public HTTP surface.

Backend agentic work and microservice orchestration live in core.gateway
and are not exposed directly.
"""
import os

from fastapi import APIRouter, Body, FastAPI, Query

import clients.google_client as GoogleClient

app = FastAPI(title="Apartment Hunter API")

v1 = APIRouter(prefix="/v1", tags=["v1"])


def _get_google_api_key() -> str:
    """Lazy load so app starts without key (e.g. health check in CI)."""
    key = os.environ.get("GOOGLE_API_KEY")
    if not key:
        raise ValueError("GOOGLE_API_KEY environment variable is required for search")
    return key


@app.get("/")
def health():
    return {"status": "healthy"}


@v1.post("/search_nearby")
async def search_nearby(
    max_results: int = Query(20, ge=1, le=20),
    lat: float = Query(..., description="Latitude"),
    longi: float = Query(..., description="Longitude (west = negative)"),
    radius: int = Query(500, ge=1, description="Search radius in meters"),
    included_types: list[str] = Body(..., embed=False),
) -> dict:
    """JSON body = array of Table A types; query params = lat, longi, radius, max_results."""
    query = {
        "latitude": lat,
        "longitude": longi,
        "radius": float(radius),
        "secret": _get_google_api_key(),
    }
    config = {"includedType": included_types, "results": max_results}
    return GoogleClient.search_nearby(query, config)


@v1.get("/profile")
async def get_profile(name: str = Query(..., description="Profile name")):
    """Return user profile by name. Not implemented yet."""
    return {"error": "not_implemented", "message": "Profile lookup coming soon"}


app.include_router(v1)