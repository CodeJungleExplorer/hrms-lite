from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_employee():
    response = client.post(
        "/employees",
        json={
            "employee_id": "TEST_EMP_1",
            "full_name": "Test User",
            "email": "testuser1@gmail.com",
            "department": "QA"
        }
    )

    assert response.status_code in (201, 409)


def test_get_employees():
    response = client.get("/employees")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
