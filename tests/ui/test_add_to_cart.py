import allure, pytest
from pages.model.login_page import LoginPage
from pages.model.catalog_page import CatalogPage
from pages.model.header_page import HeaderPage
from pages.model.cart_page import CartPage
from utils.config import USERNAME, PASSWORD, BASE_UI_URL


@allure.epic("UI Testing")
@allure.feature("Cart")
@allure.story("User can add item to cart")
@allure.description("This test verifies that a user can add an item to the cart and the cart badge updates accordingly.")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.ui
@pytest.mark.smoke
@pytest.mark.critical
def test_add_to_cart(page):

    with allure.step("Enter valid username and password and click login button"):
        login = LoginPage(page)
        login.login(USERNAME, PASSWORD)

    item_label = "Sauce Labs Backpack"
    with allure.step("Click Sauce Labs Backpack 'Add to cart' button"):
        catalog_page = CatalogPage(page)
        catalog_page.add_or_remove_item_from_cart(item_label, isAdding=True)

    with allure.step("Verify 'Remove' button is displayed for Sauce Labs Backpack"):
        catalog_page.verify_remove_button_is_displayed(item_label)

    with allure.step("Verify shopping cart badge is displayed and has correct count=1"):
        header = HeaderPage(page)
        header.verify_cart_badge_is_displayed()
        header.verify_cart_badge_contains_count("1")

    with allure.step("Click shopping cart link"):
        header.click_shopping_cart_link()

    with allure.step("Verify cart page is displayed and item backpack is present in the cart"):
        cart = CartPage(page)
        header.verify_page_is_displayed(f"{BASE_UI_URL}/cart.html", "Your Cart")
        cart.verify_cart_inventory_item_visibility(item_label, isVisible=True)

        