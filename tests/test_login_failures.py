import pytest
from playwright.sync_api import expect
from pages.login_page import LoginPage

@pytest.mark.parametrize("user, pw, expected", [
    ("invalid_user", "SuperSecretPassword!", "Your username is invalid!"),
    ("tomsmith", "wrong_password", "Your password is invalid!"),
    ("", "", "Your username is invalid!")
    ])

def test_login_failure_scenarios(page, user, pw, expected):
    login_page = LoginPage(page)

    login_page.navigate()
    login_page.login(user, pw)
    expect(login_page.error_message).to_contain_text(expected)