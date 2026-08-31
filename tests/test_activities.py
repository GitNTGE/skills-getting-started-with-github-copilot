def test_get_activities_returns_all_activities_with_expected_shape(client):
    # Arrange
    # (no test-specific setup needed; fixtures provide client + seeded activities)

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    body = response.json()
    assert "Chess Club" in body
    for activity in body.values():
        assert set(["description", "schedule", "max_participants", "participants"]).issubset(activity.keys())
