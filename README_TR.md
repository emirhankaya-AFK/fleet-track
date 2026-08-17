# Fleet Track

[English](README.md) | [Türkçe](README_TR.md)

Araç konumları ve dikdörtgen geofence olayları için FastAPI telemetri servisi.

POST /api/v1/geofences geofence oluşturur; POST /api/v1/positions konum kaydeder ve ihlali bildirir; GET /api/v1/vehicles son konumları döndürür.

MVP şeffaf kutu hesabı ve bellek kullanır. Üretimde PostGIS, Redis Streams, WebSocket, kimlik doğrulama ve rota analizi eklenebilir.

    pip install -e ".[dev]"
    uvicorn app.main:app --reload
    pytest -q

