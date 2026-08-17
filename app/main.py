from fastapi import FastAPI
from pydantic import BaseModel, Field


class Position(BaseModel):
    vehicle_id: str = Field(min_length=1, max_length=60)
    latitude: float = Field(ge=-90, le=90)
    longitude: float = Field(ge=-180, le=180)
    speed_kmh: float = Field(ge=0, le=400)


class Geofence(BaseModel):
    name: str
    min_latitude: float
    max_latitude: float
    min_longitude: float
    max_longitude: float


def inside(position: Position, fence: Geofence) -> bool:
    return (
        fence.min_latitude <= position.latitude <= fence.max_latitude
        and fence.min_longitude <= position.longitude <= fence.max_longitude
    )


def create_app() -> FastAPI:
    app = FastAPI(title="FleetTrack", version="0.1.0")
    latest: dict[str, Position] = {}
    fences: list[Geofence] = []

    @app.get("/health")
    async def health() -> dict[str, str]:
        return {"status": "ok", "service": "fleet-track"}

    @app.post("/api/v1/geofences", response_model=Geofence)
    async def add_geofence(fence: Geofence) -> Geofence:
        fences.append(fence)
        return fence

    @app.post("/api/v1/positions")
    async def ingest(position: Position) -> dict:
        latest[position.vehicle_id] = position
        violations = [fence.name for fence in fences if not inside(position, fence)]
        return {"position": position, "outside_geofences": violations}

    @app.get("/api/v1/vehicles")
    async def vehicles() -> list[Position]:
        return list(latest.values())

    return app


app = create_app()
