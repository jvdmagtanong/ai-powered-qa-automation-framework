from playwright.sync_api import Page


class LoginLocator:

    @staticmethod
    def login_button(page: Page):
        return (
            page.locator("[data-test='login-button']")
            .or_(page.get_by_role("button", name="Login"))
            .or_(page.get_by_text("Login"))
        )

    @staticmethod
    def username_input(page: Page):
        return page.locator("[data-test='username']").or_(
            page.get_by_label("Username")
        )

    @staticmethod
    def password_input(page: Page):
        return page.locator("[data-test='password']").or_(
            page.get_by_label("Password")
        )