from fastapi.testclient import TestClient

from src.app import app


client = TestClient(app)


def test_delete_participant_removes_student_from_activity():
    original = client.get("/activities").json()["Chess Club"]["participants"]

    try:
        response = client.delete(
            "/activities/Chess Club/participants?email=michael@mergington.edu"
        )

        assert response.status_code == 200
        assert response.json() == {
            "message": "Removed michael@mergington.edu from Chess Club"
        }

        updated = client.get("/activities").json()["Chess Club"]["participants"]
        assert "michael@mergington.edu" not in updated
    finally:
        client.post("/activities/Chess Club/signup?email=michael@mergington.edu")
