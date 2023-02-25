import pytest
from fastapi.testclient import TestClient

from app.main.config import create_app
from app.main.helper.logger import init_logger


@pytest.fixture
def client():
    init_logger()
    app = create_app()
    return TestClient(app)
