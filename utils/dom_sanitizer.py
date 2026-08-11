from bs4 import BeautifulSoup

SAFE_ATTRIBUTES = {
    "id",
    "class",
    "name",
    "type",
    "role",
    "data-test",
    "data-testid",
    "aria-label",
    "aria-labelledby",
    "placeholder",
    "href",
}

REMOVE_TAGS = {
    "script",
    "style",
    "iframe",
    "object",
    "embed",
}


def sanitize_dom(page_content: str) -> str:
    soup = BeautifulSoup(page_content, "html.parser")

    # Remove unnecessary tags
    for tag in soup.find_all(REMOVE_TAGS):
        tag.decompose()

    # Remove input values
    for tag in soup.find_all("input"):
        tag.attrs.pop("value", None)

    # Remove textarea contents
    for tag in soup.find_all("textarea"):
        tag.clear()

    # Remove selected state from dropdowns
    for tag in soup.find_all("select"):
        for option in tag.find_all("option"):
            option.attrs.pop("selected", None)

    # Keep only attributes useful for locator healing
    for tag in soup.find_all(True):
        tag.attrs = {
            key: value
            for key, value in tag.attrs.items()
            if key in SAFE_ATTRIBUTES
        }

    return str(soup)