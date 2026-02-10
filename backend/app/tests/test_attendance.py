from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_mark_attendance():
    response = client.post(
        "/attendance",
        json={
            "employee_id": "TEST_EMP_1",
            "date": "2026-02-10",
            "status": "Present"
        }
    )

    assert response.status_code in (201, 409)


def test_get_attendance():
    response = client.get("/attendance/TEST_EMP_1")
    assert response.status_code in (200, 404)
