from pages.login_page import LoginPage

def test_add_to_cart(page):
    login = LoginPage(page)

    login.goto()
    login.login("standard_user", "secret_sauce")

    page.click("#add-to-cart-sauce-labs-backpack")
    page.click(".shopping_cart_link")

    assert "cart" in page.url