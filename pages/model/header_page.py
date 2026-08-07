from pages.locator.header_locator import HeaderLocator
from pages.model.base_page import BasePage

class HeaderPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

    def shopping_cart_link(self):
        return self.page.locator(HeaderLocator.SHOPPING_CART_LINK)

    def shopping_cart_badge(self):
        return self.page.locator(HeaderLocator.SHOPPING_CART_BADGE)

    def open_menu_button(self):
        role, name = HeaderLocator.OPEN_MENU_BUTTON_ROLE
        return self.page.locator(HeaderLocator.OPEN_MENU_BUTTON).or_(
            self.page.get_by_role(role, name=name)
        )

    def inventory_sidebar_link(self):
        role, name = HeaderLocator.INVENTORY_SIDEBAR_LINK_ROLE
        return self.page.locator(HeaderLocator.INVENTORY_SIDEBAR_LINK).or_(
            self.page.get_by_role(role, name=name)
        )

    def logout_sidebar_link(self):
        role, name = HeaderLocator.LOGOUT_SIDEBAR_LINK_ROLE
        return self.page.locator(HeaderLocator.LOGOUT_SIDEBAR_LINK).or_(
            self.page.get_by_role(role, name=name)
        )

    def reset_sidebar_link(self):
        role, name = HeaderLocator.RESET_SIDEBAR_LINK_ROLE
        return self.page.locator(HeaderLocator.RESET_SIDEBAR_LINK).or_(
            self.page.get_by_role(role, name=name)
        )

    def close_menu_button(self):
        role, name = HeaderLocator.CLOSE_MENU_BUTTON_ROLE
        return self.page.locator(HeaderLocator.CLOSE_MENU_BUTTON).or_(
            self.page.get_by_role(role, name=name)
        )

    def click_shopping_cart_link(self):
        self.click(self.shopping_cart_link())

    def click_open_menu_button(self):
        if self.is_visible(self.open_menu_button()):
            self.click(self.open_menu_button())

    def click_inventory_sidebar_link(self):
        self.click_open_menu_button()
        self.click(self.inventory_sidebar_link())

    def click_logout_sidebar_link(self):
        self.click_open_menu_button()
        self.click(self.logout_sidebar_link())

    def click_reset_sidebar_link(self):
        self.click_open_menu_button()
        self.click(self.reset_sidebar_link())

    def click_close_menu_button(self):
        if self.is_visible(self.close_menu_button()):
            self.click(self.close_menu_button())