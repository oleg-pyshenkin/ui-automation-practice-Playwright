from pages.base_page import BasePage

class SecurePage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.flash_message = page.locator("#flash")
    
    def get_message_text(self):
        return self.flash_message.inner_text()
