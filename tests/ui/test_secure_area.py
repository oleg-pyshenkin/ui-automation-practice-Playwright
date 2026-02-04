from playwright.sync_api import expect
from pages.secure_page import SecurePage
from pages.login_page import LoginPage

def test_complete_login_flow(page):
    login_page = LoginPage(page)
    secure_page = SecurePage(page)

    login_page.navigate()
    login_page.login("tomsmith", "SuperSecretPassword!")
    expect(page).to_have_url("https://the-internet.herokuapp.com/secure")

    message = secure_page.get_message_text()
    assert "You logged into a secure area" in message