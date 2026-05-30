from pages.login_page import LoginPage


def test_invalid_login(page):
    login = LoginPage(page)

    login.goto()
    login.login("invalid_user", "wrong_password")

    error_message = page.locator("[data-test='error']")

    assert error_message.is_visible()

    assert (
        "Username and password do not match"
        in error_message.text_content()
    )