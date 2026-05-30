import allure
from pages.login_page import LoginPage


@allure.epic("UI Testing")
@allure.feature("Authentication")
@allure.story("Locked User")
@allure.severity(allure.severity_level.CRITICAL)
def test_locked_user(page):
    login = LoginPage(page)

    with allure.step("Open login page"):
        login.goto()

    with allure.step("Enter locked out user's valid login credentials and click login button"):
        login.login("locked_out_user", "secret_sauce")

    with allure.step("Verify error message is displayed"):
        error_message = page.locator("[data-test='error']")
        assert error_message.is_visible()
        assert (
            "Sorry, this user has been locked out."
            in error_message.text_content()
        )