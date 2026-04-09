from src.app import activities


def test_signup_adds_new_participant(client):
    # Arrange
    email = "newstudent@mergington.edu"

    # Act
    response = client.post(f"/activities/Chess Club/signup?email={email}")

    # Assert
    assert response.status_code == 200
    assert response.json() == {"message": f"Signed up {email} for Chess Club"}
    assert email in activities["Chess Club"]["participants"]


def test_signup_rejects_duplicate_participant(client):
    # Arrange
    email = "michael@mergington.edu"

    # Act
    response = client.post(f"/activities/Chess Club/signup?email={email}")

    # Assert
    assert response.status_code == 400
    assert response.json() == {"detail": "Already signed up"}


def test_signup_rejects_unknown_activity(client):
    # Arrange
    email = "newstudent@mergington.edu"

    # Act
    response = client.post(f"/activities/Unknown Club/signup?email={email}")

    # Assert
    assert response.status_code == 404
    assert response.json() == {"detail": "Activity not found"}


def test_signup_requires_email_query_parameter(client):
    # Arrange

    # Act
    response = client.post("/activities/Chess Club/signup")

    # Assert
    assert response.status_code == 422


def test_unregister_removes_existing_participant(client):
    # Arrange
    email = "michael@mergington.edu"

    # Act
    response = client.delete(f"/activities/Chess Club/signup?email={email}")

    # Assert
    assert response.status_code == 200
    assert response.json() == {"message": f"Removed {email} from Chess Club"}
    assert email not in activities["Chess Club"]["participants"]


def test_unregister_rejects_unknown_participant(client):
    # Arrange
    email = "absent@mergington.edu"

    # Act
    response = client.delete(f"/activities/Chess Club/signup?email={email}")

    # Assert
    assert response.status_code == 404
    assert response.json() == {"detail": "Participant not found"}


def test_unregister_rejects_unknown_activity(client):
    # Arrange
    email = "michael@mergington.edu"

    # Act
    response = client.delete(f"/activities/Unknown Club/signup?email={email}")

    # Assert
    assert response.status_code == 404
    assert response.json() == {"detail": "Activity not found"}