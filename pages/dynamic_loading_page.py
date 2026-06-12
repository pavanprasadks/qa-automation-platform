from pages.base_page import BasePage


class DynamicLoadingPage(BasePage):

    URL = "https://practice.expandtesting.com/dynamic-loading"

    EXAMPLE_1_URL = (
        "https://practice.expandtesting.com/dynamic-loading/1"
    )

    EXAMPLE_2_URL = (
        "https://practice.expandtesting.com/dynamic-loading/2"
    )

    PAGE_HEADING = "h1"

    EXAMPLE_1_LINK = (
        "a[href='/dynamic-loading/1']"
    )

    EXAMPLE_2_LINK = (
        "a[href='/dynamic-loading/2']"
    )

    START_BUTTON = "#start button"

    FINISH_CONTAINER = "#finish"

    def navigate(self):
        super().navigate(self.URL)

    def navigate_to_example_1(self):
        super().navigate(
            self.EXAMPLE_1_URL
        )

    def navigate_to_example_2(self):
        super().navigate(
            self.EXAMPLE_2_URL
        )

    def page_heading(self):
        return self.get_locator(
            self.PAGE_HEADING
        )

    def example_1_link(self):
        return self.get_locator(
            self.EXAMPLE_1_LINK
        )

    def example_2_link(self):
        return self.get_locator(
            self.EXAMPLE_2_LINK
        )

    def start_button(self):
        return self.get_locator(
            self.START_BUTTON
        )

    def finish_container(self):
        return self.get_locator(
            self.FINISH_CONTAINER
        )

    def start_loading(self):
        self.start_button().click()