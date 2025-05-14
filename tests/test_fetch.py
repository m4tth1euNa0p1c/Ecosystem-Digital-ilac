import pytest
import requests
from src.fetch_parse import fetch_json

class DummyResponse:
    def __init__(self, json_data, status_code=200):
        self._json = json_data
        self.status_code = status_code

    def raise_for_status(self):
        if not (200 <= self.status_code < 300):
            raise requests.HTTPError(f"Status code: {self.status_code}")

    def json(self):
        return self._json

def test_fetch_json_success(monkeypatch):
    sample = {"foo": "bar"}
    def mock_get(*args, **kwargs):
        return DummyResponse(sample, status_code=200)

    monkeypatch.setattr(requests, "get", mock_get)
    result = fetch_json("https://example.com/success.json")
    assert result == sample

def test_fetch_json_http_error(monkeypatch):
    def mock_get(*args, **kwargs):
        return DummyResponse(None, status_code=404)

    monkeypatch.setattr(requests, "get", mock_get)
    with pytest.raises(SystemExit) as exc:
        fetch_json("https://example.com/missing.json")
    assert exc.value.code == 1

def test_fetch_json_request_exception(monkeypatch):
    def mock_get(*args, **kwargs):
        raise requests.RequestException("Network error")

    monkeypatch.setattr(requests, "get", mock_get)
    with pytest.raises(SystemExit) as exc:
        fetch_json("https://example.com/error.json")
    assert exc.value.code == 1
