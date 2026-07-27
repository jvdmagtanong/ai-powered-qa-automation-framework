from utils.config import BASE_UI_URL
from pages.login.login_locator import LoginLocator


class LoginPage:
    def __init__(self, page):
        self.page = page

    def goto(self):
        self.page.goto(BASE_UI_URL)

    def login(self, username, password):
        LoginLocator.username_input(self.page).fill(username)
        LoginLocator.password_input(self.page).fill(password)
        LoginLocator.login_button(self.page).click()