from pages.login_page import LoginPage
from utils.config import USERNAME, PASSWORD

def test_login_success(page):
    login = LoginPage(page)

    login.goto()
    login.login(USERNAME, PASSWORD)

    assert "inventory" in page.url