from playwright.sync_api import expect


def test_sortable_tables_are_visible(
        tables_page
):
    tables_page.navigate()

    expect(
        tables_page.table_1()
    ).to_be_visible()

    expect(
        tables_page.table_2()
    ).to_be_visible()


def test_table_headers_match_expected_columns(
        tables_page
):
    tables_page.navigate()

    expect(
        tables_page.table_1_headers()
    ).to_have_text(
        [
            "Last Name",
            "First Name",
            "Email",
            "Due",
            "Web Site",
            "Action"
        ]
    )


def test_table_contains_expected_first_row_data(
        tables_page
):
    tables_page.navigate()

    row = tables_page.table_1_first_row_cells()

    expect(row.nth(0)).to_have_text("Smith")
    expect(row.nth(1)).to_have_text("John")
    expect(row.nth(2)).to_have_text("jsmith@gmail.com")
    expect(row.nth(3)).to_have_text("$50.00")
    expect(row.nth(4)).to_have_text("http://www.jsmith.com")

    actions = row.nth(5).inner_text()

    assert "Edit" in actions
    assert "Delete" in actions