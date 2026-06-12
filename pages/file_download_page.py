from pages.base_page import BasePage


class FileDownloadPage(BasePage):

    URL = "https://practice.expandtesting.com/download"

    PAGE_HEADING = "h1"
    DOWNLOAD_LINKS = "a[download]"

    def navigate(self):
        super().navigate(self.URL)

    def page_heading(self):
        return self.get_locator(self.PAGE_HEADING)

    def download_links(self):
        return self.get_locator(self.DOWNLOAD_LINKS)

    def first_download_link(self):
        return self.download_links().first
