import allure
import pytest
import os
from playwright.sync_api import sync_playwright
from datetime import datetime
from utils.config import HEADED, BASE_API_URL
from utils.api_client import ApiClient
from utils.gemini_failure_analyzer import analyze_test_failure


def pytest_addoption(parser):
    parser.addoption(
        "--headed",
        action="store_true",
        default=False,
        help="Run browser in headed mode"
    )


@pytest.fixture
def page(request):
    cli_headed = request.config.getoption("--headed")
    headed = cli_headed or HEADED

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=not headed)
        page = browser.new_page()
        yield page
        browser.close()


@pytest.fixture
def api_client():
    return ApiClient(BASE_API_URL)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    # Only take screenshot on actual test failure
    if report.when == "call" and report.failed:
        test_name = item.name
        page = item.funcargs.get("page")

        if page:
            screenshots_dir = "test-reports/screenshots"
            os.makedirs(screenshots_dir, exist_ok=True)

            timestamp = datetime.now().strftime(
                "%Y-%m-%d_%H-%M-%S"
            )

            screenshot_path = (
                f"{screenshots_dir}/"
                f"{test_name}_{timestamp}.png"
            )

            page.screenshot(path=screenshot_path)

            allure.attach.file(
                screenshot_path,
                name=f"{test_name}_failure",
                attachment_type=allure.attachment_type.PNG
            )
        
        stack_trace = report.longreprtext
        print(f"\n\n[Gemini AI] Analyzing failure for {test_name}...")
        analysis = analyze_test_failure(test_name, stack_trace)
        
        # print("\n" + "="*40 + "\nGEMINI FAILURE ANALYSIS\n" + "="*40)
        # print(analysis)
        # print("="*40 + "\n")

        allure.attach(
            analysis,
            name="AI Failure Analysis",
            attachment_type=allure.attachment_type.TEXT
        )

