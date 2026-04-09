from fastapi.testclient import TestClient
import pytest

from src.app import activities, app, create_initial_activities


@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture(autouse=True)
def reset_activities():
    activities.clear()
    activities.update(create_initial_activities())
    yield