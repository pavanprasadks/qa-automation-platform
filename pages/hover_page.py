from pages.base_page import BasePage


class HoverPage(BasePage):

    URL = "https://practice.expandtesting.com/hovers"

    PAGE_HEADING = "h1"
    USER_CARD = "[data-testid='user-{user_number}']"
    USER_CAPTION = "[data-testid='user-{user_number}'] .figcaption"
    USER_PROFILE_LINK = "[data-testid='user-{user_number}'] .figcaption a"

    def navigate(self):
        super().navigate(self.URL)

    def page_heading(self):
        return self.get_locator(self.PAGE_HEADING)

    def user_card(self, user_number):
        return self.get_locator(
            self.USER_CARD.format(user_number=user_number)
        )

    def user_caption(self, user_number):
        return self.get_locator(
            self.USER_CAPTION.format(user_number=user_number)
        )

    def user_profile_link(self, user_number):
        return self.get_locator(
            self.USER_PROFILE_LINK.format(user_number=user_number)
        )

    def hover_user(self, user_number):
        self.user_card(user_number).hover()
