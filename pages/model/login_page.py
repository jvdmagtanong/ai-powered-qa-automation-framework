from pages import locator
from utils.config import BASE_UI_URL
from pages.model.base_page import BasePage, LocatorStrategy
from pages.locator.login_locator import LoginLocator

class LoginPage(BasePage):

    def __init__(self, page):
        super().__init__(page)

    def goto(self):
        self.page.goto(BASE_UI_URL)

    def login_button(self):
        role, name = LoginLocator.LOGIN_BUTTON_ROLE
        locator = self.get_element( 
            LoginLocator.LOGIN_BUTTON,
            LocatorStrategy.ROLE_AND_DESCRIPTION, role, name
        )
        return locator

    def username_input(self):
        return self.get_element(
            LoginLocator.USERNAME_INPUT,
            LocatorStrategy.TEXT,
            element_description=LoginLocator.USERNAME_INPUT_LABEL
        )

    def password_input(self):
        return self.get_element(
            LoginLocator.PASSWORD_INPUT,
            LocatorStrategy.TEXT,
            element_description=LoginLocator.PASSWORD_INPUT_LABEL
        )

    def error_message(self):
        return self.get_element(LoginLocator.ERROR_MESSAGE, LocatorStrategy.LOCATOR)

    def login(self, username, password):
        self.actions.fill(self.username_input(), username)
        self.actions.fill(self.password_input(), password)
        self.actions.click(self.login_button())

    def verify_error_message(self, expected_message):
        error_message = self.error_message()
        self.actions.wait_for_visible(error_message)
        self.verifications.verify_element_has_text(error_message, expected_message)
    