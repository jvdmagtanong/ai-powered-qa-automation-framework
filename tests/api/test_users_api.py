import pytest
import allure
from utils.api_logger import log_api_response
from utils.api_assertions import (
    assert_attributes, 
    assert_response_is_non_empty_list, 
    assert_response_contains_payload
)
from tests.api.data.users_data import (
    VALID_USER,
    UPDATED_USER,
    INVALID_USER_IDS,
    INVALID_USER_PAYLOADS
)


@allure.epic("API Testing")
@allure.feature("Users Endpoint")
@allure.story("Get all users")
@pytest.mark.api
@pytest.mark.regression
def test_get_users(api_client):
    response = api_client.get("/users")

    log_api_response(response)
    assert response.status_code == 200
    data = assert_response_is_non_empty_list(response)
    attributes = ["id", "name", "username", "email"]
    assert_attributes(data[0], attributes)


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
    attributes = ["name", "username", "email"]
    assert_attributes(data, attributes)


@allure.epic("API Testing")
@allure.feature("Users Endpoint")
@allure.story("Get user with invalid ID")
@pytest.mark.api
@pytest.mark.regression
@pytest.mark.parametrize("user_id", INVALID_USER_IDS)
def test_get_user_invalid_id(api_client, user_id):
    response = api_client.get(f"/users/{user_id}")

    log_api_response(response)
    assert response.status_code == 404
    assert response.json() == {}


@allure.epic("API Testing")
@allure.feature("Users Endpoint")
@allure.story("Create a user")
@pytest.mark.api
@pytest.mark.regression
def test_create_user(api_client):
    response = api_client.post(f"/users", VALID_USER)

    log_api_response(response)
    assert response.status_code == 201
    data = assert_response_contains_payload(response, VALID_USER)
    assert "id" in data


@allure.epic("API Testing")
@allure.feature("Users Endpoint")
@allure.story("Update a user")
@pytest.mark.api
@pytest.mark.regression
def test_update_user(api_client):
    original_response = api_client.get("/users/1")
    assert original_response.status_code == 200
    original_data = original_response.json()
    response = api_client.put("/users/1", UPDATED_USER)

    log_api_response(response)
    assert response.status_code == 200

    updated_data = assert_response_contains_payload(response, UPDATED_USER)
    assert original_data["name"] != updated_data["name"]
    assert original_data["username"] != updated_data["username"]


@allure.epic("API Testing")
@allure.feature("Users Endpoint")
@allure.story("Delete a user")
@pytest.mark.api
@pytest.mark.regression
def test_delete_user(api_client):
    response = api_client.delete("/users/1")
    log_api_response(response)
    assert response.status_code == 200
    assert response.json() == {}


@allure.epic("API Testing")
@allure.feature("Users Endpoint")
@allure.story("Create a user with incomplete/edge-case payloads")
@pytest.mark.api
@pytest.mark.regression
@pytest.mark.parametrize("user_data", INVALID_USER_PAYLOADS)
def test_create_user_with_incomplete_payloads(api_client, user_data):
    response = api_client.post(f"/users", user_data)

    log_api_response(response)
    assert_response_contains_payload(response, user_data)


@allure.epic("API Testing")
@allure.feature("Users Endpoint")
@allure.story("Update a user with invalid id")
@pytest.mark.api
@pytest.mark.regression
@pytest.mark.parametrize("user_id", INVALID_USER_IDS)
def test_update_user_with_invalid_id(api_client, user_id):
    response = api_client.put(f"/users/{user_id}", UPDATED_USER)

    log_api_response(response)
    assert response.status_code == 500
    assert "Cannot read properties of undefined" in response.text

