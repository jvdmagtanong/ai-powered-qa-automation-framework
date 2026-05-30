# AI-Powered QA Automation Framework

This project is a QA automation framework built using Python and Playwright, demonstrating UI automation, test structuring, and scalable test design.

## Test Site
https://www.saucedemo.com/

## Author
Jose Magtanong

## Tech Stack
- Python
- Playwright
- Pytest
- Page Object Model (POM)
- Pytest Fixtures
- HTML Reporting

## Features
- UI automation for e-commerce demo app
- Login and cart workflow tests
- Reusable Page Object Model design
- Pytest fixtures for browser management
- HTML test reporting

## How to Run

```bash
pip install -r requirements.txt
playwright install
pytest -s --html=report.html --self-contained-html