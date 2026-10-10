# Fleet Track

[English](#english) | [Türkçe](#türkçe) | [Deutsch](#deutsch)

## English

**Purpose**
- Provide endpoints to define rectangular geofences, record vehicle positions, and detect fence violations.

**Verified Features**
- `POST /api/v1/geofences` – create a geofence.
- `POST /api/v1/positions` – record a position and report any violations.
- `GET /api/v1/vehicles` – retrieve latest known positions.
- Transparent bounding‑box calculation.
- In‑memory state for the MVP.

**Stack**
- Python ≥ 3.9
- FastAPI
- Uvicorn (ASGI server)
- Docker & Docker Compose (optional)
- pytest for testing

**Setup & Usage**
```bash
pip install -e ".[dev]"
uvicorn app.main:app --reload
```
Run the test suite:
```bash
pytest -q
```

**Limitations**
- The MVP holds all data in memory; state is lost on restart.
- Geofence checks use a simple axis‑aligned bounding box; no advanced spatial indexing.
- No persistence, authentication, or real‑time streaming in the base implementation.

**License**
See the `LICENSE` file for details.

## Türkçe

**Amaç**
- Dikdörtjen geofence tanımlamak, araç pozisyonlarını kaydetmek ve geçiş ihlallerini raporlamak için uç noktalar sağlar.

**Doğrulanmış Özellikler**
- `POST /api/v1/geofences` – bir geofence oluşturur.
- `POST /api/v1/positions` – bir pozisyon kaydeder ve herhangi bir ihlali bildirir.
- `GET /api/v1/vehicles` – en son 알려진 araç pozisyonlarını döndürür.
- Şeffaf sınırlayıcı kutu hesaplaması.
- MVP için bellek içi durum.

**Yığın**
- Python ≥ 3.9
- FastAPI
- Uvicorn (ASGI sunucusu)
- Docker ve Docker Compose (isteğe bağlı)
- pytest testleri için

**Kurulum & Kullanım**
```bash
pip install -e ".[dev]"
uvicorn app.main:app --reload
```
Test paketini çalıştırın:
```bash
pytest -q
```

**Sınırlamalar**
- MVP tüm veriyi bellekte tutar; yeniden başlatıldığında durum kaybolur.
- Geofence kontrolleri basit eksen‑paralel sınırlayıcı kutu kullanır; gelişmiş uzamsal indeksleme yok.
- Temel uygulamada kalıcılık, kimlik doğrulama veya gerçek‑zamanlı akış yok.

**Lisans**
Detaylar için `LICENSE` dosyasına bakın.

## Deutsch

**Zweck**
- Endpunkte zum Definieren rechteckiger Geofences, Aufzeichnen von Fahrzeugpositionen und Melden von Verstößen bereitstellen.

**Verifizierte Funktionen**
- `POST /api/v1/geofences` – erstellt einen Geofence.
- `POST /api/v1/positions` – zeichnet eine Position auf und meldet eventuelle Verstöße.
- `GET /api/v1/vehicles` – liefert die zuletzt bekannten Positionen.
- Transparente Bounding‑Box‑Berechnung.
- In‑Memory‑Zustand für das MVP.

**Stack**
- Python ≥ 3.9
- FastAPI
- Uvicorn (ASGI‑Server)
- Docker & Docker Compose (optional)
- pytest zum Testen

**Setup & Nutzung**
```bash
pip install -e ".[dev]"
uvicorn app.main:app --reload
```
Testsuite ausführen:
```bash
pytest -q
```

**Einschränkungen**
- Das MVP hält alle Daten im Speicher; beim Neustart geht der Zustand verloren.
- Geofence‑Prüfungen verwenden eine einfache achsenparallel ausgerichtete Bounding Box; es gibt keine räumliche Indizierung.
- Keine Persistenz, Authentifizierung oder Echtzeit‑Streaming in der Basisimplementierung.

**Lizenz**
Siehe die `LICENSE` Datei für Details.
