import allure
import pytest
from pages.model.login_page import LoginPage


@allure.epic("UI Testing")
@allure.feature("Authentication")
@allure.story("Locked User")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.ui
@pytest.mark.regression
def test_locked_user(page):
    login = LoginPage(page)

    with allure.step("Open login page"):
        login.goto()

    with allure.step("Enter locked out user's valid login credentials and click login button"):
        login.login("locked_out_user", "secret_sauce")

    with allure.step("Verify error message is displayed"):
        login.verify_error_message("Epic sadface: Sorry, this user has been locked out.")