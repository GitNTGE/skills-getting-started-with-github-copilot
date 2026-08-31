import copy

import pytest
from fastapi.testclient import TestClient

from src.app import app, activities


@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture(autouse=True)
def reset_activities():
    """Restore the in-memory activities dict so tests don't leak state into each other."""
    original = copy.deepcopy(activities)
    yield
    activities.clear()
    activities.update(original)
