import allure, pytest
from pages.model.login_page import LoginPage
from utils.config import USERNAME, PASSWORD


@allure.epic("UI Testing")
@allure.feature("Authentication")
@allure.story("Invalid Login")
@allure.description("This test verifies that an error message is displayed when a user attempts to log in with invalid credentials.")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.ui
@pytest.mark.regression
def test_invalid_login(page):
    
    login = LoginPage(page)
    invalid_credentials_error_message = "Epic sadface: Username and password do not match any user in this service"
    username_required_error_message = "Epic sadface: Username is required"
    password_required_error_message = "Epic sadface: Password is required"

    with allure.step("Enter invalid username and valid password and click login button"):
        login.login("invalid_user", PASSWORD)

    with allure.step("Verify error message is displayed"):
        login.verify_error_message(invalid_credentials_error_message)

    with allure.step("Enter invalid username and invalid password and click login button"):
        login.login("invalid_user", "wrong_password")

    with allure.step("Verify error message is displayed"):
        login.verify_error_message(invalid_credentials_error_message)
    
    with allure.step("Enter valid username and invalid password and click login button"):
        login.login(USERNAME, "wrong_password")

    with allure.step("Verify error message is displayed"):
        login.verify_error_message(invalid_credentials_error_message)

    with allure.step("Enter username in UPPERCASE and valid password and click login button"):
        login.login(USERNAME.upper(), PASSWORD)

    with allure.step("Verify error message is displayed"):
        login.verify_error_message(invalid_credentials_error_message)

    with allure.step("Enter valid username and password in UPPERCASE and click login button"):
        login.login(USERNAME, PASSWORD.upper())

    with allure.step("Verify error message is displayed"):
        login.verify_error_message(invalid_credentials_error_message)

    with allure.step("Leave username blank, enter valid password and click login button"):
        login.login("", PASSWORD)

    with allure.step("Verify error message is displayed"):
        login.verify_error_message(username_required_error_message)

    with allure.step("Leave both username and password blank and click login button"):
        login.login("", "")

    with allure.step("Verify error message is displayed"):
        login.verify_error_message(username_required_error_message)

    with allure.step("Enter valid username, leave password blank and click login button"):
        login.login(USERNAME, "")

    with allure.step("Verify error message is displayed"):
        login.verify_error_message(password_required_error_message)

