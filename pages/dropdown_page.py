from pages.base_page import BasePage


class DropdownPage(BasePage):

    URL = "https://practice.expandtesting.com/dropdown"

    PAGE_HEADING = "h1"
    SIMPLE_DROPDOWN = "#dropdown"
    SIMPLE_DROPDOWN_OPTIONS = "#dropdown option"
    SELECTED_SIMPLE_DROPDOWN_OPTION = "#dropdown option:checked"
    SIMPLE_DROPDOWN_OPTION_BY_VALUE = "#dropdown option[value='{value}']"

    def navigate(self):
        super().navigate(self.URL)

    def page_heading(self):
        return self.get_locator(self.PAGE_HEADING)

    def simple_dropdown(self):
        return self.get_locator(self.SIMPLE_DROPDOWN)

    def simple_dropdown_options(self):
        return self.get_locator(self.SIMPLE_DROPDOWN_OPTIONS)

    def selected_simple_dropdown_option(self):
        return self.get_locator(self.SELECTED_SIMPLE_DROPDOWN_OPTION)

    def simple_dropdown_option_by_value(self, option_value):
        return self.get_locator(
            self.SIMPLE_DROPDOWN_OPTION_BY_VALUE.format(
                value=option_value
            )
        )

    def select_simple_option(self, option_value):
        self.simple_dropdown().select_option(option_value)
