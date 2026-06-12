from pages.base_page import BasePage


class CheckboxPage(BasePage):

    URL = "https://practice.expandtesting.com/checkboxes"

    CHECKBOX_1 = "#checkbox1"
    CHECKBOX_2 = "#checkbox2"

    def navigate(self):
        super().navigate(self.URL)

    def checkbox_1(self):
        return self.get_locator(self.CHECKBOX_1)

    def checkbox_2(self):
        return self.get_locator(self.CHECKBOX_2)
