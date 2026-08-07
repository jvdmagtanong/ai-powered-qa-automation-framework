from utils.config import BASE_UI_URL
from pages.login.login_locator import LoginLocator


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

    def login(self, username, password):
        self.username_input().fill(username)
        self.password_input().fill(password)
        self.login_button().click()
    