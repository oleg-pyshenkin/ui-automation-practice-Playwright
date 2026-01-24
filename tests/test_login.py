from playwright.sync_api import expect
from pages.login_page import LoginPage


def test_successful_login(login_page):
    login_page.login("tomsmith", "SuperSecretPassword!")
    expect(login_page.page).to_have_url("https://the-internet.herokuapp.com/secure")

def test_logout(login_page):
    login_page.login("tomsmith", "SuperSecretPassword!")
    login_page.logout()
    expect(login_page.login_button).to_be_visible()

def test_failed_login(login_page):
    login_page.login("wrong_user", "wrong_password")
    expect(login_page.success_message).to_contain_text("invalid", ignore_case=True)