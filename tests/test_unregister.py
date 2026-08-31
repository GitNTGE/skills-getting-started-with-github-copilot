from src.app import activities


def test_unregister_removes_participant_and_returns_success_message(client):
    # Arrange
    activity_name = "Chess Club"
    email = "michael@mergington.edu"  # already signed up in the seed data

    # Act
    response = client.post(f"/activities/{activity_name}/unregister", params={"email": email})

    # Assert
    assert response.status_code == 200
    assert response.json() == {"message": f"Unregistered {email} from {activity_name}"}
    assert email not in activities[activity_name]["participants"]


def test_unregister_from_unknown_activity_returns_404(client):
    # Arrange
    email = "michael@mergington.edu"

    # Act
    response = client.post("/activities/Nonexistent Club/unregister", params={"email": email})

    # Assert
    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"


def test_unregister_email_not_signed_up_returns_400(client):
    # Arrange
    activity_name = "Chess Club"
    email = "notregistered@mergington.edu"

    # Act
    response = client.post(f"/activities/{activity_name}/unregister", params={"email": email})

    # Assert
    assert response.status_code == 400
    assert response.json()["detail"] == "Student is not signed up for this activity"
