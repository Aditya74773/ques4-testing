import pytest
from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True

    with app.test_client() as client:
        yield client


def test_valid_login(client):
    response = client.post(
        "/login",
        data={
            "username": "admin",
            "password": "admin123"
        }
    )

    assert response.status_code == 200
    assert b"Login successful" in response.data


def test_home_navigation(client):
    response = client.get("/")

    assert response.status_code == 200
    assert b"Q4 Testing Demo Application" in response.data
    assert b"Login" in response.data
    assert b"Form" in response.data


def test_form_validation(client):
    response = client.post(
        "/form",
        data={
            "name": ""
        }
    )

    assert response.status_code == 200
    assert b"Name is required" in response.data