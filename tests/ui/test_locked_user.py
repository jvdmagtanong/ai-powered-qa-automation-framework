from pages.login_page import LoginPage


def test_locked_user(page):
    login = LoginPage(page)

    login.goto()
    login.login("locked_out_user", "secret_sauce")

    error_message = page.locator("[data-test='error']")

    assert error_message.is_visible()

    assert (
        "Sorry, this user has been locked out."
        in error_message.text_content()
    )