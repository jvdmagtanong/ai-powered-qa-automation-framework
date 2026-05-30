from pages.login_page import LoginPage

def test_login_success(page):
    login = LoginPage(page)

    login.goto()
    login.login("standard_user", "secret_sauce")

    assert "inventory" in page.url