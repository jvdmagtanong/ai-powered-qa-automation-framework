import os
from google import genai


def suggest_locator_for_element(element_description, failed_locator, page_source):
    """
    Ask Gemini to suggest an alternative Playwright locator
    based on the current page DOM.
    """

    prompt = f"""
        You are an expert SDET specializing in Playwright.

        A Playwright locator failed to find an element.

        Element description:
        {element_description}

        Failed locator:
        {failed_locator}

        Current page HTML:
        {page_source[:10000]}

        Suggest ONE alternative Playwright locator that is most likely
        to identify the same element.

        Prefer locators in this order:
        1. data-testid or data-test
        2. accessible role + name
        3. label
        4. stable CSS selector
        5. text selector

        Return ONLY the locator string.
        Do not include markdown.
        Do not include explanations.
        """
    return ask_gemini(prompt)

def suggest_locator_for_elements(element_description, failed_locator, page_source):
    prompt = f"""
        You are an expert Playwright and QA Automation Engineer.

        The original Playwright locator below is intended to identify a LIST or COLLECTION of similar elements, not a single specific element.

        Original locator:
        {failed_locator}

        Element description:
        {element_description}

        The locator has failed or no longer identifies the expected collection.

        Your task is to find an alternative Playwright locator that identifies the SAME TYPE OF ELEMENTS as the original locator.

        IMPORTANT:

        * Return a locator for the COLLECTION/LIST of elements.
        * Do NOT return a locator for one specific item.
        * The returned locator must be usable with Playwright's `.filter(has_text=...)` method.
        * The test code will use the returned locator to find a specific item by its text afterward.
        * The locator should therefore identify the parent/container elements representing each item in the collection.
        * Prefer stable attributes such as `data-test`, `data-testid`, semantic roles, meaningful ARIA attributes, or stable CSS attributes.
        * Avoid generated classes, dynamic IDs, nth-child selectors, positional selectors, or other brittle selectors when possible.
        * The locator must be valid Playwright Python syntax.
        * Return ONLY the locator itself. Do not include Markdown, explanations, quotes, or additional text.

        Example:

        Original locator:
        [data-test='inventory-item']

        Element description:
        inventory item collection

        Good response:
        [data-test='inventory-item']

        Bad response:
        [data-test='inventory-item']:has-text('Sauce Labs Backpack')

        The bad response is incorrect because it identifies one specific item rather than the collection.

        HTML:
        {page_source[:10000]}
        """
    return ask_gemini(prompt)

def ask_gemini(prompt: str):
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        return None

    client = genai.Client(api_key=api_key)

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
        )

        if response.text:
            return response.text.strip()

        return None

    except Exception as e:
        print(f"Gemini locator healing error: {e}")
        return None
    