from pages.base_page import BasePage


class DragAndDropPage(BasePage):

    URL = "https://practice.expandtesting.com/drag-and-drop"

    PAGE_HEADING = "h1"
    COLUMN_A = "#column-a"
    COLUMN_B = "#column-b"

    def navigate(self):
        super().navigate(self.URL)

    def page_heading(self):
        return self.get_locator(self.PAGE_HEADING)

    def column_a(self):
        return self.get_locator(self.COLUMN_A)

    def column_b(self):
        return self.get_locator(self.COLUMN_B)

    def drag_column_a_to_column_b(self):
        self.column_a().drag_to(self.column_b())
