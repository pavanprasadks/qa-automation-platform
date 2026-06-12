from pages.base_page import BasePage


class DynamicIdPage(BasePage):

    URL = "https://practice.expandtesting.com/dynamic-id"

    PAGE_HEADING = "h1"
    DYNAMIC_BUTTON = "button.btn-primary"

    def navigate(self):
        super().navigate(self.URL)

    def page_heading(self):
        return self.get_locator(self.PAGE_HEADING)

    def dynamic_button(self):
        return self.get_locator(self.DYNAMIC_BUTTON)

    def click_dynamic_button(self):
        self.dynamic_button().click()

    def dynamic_button_id(self):
        return self.dynamic_button().get_attribute("id")
