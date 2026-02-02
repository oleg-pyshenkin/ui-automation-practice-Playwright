import pytest
import allure
from pages.login_page import LoginPage
from playwright.sync_api import sync_playwright

@pytest.fixture
def login_page(page):
    lp = LoginPage(page)
    lp.navigate()
    return lp


@pytest.fixture(scope="function")
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True) # Set to False if you want to see it
        context = browser.new_context()
        page = context.new_page()
        yield page
        browser.close()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == 'call' and report.failed:
        page = item.funcargs.get('page')
        if page:
            screenshot = page.screenshot(full_page=True)
            allure.attach(screenshot, name="screenshot", attachment_type=allure.attachment_type.PNG)