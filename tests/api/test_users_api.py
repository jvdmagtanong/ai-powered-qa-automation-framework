import pytest
import allure
from utils.api_logger import log_api_response


@allure.epic("API Testing")
@allure.feature("Users Endpoint")
@allure.story("Get all users")
@pytest.mark.api
@pytest.mark.regression
def test_get_users(api_client):
    response = api_client.get("/users")

    log_api_response(response)
    assert response.status_code == 200

    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0

    user = data[0]
    assert "id" in user
    assert "name" in user
    assert "username" in user
    assert "email" in user


@allure.epic("API Testing")
@allure.feature("Users Endpoint")
@allure.story("Get user by ID")
@pytest.mark.api
@pytest.mark.regression
def test_get_user_id(api_client):
    response = api_client.get("/users/1")

    log_api_response(response)
    assert response.status_code == 200

    data = response.json()
    assert isinstance(data, dict)
    assert data["id"] == 1
    assert "name" in data
    assert "username" in data
    assert "email" in data


@allure.epic("API Testing")
@allure.feature("Users Endpoint")
@allure.story("Get user with invalid ID")
@pytest.mark.api
@pytest.mark.regression
@pytest.mark.parametrize("user_id",[999, "abc", 0, -1, "$@#", "does-not-exist"])
def test_get_user_invalid_id(api_client, user_id):
    response = api_client.get(f"/users/{user_id}")

    log_api_response(response)
    assert response.status_code == 404
    assert response.json() == {}


