# Playwright UI Automation Practice

A professional-grade test automation framework built with **Python** and **Playwright**, following the **Page Object Model (POM)** design pattern.

## Tech Stack
* **Language:** Python 3.13+
* **Framework:** Pytest
* **Tool:** Playwright
* **Pattern:** Page Object Model (POM)

## Key Features
* **Scalable Architecture:** Implemented Page Object Model to separate page logic from test scripts.
* **Shared Context:** Utilized `conftest.py` and Pytest fixtures for efficient setup/teardown.
* **Robust Assertions:** Leveraged Playwright's `expect` library with auto-waiting and fuzzy matching (`ignore_case=True`) to reduce test flakiness.
* **Negative Testing:** Includes verification for failed login scenarios and error message validation.

## Project Structure
- `pages/`: Contains Page Object classes (logic and locators).
- `tests/`: Contains test scripts organized by feature.
- `requirements.txt`: List of project dependencies.
- `.gitignore`: Files and folders to be excluded from Git.

## Installation
1. Clone the repo: `git clone <your-repo-link>`
2. Create venv: `python3 -m venv venv`
3. Activate venv: `source venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Install Playwright browsers: `playwright install`

## Running Tests
Run all tests in headless mode:
```bash
pytest