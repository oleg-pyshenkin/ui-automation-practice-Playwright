class LoginPage:
    def __init__(self, page):
        self.page = page

        self.username_input = page.locator("#username")
        self.password_input = page.locator("#password")
        self.login_button = page.locator("button[type='submit']")
        self.logout_button = page.get_by_role("link", name="Logout")
        self.success_message = page.locator("#flash")

    def navigate(self):
        self.page.goto("https://the-internet.herokuapp.com/login")

    def login(self, user, pwd):
        self.username_input.fill(user)
        self.password_input.fill(pwd)
        self.login_button.click()

    def logout(self):
        self.logout_button.click()
