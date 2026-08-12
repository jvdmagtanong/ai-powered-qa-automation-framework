import pytest
import allure
from utils.api_logger import log_api_response


@allure.epic("API Testing")
@allure.feature("Posts Endpoint")
@allure.story("Get all posts")
@pytest.mark.api
@pytest.mark.regression
def test_get_posts(api_client):
    response = api_client.get("/posts")

    log_api_response(response)
    assert response.status_code == 200

    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0


@allure.epic("API Testing")
@allure.feature("Posts Endpoint")
@allure.story("Get all posts by userId")
@pytest.mark.api
@pytest.mark.regression
def test_get_posts_by_user(api_client):
    response = api_client.get("/posts?userId=1")

    log_api_response(response)
    assert response.status_code == 200

    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0
    non_matching_posts = [post for post in data if post["userId"] != 1]
    assert len(non_matching_posts) == 0


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
    post_data = {
        "userId": 1,
        "title": "Jose - Test Post",
        "body": "Testing api - create a post."
    }
    response = api_client.post("/posts", post_data)
    log_api_response(response)
    assert response.status_code == 201
    data = response.json()
    assert isinstance(data, dict)
    assert "id" in data
    for key, value in post_data.items():
        assert data[key] == value


@allure.epic("API Testing")
@allure.feature("Posts Endpoint")
@allure.story("Create a post with incomplete or edge-case payload")
@pytest.mark.api
@pytest.mark.regression
@pytest.mark.parametrize("post_data", [
    pytest.param({"userId": 1, "body": "Test create post."}, id="missing-title"), 
    pytest.param({"userId": 1, "title": "Test Post"}, id="missing-body"),
    pytest.param({"title": "Test Post", "body": "Test create post"}, id="missing-user-id"),
    pytest.param({"userId": 999, "title": "Test Post", "body": "Test create post."}, id="invalid-user-id"),
    pytest.param({"userId": 1, "title": "", "body": ""}, id="empty-values"),
    pytest.param({}, id="empty-payload")
])
def test_create_post_with_incomplete_or_edge_case_payload(api_client, post_data):
    response = api_client.post("/posts", post_data)
    log_api_response(response)
    assert response.status_code == 201
    data = response.json()
    assert isinstance(data, dict)
    assert "id" in data
    for key, value in post_data.items():
        assert data[key] == value


@allure.epic("API Testing")
@allure.feature("Posts Endpoint")
@allure.story("Update a post")
@pytest.mark.api
@pytest.mark.regression
def test_update_post(api_client):
    original_response = api_client.get("/posts/1")
    assert original_response.status_code == 200
    original_data = original_response.json()
    post_data = {
        "id": 1,
        "title": "Updated test post",
        "body": "This post has been updated",
        "userId": 1
    }
    response = api_client.put("/posts/1", data=post_data)
    log_api_response(response)
    assert response.status_code == 200
    updated_data = response.json()
    assert isinstance(updated_data, dict)
    for key, value in post_data.items():
        assert updated_data[key] == value

    assert original_data["title"] != updated_data["title"]
    assert original_data["body"] != updated_data["body"]


@allure.epic("API Testing")
@allure.feature("Posts Endpoint")
@allure.story("Update a post with invalid ID")
@pytest.mark.api
@pytest.mark.regression
@pytest.mark.parametrize("post_id", [999, 0, -1, "abc"])
def test_update_post_with_invalid_id(api_client, post_id):
    post_data = {
        "id": post_id,
        "title": "Updated test post",
        "body": "This post has been updated",
        "userId": 1
    }
    response = api_client.put(f"/posts/{post_id}", data=post_data)
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


