from pages.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

        self.username_input = page.locator("#username")
        self.password_input = page.locator("#password")
        self.login_button = page.locator("button[type='submit']")
        self.logout_button = page.get_by_role("link", name="Logout")
        self.success_message = page.locator("#flash")
        self.error_message = page.locator("#flash")
        

    def navigate(self):
        super().navigate("/login")

    def login(self, username, password):
        self.type_text(self.username_input, username)
        self.type_text(self.password_input, password)
        self.click(self.login_button)

    def logout(self):
        self.click(self.logout_button)
