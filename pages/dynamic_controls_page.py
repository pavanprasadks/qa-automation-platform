from pages.base_page import BasePage


class DynamicControlsPage(BasePage):

    URL = "https://practice.expandtesting.com/dynamic-controls"

    PAGE_HEADING = "h1"

    CHECKBOX = "input[type='checkbox']"

    CHECKBOX_BUTTON = "#checkbox-example button"

    INPUT = "#input-example input"

    INPUT_BUTTON = "#input-example button"

    MESSAGE = "#message"

    def navigate(self):
        super().navigate(self.URL)

    def page_heading(self):
        return self.get_locator(
            self.PAGE_HEADING
        )

    def checkbox(self):
        return self.get_locator(
            self.CHECKBOX
        )

    def checkbox_button(self):
        return self.get_locator(
            self.CHECKBOX_BUTTON
        )

    def input_field(self):
        return self.get_locator(
            self.INPUT
        )

    def input_button(self):
        return self.get_locator(
            self.INPUT_BUTTON
        )

    def message(self):
        return self.get_locator(
            self.MESSAGE
        )

    def click_checkbox_control_button(self):
        self.checkbox_button().click()

    def click_input_control_button(self):
        self.input_button().click()