from playwright.sync_api import Page


def test_login_page_loads(page: Page):
    page.goto("https://practice.expandtesting.com/login")

    assert page.title() == "Test Login Page for Automation Testing Practice"