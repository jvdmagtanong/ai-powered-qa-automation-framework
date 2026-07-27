import allure
from pages.login.login_page import LoginPage
from utils.config import USERNAME, PASSWORD


@allure.epic("UI Testing")
@allure.feature("Cart")
@allure.story("User can add item to cart")
@allure.severity(allure.severity_level.CRITICAL)
def test_add_to_cart(page):
    login = LoginPage(page)

    with allure.step("Open login page"):
        login.goto()

    with allure.step("Enter valid username and password and click login button"):
        login.login(USERNAME, PASSWORD)

    with allure.step("Click item backpack"):
        page.click("#add-to-cart-sauce-labs-backpack")

    with allure.step("Click shopping cart link"):
        page.click(".shopping_cart_link")

    with allure.step("Verify cart page is displayed"):
        assert "cart" in page.url