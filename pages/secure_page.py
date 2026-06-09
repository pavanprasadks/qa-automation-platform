from playwright.sync_api import Page


class SecurePage:

    SECURE_URL = (
        "https://practice.expandtesting.com/secure"
    )

    def __init__(self, page: Page):
        self.page = page