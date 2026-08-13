from pages.locator.header_locator import HeaderLocator
from pages.model.base_page import BasePage, LocatorStrategy

class HeaderPage(BasePage):

    def shopping_cart_link(self):
        return self.get_element(HeaderLocator.SHOPPING_CART_LINK, LocatorStrategy.LOCATOR)

    def shopping_cart_badge(self):
        return self.get_element(HeaderLocator.SHOPPING_CART_BADGE, LocatorStrategy.LOCATOR)

    def open_menu_button(self):
        role, name = HeaderLocator.OPEN_MENU_BUTTON_ROLE
        return self.get_element(HeaderLocator.OPEN_MENU_BUTTON, LocatorStrategy.ROLE_AND_DESCRIPTION, role, name)

    def inventory_sidebar_link(self):
        role, name = HeaderLocator.INVENTORY_SIDEBAR_LINK_ROLE
        return self.get_element(HeaderLocator.INVENTORY_SIDEBAR_LINK, LocatorStrategy.ROLE_AND_DESCRIPTION, role, name)

    def logout_sidebar_link(self):
        role, name = HeaderLocator.LOGOUT_SIDEBAR_LINK_ROLE
        return self.get_element(HeaderLocator.LOGOUT_SIDEBAR_LINK, LocatorStrategy.ROLE_AND_DESCRIPTION, role, name)

    def reset_sidebar_link(self):
        role, name = HeaderLocator.RESET_SIDEBAR_LINK_ROLE
        return self.get_element(HeaderLocator.RESET_SIDEBAR_LINK, LocatorStrategy.ROLE_AND_DESCRIPTION, role, name)

    def close_menu_button(self):
        role, name = HeaderLocator.CLOSE_MENU_BUTTON_ROLE
        return self.get_element(HeaderLocator.CLOSE_MENU_BUTTON, LocatorStrategy.ROLE_AND_DESCRIPTION, role, name)

    def click_shopping_cart_link(self):
        self.actions.click(self.shopping_cart_link())

    def click_open_menu_button(self):
        if self.verifications.is_visible(self.open_menu_button()):
            self.actions.click(self.open_menu_button())

    def click_inventory_sidebar_link(self):
        self.click_open_menu_button()
        self.actions.click(self.inventory_sidebar_link())

    def click_logout_sidebar_link(self):
        self.click_open_menu_button()
        self.actions.click(self.logout_sidebar_link())

    def click_reset_sidebar_link(self):
        self.click_open_menu_button()
        self.actions.click(self.reset_sidebar_link())

    def click_close_menu_button(self):
        if self.verifications.is_visible(self.close_menu_button()):
            self.actions.click(self.close_menu_button())

    def verify_car_badge_contains_count(self, count):
        self.verifications.verify_element_is_visible(self.shopping_cart_badge())
        self.verifications.verify_element_has_text(self.shopping_cart_badge(), count)
    