from pages.base_page import BasePage


class LoginPage(BasePage):

    URL = "https://practice.expandtesting.com/login"

    USERNAME_INPUT = "#username"
    PASSWORD_INPUT = "#password"
    LOGIN_BUTTON = "button[type='submit']"
    FLASH_MESSAGE = "#flash"

    def navigate(self):
        super().navigate(self.URL)

    def enter_username(self, username):
        self.fill(
            self.USERNAME_INPUT,
            username
        )

    def enter_password(self, password):
        self.fill(
            self.PASSWORD_INPUT,
            password
        )

    def click_login(self):
        self.click(
            self.LOGIN_BUTTON
        )

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def flash_message(self):
        return self.get_locator(
            self.FLASH_MESSAGE
        )