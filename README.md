## Test Site

UI - https://www.saucedemo.com/
API - https://jsonplaceholder.typicode.com

## Author

Jose Magtanong

# AI-Powered QA Automation Framework

A hybrid UI + API test automation framework built with **Python, Playwright, Pytest, and Allure reporting**.

Designed to demonstrate real-world QA Automation / SDET skills including test design, reusable framework architecture, reporting, CI/CD, and AI-assisted locator recovery.

---

# Tech Stack

* Python 3.x
* Pytest
* Playwright (UI Automation)
* Requests (API Testing)
* Google Gemini API
* BeautifulSoup4
* Allure Reports (Test Reporting)
* Git / GitHub
* GitHub Actions

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
* Test retries for handling transient failures
* CI/CD-ready structure with GitHub Actions

---

# Environment Configuration

The framework uses environment variables for local configuration and API credentials.

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
git clone
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

* Run tests
* Generate the Allure report
* Open the HTML report

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

Tests run automatically using GitHub Actions.

The pipeline:

* Executes UI and API tests
* Supports different test suites
* Supports test retries
* Generates Allure reports
* Publishes the latest report to GitHub Pages
