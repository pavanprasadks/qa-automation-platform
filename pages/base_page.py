from playwright.sync_api import Page


class BasePage:

    def __init__(self, page: Page):
        self.page = page

    def navigate(self, url):
        self.page.goto(url)

    def fill(self, locator, value):
        self.page.locator(locator).fill(value)

    def click(self, locator):
        self.page.locator(locator).click()

    def get_locator(self, locator):
        return self.page.locator(locator)

    def get_text(self, locator):
        return self.page.locator(locator).text_content()

