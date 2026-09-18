import allure, pytest
from pages.model.login_page import LoginPage
from pages.model.header_page import HeaderPage
from utils.config import USERNAME, PASSWORD, BASE_UI_URL


@allure.epic("UI Testing")
@allure.feature("Authentication")
@allure.story("Valid Login")
@allure.description("This test verifies that a user can log in successfully with valid credentials and lands on the dashboard.")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.ui
@pytest.mark.smoke
@pytest.mark.critical
def test_login_success(page):
    
    login = LoginPage(page)

    with allure.step("Enter valid username and password and click login button"):
        login.login(USERNAME, PASSWORD)

    with allure.step("Verify user lands on Catalog page and URL contains 'inventory'"):
        header = HeaderPage(page)
        header.verify_page_is_displayed(f"{BASE_UI_URL}/inventory.html", "Products")