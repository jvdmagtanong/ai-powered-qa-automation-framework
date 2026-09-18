import allure, pytest
from pages.model.login_page import LoginPage
from utils.config import BASE_UI_URL

@allure.epic("UI Testing")
@allure.feature("Authentication")
@allure.story("Locked User")
@allure.description("This test verifies that an error message is displayed when a locked out user attempts to log in with valid credentials.")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.ui
@pytest.mark.regression
def test_locked_user(page):

    login = LoginPage(page)

    with allure.step("Enter locked out user's valid login credentials and click login button"):
        login.login("locked_out_user", "secret_sauce")

    with allure.step("Verify Login page is still displayed"):
        login.verify_login_page_is_displayed(f"{BASE_UI_URL}/")

    with allure.step("Verify error message is displayed"):
        login.verify_error_message("Epic sadface: Sorry, this user has been locked out.")