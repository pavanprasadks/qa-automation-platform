from pages.base_page import BasePage


class MultipleWindowsPage(BasePage):

    URL = "https://practice.expandtesting.com/windows"

    PAGE_HEADING = "h1"
    NEW_WINDOW_LINK = "a[href='/windows/new']"
    NEW_WINDOW_HEADING = "h1"

    def navigate(self):
        super().navigate(self.URL)

    def page_heading(self):
        return self.get_locator(self.PAGE_HEADING)

    def new_window_link(self):
        return self.get_locator(self.NEW_WINDOW_LINK)
