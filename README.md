## Test Site
https://www.saucedemo.com/

## Author
Jose Magtanong

# 🧪 AI-Powered QA Automation Framework

A hybrid UI + API test automation framework built with **Python, Playwright, Pytest, and Allure reporting**.  
Designed to demonstrate real-world QA Automation / SDET skills including test design, reporting, and CI/CD readiness.

---

# 🚀 Tech Stack

- Python 3.x
- Pytest
- Playwright (UI Automation)
- Requests (API Testing)
- Allure Reports (Test Reporting)
- Git / GitHub

---

## Features
- UI automation for e-commerce demo app
- Login and cart workflow tests
- Reusable Page Object Model design
- Pytest fixtures for browser management
- HTML test reporting

# ⚙️ Setup Instructions

## 1. Clone repo
git clone <your-repo-url>
cd ai-powered-qa-automation-framework

## 2. Create virtual environment
python3 -m venv venv
source venv/bin/activate

## 3. Install dependencies
pip install -r requirements.txt

## 4. Install Playwright browsers
playwright install

## 🧪 Running Tests
## Run all tests
pytest

## Run UI tests
pytest tests/ui

## Run API tests
pytest tests/api

## 📊 Allure Reporting (Professional Setup)
## Step 1: Run tests with Allure results
pytest --alluredir=test-reports/allure-results

## Step 2: Generate HTML report
allure generate test-reports/allure-results -o test-reports/allure-report --clean

## Step 3: Open report
open test-reports/allure-report/index.html

## 🚀 One-command execution
./run_tests.sh 

# This will:
- run tests
- generate Allure report
- open HTML report

## 📸 Features
- Page Object Model (POM) architecture
- UI automation with Playwright
- API automation with Requests
- Structured test reporting with Allure
- Screenshot capture on failure (UI tests)
- CI/CD-ready structure (GitHub Actions compatible)

