from fastapi.testclient import TestClient

from app.main import app
from . import dummy_data

client = TestClient(app)


def test_200_map_cargos_to_trucks():
    response = client.post("/mapping/", json=dummy_data.MAPPING_POST_200_INPUT)
    assert response.status_code == 200
    assert response.json() == dummy_data.MAPPING_POST_200_OUTPUT


def test_422_map_cargos_to_trucks():
    response = client.post("/mapping/", json=dummy_data.MAPPING_POST_422_INPUT)
    assert response.status_code == 422
    assert response.json() == dummy_data.MAPPING_POST_422_OUTPUT
