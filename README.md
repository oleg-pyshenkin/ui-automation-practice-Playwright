![UI and API Tests](https://github.com/oleg-pyshenkin/ui-automation-practice-Playwright/actions/workflows/python-tests.yml/badge.svg)

# Hybrid (UI & API) Automation Framework

A professional-grade test automation framework built with **Python**, **Playwright**, and **Requests**, following the **Page Object Model (POM)** design pattern.

## Tech Stack
* **Language:** Python 3.13+
* **Framework:** Pytest
* **UI Tool:** Playwright
* **API Tool:** Requests
* **Reporting:** Allure Report
* **Pattern:** Page Object Model (POM)

## Key Features
* **Hybrid Testing:** Combines fast API validation for backend logic with Playwright for end-to-end UI flows.
* **Page Object Model:** Separates page logic from test scripts for high maintainability.
* **Advanced Reporting:** Integrated **Allure Report** with automatic **screenshots on failure** to simplify debugging.
* **Robust Assertions:** Leveraged Playwright's `expect` library with auto-waiting and API response content validation.

## Project Structure
- `pages/`: Page Object classes (logic and locators).
- `tests/ui/`: UI-specific test scripts.
- `tests/api/`: Backend API test scripts.
- `conftest.py`: Global fixtures and Allure hooks (screenshot capture).
- `requirements.txt`: Project dependencies.

## Installation
1. Clone the repo: `git clone <your-repo-link>`
2. Create & activate venv: `python3 -m venv venv && source venv/bin/activate`
3. Install dependencies: `pip install -r requirements.txt`
4. Install Playwright browsers: `playwright install`

## Running Tests & Reporting
Run all tests and generate results:
```bash
python3 -m pytest --alluredir=allure-results