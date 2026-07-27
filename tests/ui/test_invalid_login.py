import allure
from pages.login.login_page import LoginPage


@allure.epic("UI Testing")
@allure.feature("Authentication")
@allure.story("Invalid Login")
@allure.severity(allure.severity_level.CRITICAL)
def test_invalid_login(page):
    login = LoginPage(page)

    with allure.step("Open login page"):
        login.goto()

    with allure.step("Enter invalid username and invalid password and click login button"):
        login.login("invalid_user", "wrong_password")

    with allure.step("Verify error message is displayed"):
        error_message = page.locator("[data-test='error']")
        assert error_message.is_visible()
        assert (
            "Username and password do not match" 
            in error_message.text_content()
        )