class BasePage:
    def __init__(self, page):
        self.page = page

    def navigate(self, path: str):
        '''Navigates to a specific URL path.'''
        self.page.goto(f"https://the-internet.herokuapp.com{path}")

    def click(self, locator):
        locator.wait_for(state="visible")
        locator.click()

    def type_text(self, locator, text: str):
        '''Clears the field and then types text.'''
        locator.fill("")
        locator.fill(text)

