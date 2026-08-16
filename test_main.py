from fastapi.testclient import TestClient

from main import app
from qr import make_qr

client = TestClient(app)

HEADERS = {"X-API-Key": "demo-free"}


def test_make_qr_returns_png():
    data = make_qr("https://example.com")
    assert data.startswith(b"\x89PNG")


def test_make_qr_respects_size():
    small = make_qr("hi", size=128)
    big = make_qr("hi", size=1024)
    assert len(small) < len(big)


def test_make_qr_rejects_empty():
    try:
        make_qr("   ")
    except ValueError:
        pass
    else:
        raise AssertionError("empty text should raise")


def test_qr_endpoint_returns_image():
    response = client.get(
        "/api/qr",
        params={"text": "https://example.com"},
        headers=HEADERS,
    )
    assert response.status_code == 200
    assert response.headers["content-type"] == "image/png"
    assert response.content.startswith(b"\x89PNG")


def test_qr_endpoint_size():
    response = client.get(
        "/api/qr",
        params={"text": "hi", "size": 256},
        headers=HEADERS,
    )
    assert response.status_code == 200
    assert response.headers["content-type"] == "image/png"


def test_qr_requires_key():
    response = client.get("/api/qr", params={"text": "hi"})
    assert response.status_code == 401


def test_qr_rejects_empty():
    response = client.get("/api/qr", params={"text": ""}, headers=HEADERS)
    assert response.status_code == 400


def test_quota_endpoint():
    response = client.get("/api/quota", headers=HEADERS)
    assert response.status_code == 200
    assert response.json()["tier"] == "free"
