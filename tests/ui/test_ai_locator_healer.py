import pytest
import allure

from utils.gemini_locator_healer import suggest_locator_for_element, suggest_locator_for_elements
from utils.dom_sanitizer import sanitize_dom 
from utils.config import USERNAME, PASSWORD  
from pages.model.login_page import LoginPage

@pytest.mark.skip
def test_ai_locator_healer(page):
    with allure.step("Open login page"):
        login = LoginPage(page)
        login.goto()
        
    page_source = sanitize_dom(page.content())
    # print(f"Page source for healing: {page_source[:500]}...")  # Print first 500 chars for debugging

    result = suggest_locator_for_element(
        element_description="Login button",
        failed_locator="[data-test='wrong-login-button']",
        page_source=page_source
    )

    print(f"\nGemini suggested locator: {result}")
    assert result is not None
    healed_locator = page.locator(result)
    print(f"Healed locator count: {healed_locator.count()}")
    assert healed_locator.count() == 1
    
@pytest.mark.skip
def test_ai_collection_locator_healer(page):
    with allure.step("Open login page"):
        login = LoginPage(page)
        login.goto()

    with allure.step("Enter valid username and password and click login button"):
        login.login(USERNAME, PASSWORD)

    page_source = sanitize_dom(page.content())
    # print(f"Page source for healing: {page_source[:500]}...")  # Print first 500 chars for debugging
    element_description = "Sauce Labs Backpack"
    result = suggest_locator_for_elements(
        element_description=element_description,
        failed_locator="[data-test='inventory-item-wrong']",
        page_source=page_source
    )

    print(f"\nGemini suggested locator: {result}")
    assert result is not None
    healed_locator = page.locator(result)
    print(f"Healed locator count: {healed_locator.count()}")
    assert healed_locator.count() > 0
    item = healed_locator.filter(has_text=element_description)
    assert item.count() == 1
    