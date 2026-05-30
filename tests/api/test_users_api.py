import requests
import allure
from utils.config import BASE_API_URL

@allure.epic("API Testing")
def test_get_users():
    response = requests.get(f"{BASE_API_URL}/users")

    assert response.status_code == 200

    data = response.json()

    assert len(data) > 0
    assert data[0]["id"] == 1