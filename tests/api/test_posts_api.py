import pytest
import allure
from utils.api_logger import log_api_response
from utils.api_assertions import assert_response_contains_payload, assert_response_is_non_empty_list
from tests.api.data.posts_data import (
    VALID_POST,
    INVALID_POST_PAYLOADS,
    UPDATED_POST,
    INVALID_POST_IDS,
    get_invalid_update_post_payload
)


@allure.epic("API Testing")
@allure.feature("Posts Endpoint")
@allure.story("Get all posts")
@pytest.mark.api
@pytest.mark.regression
def test_get_posts(api_client):
    response = api_client.get("/posts")

    log_api_response(response)
    assert response.status_code == 200
    assert_response_is_non_empty_list(response)


@allure.epic("API Testing")
@allure.feature("Posts Endpoint")
@allure.story("Get all posts by userId")
@pytest.mark.api
@pytest.mark.regression
def test_get_posts_by_user(api_client):
    response = api_client.get("/posts?userId=1")

    log_api_response(response)
    assert response.status_code == 200
    data = assert_response_is_non_empty_list(response)
    assert all(post["userId"] == 1 for post in data)


@allure.epic("API Testing")
@allure.feature("Posts Endpoint")
@allure.story("Get posts by invalid userId")
@pytest.mark.api
@pytest.mark.regression
@pytest.mark.parametrize("user_id",[999, "abc", 0, -1, "$@#", "does-not-exist"])
def test_get_posts_by_invalid_user(api_client, user_id):
    response = api_client.get(f"/posts?userId={user_id}")

    log_api_response(response)
    assert response.status_code == 200
    assert response.json() == []


@allure.epic("API Testing")
@allure.feature("Posts Endpoint")
@allure.story("Create a post")
@pytest.mark.api
@pytest.mark.regression
def test_create_post(api_client):
    response = api_client.post("/posts", VALID_POST)

    log_api_response(response)
    assert response.status_code == 201
    data = assert_response_contains_payload(response, VALID_POST)
    assert "id" in data


@allure.epic("API Testing")
@allure.feature("Posts Endpoint")
@allure.story("Create a post with incomplete or edge-case payload")
@pytest.mark.api
@pytest.mark.regression
@pytest.mark.parametrize("post_data", INVALID_POST_PAYLOADS)
def test_create_post_with_incomplete_or_edge_case_payload(api_client, post_data):
    response = api_client.post("/posts", post_data)

    log_api_response(response)
    assert response.status_code == 201
    assert_response_contains_payload(response, post_data)


@allure.epic("API Testing")
@allure.feature("Posts Endpoint")
@allure.story("Update a post")
@pytest.mark.api
@pytest.mark.regression
def test_update_post(api_client):
    original_response = api_client.get("/posts/1")
    assert original_response.status_code == 200
    original_data = original_response.json()
    response = api_client.put("/posts/1", data=UPDATED_POST)

    log_api_response(response)
    assert response.status_code == 200

    updated_data = assert_response_contains_payload(response, UPDATED_POST)
    assert original_data["title"] != updated_data["title"]
    assert original_data["body"] != updated_data["body"]


@allure.epic("API Testing")
@allure.feature("Posts Endpoint")
@allure.story("Update a post with invalid ID")
@pytest.mark.api
@pytest.mark.regression
@pytest.mark.parametrize("post_id", INVALID_POST_IDS)
def test_update_post_with_invalid_id(api_client, post_id):
    response = api_client.put(
        f"/posts/{post_id}", 
        get_invalid_update_post_payload(post_id)
    )

    log_api_response(response)
    assert response.status_code == 500
    assert "Cannot read properties of undefined" in response.text


@allure.epic("API Testing")
@allure.feature("Posts Endpoint")
@allure.story("Delete a post")
@pytest.mark.api
@pytest.mark.regression
def test_delete_post(api_client):
    response = api_client.delete("/posts/1")
    log_api_response(response)
    assert response.status_code == 200
    assert response.json() == {}


