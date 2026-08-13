# AI-Powered QA Automation Framework

A hybrid UI + API test automation framework built with **Python, Playwright, Pytest, Requests, and Allure reporting**.

Designed to demonstrate real-world QA Automation / SDET skills including test design, reusable framework architecture, API testing, reporting, CI/CD, and AI-assisted locator recovery.

---

# Tech Stack

* Python 3.x
* Pytest
* pytest-xdist (Parallel Test Execution)
* pytest-rerunfailures (Test Retries)
* Playwright (UI Automation)
* Requests (API Testing)
* Google Gemini API
* BeautifulSoup4
* Allure Reports (Test Reporting)
* Git / GitHub
* GitHub Actions

---

# Test Sites

**UI:** https://www.saucedemo.com/

**API:** https://jsonplaceholder.typicode.com

---

## Features

* UI automation for e-commerce demo app
* Login and cart workflow tests
* API automation and validation
* Reusable Page Object Model design
* Pytest fixtures for browser management
* Locator strategy abstraction
* AI-assisted locator self-healing
* AI locator healing for individual elements and element collections
* DOM sanitization before sending page content to Gemini
* Allure reporting with locator healing details
* Screenshot capture on UI test failures
* Configurable parallel test execution
* Configurable test retries for transient failures
* CI/CD-ready structure with GitHub Actions

---

# Project Structure

```text
pages/
├── locator/
│   ├── login_locator.py
│   └── cart_locator.py
└── model/
    ├── base_page.py
    ├── base_page_actions.py
    ├── base_page_verifications.py
    ├── base_page_helper.py
    ├── login_page.py
    └── cart_page.py

tests/
├── ui/
│   ├── test_login.py
│   ├── test_invalid_login.py
│   ├── test_locked_user.py
│   └── test_cart.py
└── api/
    ├── data/
    │   ├── posts_data.py
    │   └── users_data.py
    ├── test_posts_api.py
    └── test_users_api.py

utils/
├── api_assertions.py
├── api_client.py
├── api_logger.py
├── config.py
├── dom_sanitizer.py
└── gemini_locator_healer.py

.github/
└── workflows/
    └── tests.yml

run_tests.sh
pytest.ini
requirements.txt
```

---

# Environment Configuration

The framework uses environment variables for local configuration and API credentials.

A `.env` file is required when running the framework locally. The `.env` file is intentionally excluded from Git and must be created by each developer.

Create a `.env` file in the project root:

```bash
touch .env
```

Add the following variables:

```env
BASE_UI_URL=https://www.saucedemo.com
BASE_API_URL=https://jsonplaceholder.typicode.com
USERNAME=standard_user
PASSWORD=secret_sauce
GEMINI_API_KEY=your_gemini_api_key
```

### Gemini API Key

The locator self-healing feature uses Google Gemini to generate alternative Playwright locators when the standard locator fails.

To use AI-assisted locator healing locally:

1. Create a Google AI Studio account.
2. Generate your own Gemini API key.
3. Add the key to your local `.env` file:

```env
GEMINI_API_KEY=your_gemini_api_key
```

Do not share or commit your API key.

The `.env` file is excluded from Git through `.gitignore`.

Without a valid `GEMINI_API_KEY`, the AI-assisted locator healing functionality will not be available.

> Note: The standard UI and API tests do not require you to use someone else's credentials or API key. Each developer should configure their own local environment.

---

# Setup Instructions

## 1. Clone repo

```bash
git clone <repository-url>
cd ai-powered-qa-automation-framework
```

## 2. Create virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

## 4. Install Playwright browsers

```bash
playwright install
```

---

# Running Tests

## Run all tests

```bash
pytest
```

## Run UI tests

```bash
pytest tests/ui
```

## Run API tests

```bash
pytest tests/api
```

---

# API Testing

API tests are implemented using **Requests** and organized by endpoint.

Current coverage includes:

### Users

* Get all users
* Get user by ID
* Create a user
* Update a user
* Delete a user
* Invalid user IDs
* Incomplete and edge-case payloads
* Invalid update IDs

### Posts

* Get posts
* Get post by ID
* Create a post
* Update a post
* Delete a post
* Invalid post IDs
* Invalid and incomplete payloads

Reusable API assertions and test-data modules are used to reduce duplicated validation logic and keep test cases maintainable.

Test data and payloads are separated from the API test implementations:

```text
tests/
└── api/
    ├── data/
    │   ├── posts_data.py
    │   └── users_data.py
    ├── test_posts_api.py
    └── test_users_api.py
```

---

# Locator Self-Healing

The framework includes an AI-assisted locator recovery feature using Google Gemini.

When a standard locator cannot identify the expected element, the framework can send a sanitized version of the current page DOM to Gemini and request an alternative Playwright locator.

The suggested locator is validated locally before it is used.

The framework supports both:

* Individual element locator recovery
* Collection locator recovery, allowing the recovered locator to still be used with Playwright filtering such as `filter(has_text=...)`

The normal locator strategies are always attempted first. AI-assisted recovery is only used as a fallback.

DOM sanitization is performed before page content is sent to Gemini to remove sensitive elements and entered form values, reducing the risk of exposing confidential information to the AI service.

Locator recovery details are also attached to the Allure report, including the original locator, suggested locator, and validation result.

---

# Allure Reporting

## Step 1: Run tests with Allure results

```bash
pytest --alluredir=test-reports/allure-results
```

## Step 2: Generate HTML report

```bash
allure generate test-reports/allure-results -o test-reports/allure-report --clean
```

## Step 3: Open report

```bash
open test-reports/allure-report/index.html
```

---

# One-command Execution

```bash
./run_tests.sh
```

This will:

* Clean previous Allure results and reports
* Run the test suite
* Execute tests in parallel
* Optionally retry failed tests
* Generate the Allure HTML report

### Test Execution Options

The test runner supports configurable parallel execution and test retries through environment variables.

Default configuration:

* 2 parallel workers
* 0 test retries
* 1 second retry delay

These values can be overridden when running locally:

```bash
WORKERS=4 RERUNS=1 RERUN_DELAY=2 ./run_tests.sh
```

Retries are disabled by default to avoid masking test instability.

---

# Reporting Features

* Page Object Model (POM) architecture
* UI automation with Playwright
* API automation with Requests
* Structured test reporting with Allure
* Screenshot capture on failure
* Locator healing details in Allure reports
* CI/CD-ready structure

---

# Live Test Report

View the latest automated test execution report here:

[View Allure Report](https://jvdmagtanong.github.io/ai-powered-qa-automation-framework/)

---

# CI/CD

Tests run automatically using GitHub Actions on:

* Pushes to `main`
* Pull requests
* Manual workflow execution

The pipeline:

* Executes UI and API tests
* Supports All, Smoke, Regression, UI, and API suites
* Supports configurable parallel workers
* Supports configurable test retries
* Generates Allure reports
* Publishes Allure reports to GitHub Pages
* Publishes test reports even when tests fail

For manual workflow execution, GitHub Actions provides configuration for:

* Test suite
* Number of parallel workers
* Number of test retries

---

# Author

Jose Magtanong
