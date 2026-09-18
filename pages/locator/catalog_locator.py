from playwright.sync_api import Page

class CatalogLocator:

    INVENTORY_ITEM = "[data-test='inventory-item']"
    ADD_TO_CART_BUTTON_ROLE = ("button", "Add to cart")
    REMOVE_BUTTON_ROLE = ("button", "Remove")
    BACKPACK_ADD_TO_CART_BUTTON = "[data-test='add-to-cart-sauce-labs-backpack']"
    BACKPACK_REMOVE_FROM_CART_BUTTON = "[data-test='remove-sauce-labs-backpack']"
    BIKE_LIGHT_ADD_TO_CART_BUTTON = "[data-test='add-to-cart-sauce-labs-bike-light']"
    BIKE_LIGHT_REMOVE_FROM_CART_BUTTON = "[data-test='remove-sauce-labs-bike-light']"
    BOLT_T_SHIRT_ADD_TO_CART_BUTTON = "[data-test='add-to-cart-sauce-labs-bolt-t-shirt']"
    BOLT_T_SHIRT_REMOVE_FROM_CART_BUTTON = "[data-test='remove-sauce-labs-bolt-t-shirt']"
    FLEECE_JACKET_ADD_TO_CART_BUTTON = "[data-test='add-to-cart-sauce-labs-fleece-jacket']"
    FLEECE_JACKET_REMOVE_FROM_CART_BUTTON = "[data-test='remove-sauce-labs-fleece-jacket']"
    ONESIE_ADD_TO_CART_BUTTON = "[data-test='add-to-cart-sauce-labs-onesie']"
    ONESIE_REMOVE_FROM_CART_BUTTON = "[data-test='remove-sauce-labs-onesie']"
    