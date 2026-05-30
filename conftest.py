import pytest
import os
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
        browser = p.chromium.launch(headless=not headed)
        page = browser.new_page()

        yield page

        # Screenshot on failure
        if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
            screenshot_dir = "test-reports/screenshots"
            os.makedirs(screenshot_dir, exist_ok=True)

            screenshot_path = f"{screenshot_dir}/{request.node.name}.png"
            page.screenshot(path=screenshot_path)

        browser.close()


# Hook to detect test result
@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_call", rep)