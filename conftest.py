import os, pytest, allure
from playwright.sync_api import sync_playwright
from datetime import datetime
from utils.config import HEADED, BASE_API_URL, BASE_UI_URL
from utils.api_client import ApiClient
from utils.allure_metadata import get_allure_metadata
from utils.dom_sanitizer import sanitize_dom
from utils.gemini_failure_analyzer import analyze_test_failure
from models.failure_context import FailureContext


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

        with allure.step("Open login page"):
            page.goto(BASE_UI_URL)

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
    if report.when == "call" and (report.failed or getattr(report, "wasxfail", False)):
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
        
        print(f"\n\n[Gemini AI] Analyzing failure for {test_name}...")
        metadata = get_allure_metadata(item)

        context = FailureContext(
            test_name=item.nodeid,
            epic=metadata["epic"],
            feature=metadata["feature"],
            story=metadata["story"],
            description=metadata["description"],
            stack_trace=report.longreprtext,
            page_source=sanitize_dom(page.content()) if page else None,
        )

        analysis = analyze_test_failure(context)
        print(f"\n\n[Gemini AI Response]: \n\n {analysis}")

        allure.attach(
            analysis,
            name="AI Failure Analysis",
            attachment_type=allure.attachment_type.TEXT
        )

