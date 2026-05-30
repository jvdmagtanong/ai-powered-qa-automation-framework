from utils.config import BASE_UI_URL

class LoginPage:
    def __init__(self, page):
        self.page = page

    def goto(self):
        self.page.goto(BASE_UI_URL)

    def login(self, username, password):
        self.page.fill("#user-name", username)
        self.page.fill("#password", password)
        self.page.click("#login-button")