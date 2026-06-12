from pages.base_page import BasePage


class FramesPage(BasePage):

    URL = "https://practice.expandtesting.com/iframe"

    PAGE_HEADING = "h1"
    YOUTUBE_IFRAME = "#iframe-youtube"
    EMAIL_IFRAME = "#email-subscribe"
    EMAIL_INPUT = "#email"
    SUBSCRIBE_BUTTON = "#btn-subscribe"
    SUCCESS_MESSAGE = "#success-message"

    def navigate(self):
        super().navigate(self.URL)

    def page_heading(self):
        return self.get_locator(self.PAGE_HEADING)

    def youtube_iframe(self):
        return self.get_locator(self.YOUTUBE_IFRAME)

    def email_iframe(self):
        return self.get_locator(self.EMAIL_IFRAME)

    def email_frame(self):
        return self.page.frame_locator(self.EMAIL_IFRAME)

    def email_input(self):
        return self.email_frame().locator(self.EMAIL_INPUT)

    def subscribe_button(self):
        return self.email_frame().locator(self.SUBSCRIBE_BUTTON)

    def success_message(self):
        return self.email_frame().locator(self.SUCCESS_MESSAGE)

    def subscribe(self, email):
        self.email_input().fill(email)
        self.subscribe_button().click()
