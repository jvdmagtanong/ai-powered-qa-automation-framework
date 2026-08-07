import allure
import pytest
from pages.model.login_page import LoginPage
from utils.config import USERNAME, PASSWORD


@allure.epic("UI Testing")
@allure.feature("Authentication")
@allure.story("Valid Login")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.ui
@pytest.mark.smoke
@pytest.mark.critical
def test_login_success(page):
    login = LoginPage(page)

    with allure.step("Open login page"):
        login.goto()

    with allure.step("Enter valid username and password and click login button"):
        login.login(USERNAME, PASSWORD)

    with allure.step("Verify user lands on dashboard"):
        assert "inventory" in page.url