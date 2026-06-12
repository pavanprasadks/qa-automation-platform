from pages.base_page import BasePage


class TablesPage(BasePage):

    URL = "https://practice.expandtesting.com/tables"

    PAGE_HEADING = "h1"
    TABLE_1 = "#table1"
    TABLE_2 = "#table2"
    TABLE_1_HEADERS = "#table1 thead th"
    TABLE_1_ROWS = "#table1 tbody tr"
    TABLE_1_FIRST_ROW_CELLS = "#table1 tbody tr:first-child td"
    TABLE_1_EMAIL_LINKS = "#table1 tbody tr td:nth-child(3)"
    TABLE_1_DUE_CELLS = "#table1 tbody tr td:nth-child(4)"

    def navigate(self):
        super().navigate(self.URL)

    def page_heading(self):
        return self.get_locator(self.PAGE_HEADING)

    def table_1(self):
        return self.get_locator(self.TABLE_1)

    def table_2(self):
        return self.get_locator(self.TABLE_2)

    def table_1_headers(self):
        return self.get_locator(self.TABLE_1_HEADERS)

    def table_1_rows(self):
        return self.get_locator(self.TABLE_1_ROWS)

    def table_1_first_row_cells(self):
        return self.get_locator(self.TABLE_1_FIRST_ROW_CELLS)

    def table_1_email_cells(self):
        return self.get_locator(self.TABLE_1_EMAIL_LINKS)

    def table_1_due_cells(self):
        return self.get_locator(self.TABLE_1_DUE_CELLS)
