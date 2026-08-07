from playwright.sync_api import expect
from utils.config import BASE_UI_URL
from pages.locator.login_locator import LoginLocator


class LoginPage:
    def __init__(self, page):
        self.page = page

    def goto(self):
        self.page.goto(BASE_UI_URL)

    def login_button(self):
        role, name = LoginLocator.LOGIN_BUTTON_ROLE

        return (
            self.page.locator(LoginLocator.LOGIN_BUTTON)
            .or_(self.page.get_by_role(role, name=name))
            .or_(self.page.get_by_text(name))
        )

    def username_input(self):
            return self.page.locator(LoginLocator.USERNAME_INPUT).or_(
                self.page.get_by_label(LoginLocator.USERNAME_INPUT_LABEL)
            )

    def password_input(self):
        return self.page.locator(LoginLocator.PASSWORD_INPUT).or_(
            self.page.get_by_label(LoginLocator.PASSWORD_INPUT_LABEL)
        )

    def error_message(self):
        return self.page.locator(LoginLocator.ERROR_MESSAGE)

    def login(self, username, password):
        self.username_input().fill(username)
        self.password_input().fill(password)
        self.login_button().click()

    def verify_error_message(self, expected_message):
        error_message = self.error_message()
        expect(error_message).to_be_visible()
        expect(error_message).to_have_text(expected_message)
    