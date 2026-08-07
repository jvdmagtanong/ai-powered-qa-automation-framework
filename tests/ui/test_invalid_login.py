import allure
import pytest
from pages.model.login_page import LoginPage


@allure.epic("UI Testing")
@allure.feature("Authentication")
@allure.story("Invalid Login")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.ui
@pytest.mark.regression
def test_invalid_login(page):
    login = LoginPage(page)

    with allure.step("Open login page"):
        login.goto()

    with allure.step("Enter invalid username and invalid password and click login button"):
        login.login("invalid_user", "wrong_password")

    with allure.step("Verify error message is displayed"):
        login.verify_error_message("Epic sadface: Username and password do not match any user in this service")