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

        The original Playwright locator below is intended to identify a LIST or COLLECTION
        of similar elements.

        Original locator:
        {failed_locator}

        Specific item being searched for:
        {element_description}

        The original locator has failed or no longer identifies the expected collection.

        Your task is to find an alternative Playwright locator that identifies the SAME TYPE
        OF ELEMENTS as the original locator.

        IMPORTANT:

        * "{element_description}" is the SPECIFIC ITEM that the test is looking for.
        * Do NOT return a locator that directly identifies "{element_description}".
        * Instead, identify the COLLECTION or LIST locator that contains "{element_description}".
        * The returned locator will be used by the test code with Playwright's
        `.filter(has_text=...)` method to locate the specific item afterward.
        * The returned locator must therefore match the parent/container elements
        representing each item in the collection.
        * The collection locator must contain the specific item "{element_description}"
        somewhere within its matching elements.
        * Prefer stable attributes such as `data-test`, `data-testid`, semantic roles,
        meaningful ARIA attributes, or stable CSS attributes.
        * Avoid generated classes, dynamic IDs, nth-child selectors, positional selectors,
        or other brittle selectors when possible.
        * The locator must be valid Playwright Python syntax.
        * Return ONLY the locator itself.
        * Do not return Markdown, explanations, quotes, or additional text.

        Example:

        Original locator:
        [data-test='inventory-item']

        Specific item being searched for:
        Sauce Labs Backpack

        Good response:
        [data-test='inventory-item']

        Bad response:
        [data-test='inventory-item']:has-text('Sauce Labs Backpack')

        The bad response is incorrect because it identifies the specific item instead of
        returning the collection locator.

        Another bad response:
        [data-test='inventory-item'] >> text="Sauce Labs Backpack"

        The returned locator must identify the COLLECTION, not the individual item.

        The test will perform the filtering separately, for example:

        collection = page.locator(SUGGESTED_LOCATOR)
        item = collection.filter(has_text="Sauce Labs Backpack")

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
    