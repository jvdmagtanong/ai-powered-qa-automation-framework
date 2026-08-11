import pytest
from playwright.sync_api import sync_playwright
from utils.gemini_locator_healer import suggest_locator_for_element
from utils.dom_sanitizer import sanitize_dom   

@pytest.mark.skip
def test_ai_locator_healer():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        page.goto("https://www.saucedemo.com")

        page_source = sanitize_dom(page.content())
        print(f"Page source for healing: {page_source[:500]}...")  # Print first 500 chars for debugging

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

        browser.close()