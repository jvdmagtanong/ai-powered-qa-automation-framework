import pytest
import requests
import allure
from utils.config import BASE_API_URL
from utils.api_logger import log_api_response

@allure.epic("API Testing")
@allure.feature("Users Endpoint")
@allure.story("Get all users")
@pytest.mark.api
@pytest.mark.regression
def test_get_users():
    response = requests.get(f"{BASE_API_URL}/users")
    log_api_response(response)

    assert response.status_code == 200

    data = response.json()

    assert isinstance(data, list)
    assert len(data) > 0


@allure.epic("API Testing")
@allure.feature("Posts Endpoint")
@allure.story("Get all posts")
@pytest.mark.api
@pytest.mark.regression
def test_get_posts():
    response = requests.get(f"{BASE_API_URL}/posts")
    log_api_response(response)

    assert response.status_code == 200
    assert len(response.json()) > 0