def test_get_activities_returns_seeded_data(client):
    # Arrange

    # Act
    response = client.get("/activities")
    payload = response.json()

    # Assert
    assert response.status_code == 200
    assert "Chess Club" in payload
    assert "Programming Class" in payload


def test_get_activities_returns_expected_activity_shape(client):
    # Arrange

    # Act
    response = client.get("/activities")
    payload = response.json()
    first_activity = payload["Chess Club"]

    # Assert
    assert response.status_code == 200
    assert set(first_activity) == {
        "description",
        "schedule",
        "max_participants",
        "participants",
    }
    assert isinstance(first_activity["participants"], list)


def test_get_activities_is_stable_across_repeated_reads(client):
    # Arrange

    # Act
    first_response = client.get("/activities")
    second_response = client.get("/activities")

    # Assert
    assert first_response.status_code == 200
    assert second_response.status_code == 200
    assert first_response.json() == second_response.json()