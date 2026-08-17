from fastapi.testclient import TestClient

from app.main import Geofence, Position, create_app, inside


def test_geofence_math() -> None:
    fence = Geofence(
        name="depot", min_latitude=40, max_latitude=41, min_longitude=28, max_longitude=29
    )
    assert inside(Position(vehicle_id="van-1", latitude=40.5, longitude=28.5, speed_kmh=10), fence)


def test_position_ingestion_reports_latest_state() -> None:
    with TestClient(create_app()) as client:
        client.post(
            "/api/v1/geofences",
            json={
                "name": "depot",
                "min_latitude": 40,
                "max_latitude": 41,
                "min_longitude": 28,
                "max_longitude": 29,
            },
        )
        response = client.post(
            "/api/v1/positions",
            json={"vehicle_id": "van-1", "latitude": 42, "longitude": 28, "speed_kmh": 30},
        )
    assert response.json()["outside_geofences"] == ["depot"]
