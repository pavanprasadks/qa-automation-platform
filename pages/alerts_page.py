from pages.base_page import BasePage


class AlertsPage(BasePage):

    URL = "https://practice.expandtesting.com/js-dialogs"

    PAGE_HEADING = "h1"
    ALERT_BUTTON = "#js-alert"
    CONFIRM_BUTTON = "#js-confirm"
    PROMPT_BUTTON = "#js-prompt"

    def navigate(self):
        super().navigate(self.URL)

    def page_heading(self):
        return self.get_locator(self.PAGE_HEADING)

    def alert_button(self):
        return self.get_locator(self.ALERT_BUTTON)

    def confirm_button(self):
        return self.get_locator(self.CONFIRM_BUTTON)

    def prompt_button(self):
        return self.get_locator(self.PROMPT_BUTTON)

    def result(self):
        return self.page.locator("main p").last

    def click_alert(self):
        self.alert_button().click()

    def click_confirm(self):
        self.confirm_button().click()

    def click_prompt(self):
        self.prompt_button().click()