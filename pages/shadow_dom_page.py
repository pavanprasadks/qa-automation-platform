from pages.base_page import BasePage


class ShadowDomPage(BasePage):

    URL = "https://practice.expandtesting.com/shadowdom"

    PAGE_HEADING = "h1"
    LIGHT_DOM_BUTTON = "body > button#my-btn"
    SHADOW_HOST = "#shadow-host"
    SHADOW_BUTTON = "#shadow-host #my-btn"

    def navigate(self):
        super().navigate(self.URL)

    def page_heading(self):
        return self.get_locator(self.PAGE_HEADING)

    def light_dom_button(self):
        return self.get_locator(self.LIGHT_DOM_BUTTON)

    def shadow_host(self):
        return self.get_locator(self.SHADOW_HOST)

    def shadow_button(self):
        return self.get_locator(self.SHADOW_BUTTON)
