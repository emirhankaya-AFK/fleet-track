# Fleet Track

[English](README.md) | [Türkçe](README_TR.md)

FastAPI telemetry service for vehicle positions and rectangular geofence events.

POST /api/v1/geofences creates a fence; POST /api/v1/positions records a position and reports violations; GET /api/v1/vehicles returns latest positions.

The MVP uses a transparent bounding-box calculation and in-memory state. Production extensions include PostGIS, Redis Streams, WebSockets, auth and trip analytics.

    pip install -e ".[dev]"
    uvicorn app.main:app --reload
    pytest -q

