import allure
import pytest
from conftest import page
from pages.model.login_page import LoginPage
from pages.model.allitems_page import AllItemsPage
from pages.model.header_page import HeaderPage
from pages.model.cart_page import CartPage
from utils.config import USERNAME, PASSWORD


@allure.epic("UI Testing")
@allure.feature("Cart")
@allure.story("User can add item to cart")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.ui
@pytest.mark.smoke
@pytest.mark.critical
def test_add_to_cart(page):
    with allure.step("Open login page"):
        login = LoginPage(page)
        login.goto()

    with allure.step("Enter valid username and password and click login button"):
        login.login(USERNAME, PASSWORD)

    item_label = "Sauce Labs Backpack"
    with allure.step("Click item backpack"):
        all_items = AllItemsPage(page)
        all_items.add_or_remove_item_from_cart(item_label, isAdding=True)

    with allure.step("Verify shopping cart badge is displayed and has correct count=1"):
        header = HeaderPage(page)
        assert header.shopping_cart_badge().is_visible() and \
            header.shopping_cart_badge().inner_text() == "1"

    with allure.step("Click shopping cart link"):
        header.click_shopping_cart_link()

    with allure.step("Verify cart page is displayed and item backpack is present in the cart"):
        cart = CartPage(page)
        assert "cart" in page.url
        cart.expect_cart_inventory_item_toBeVisible(item_label, isVisible=True)