from playwright.sync_api import expect


def test_new_window_link_opens_child_page(
        multiple_windows_page,
        page
):
    multiple_windows_page.navigate()

    with page.expect_popup() as popup_info:
        multiple_windows_page.new_window_link().click()

    child_page = popup_info.value

    expect(
        child_page.locator(multiple_windows_page.NEW_WINDOW_HEADING)
    ).to_have_text(
        "Example of a new window page for Automation Testing Practice"
    )

    expect(
        child_page
    ).to_have_url(
        "https://practice.expandtesting.com/windows/new"
    )
