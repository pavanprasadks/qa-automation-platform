from pages.base_page import BasePage


class FileUploadPage(BasePage):

    URL = "https://practice.expandtesting.com/upload"

    PAGE_HEADING = "h1"
    FILE_INPUT = "#fileInput"
    SUBMIT_BUTTON = "#fileSubmit"

    UPLOAD_SUCCESS_HEADING = "h1"
    UPLOADED_FILE_NAME = "div.alert"

    def navigate(self):
        super().navigate(self.URL)

    def page_heading(self):
        return self.get_locator(self.PAGE_HEADING)

    def file_input(self):
        return self.get_locator(self.FILE_INPUT)

    def submit_button(self):
        return self.get_locator(self.SUBMIT_BUTTON)

    def upload_success_heading(self):
        return self.get_locator(
            self.UPLOAD_SUCCESS_HEADING
        )

    def uploaded_file_name(self):
        return self.get_locator(
            self.UPLOADED_FILE_NAME
        )

    def upload_file(self, file_path):
        self.file_input().set_input_files(
            file_path
        )

        self.submit_button().click()