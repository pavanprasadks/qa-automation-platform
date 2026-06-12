from pages.base_page import BasePage


class SecureDownloadPage(BasePage):

    URL = "https://practice.expandtesting.com/download-secure"

    PAGE_BODY = "body"

    def navigate(self):
        return self.page.goto(self.URL)

    def page_body(self):
        return self.get_locator(self.PAGE_BODY)
