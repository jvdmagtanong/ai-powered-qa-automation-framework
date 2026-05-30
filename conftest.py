import pytest
from playwright.sync_api import sync_playwright

def pytest_addoption(parser):
    parser.addoption(
        "--headed",
        action="store_true",
        default=False,
        help="Run browser in headed mode"
    )


@pytest.fixture
def page(request):
    headed = request.config.getoption("--headed")

    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=not headed
        )

        page = browser.new_page()

        yield page

        browser.close()