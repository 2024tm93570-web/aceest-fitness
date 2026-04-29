import pytest
from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_home(client):
    response = client.get("/")
    assert response.status_code == 200
    data = response.get_json()
    assert "message" in data
    assert data["message"] == "Welcome to ACEest Fitness & Gym"


def test_home_version(client):
    response = client.get("/")
    data = response.get_json()
    assert "version" in data
    assert data["version"] == "2.0.0"


def test_members(client):
    response = client.get("/members")
    assert response.status_code == 200
    data = response.get_json()
    assert "members" in data
    assert len(data["members"]) > 0


def test_members_structure(client):
    response = client.get("/members")
    data = response.get_json()
    for member in data["members"]:
        assert "name" in member
        assert "membership" in member


def test_classes(client):
    response = client.get("/classes")
    assert response.status_code == 200
    data = response.get_json()
    assert "classes" in data
    assert len(data["classes"]) > 0


def test_classes_structure(client):
    response = client.get("/classes")
    data = response.get_json()
    for cls in data["classes"]:
        assert "name" in cls
        assert "time" in cls


def test_health(client):
    response = client.get("/health")
    assert response.status_code == 200
    data = response.get_json()
    assert data["status"] == "healthy"
    assert data["version"] == "2.0.0"


def test_invalid_route(client):
    response = client.get("/invalid")
    assert response.status_code == 404