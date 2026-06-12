from playwright.sync_api import expect


def test_checkbox_1_default_state(
        checkbox_page
):
    checkbox_page.navigate()

    expect(
        checkbox_page.checkbox_1()
    ).not_to_be_checked()


def test_checkbox_2_default_state(
        checkbox_page
):
    checkbox_page.navigate()

    expect(
        checkbox_page.checkbox_2()
    ).to_be_checked()


def test_checkbox_1_can_be_checked(
        checkbox_page
):
    checkbox_page.navigate()

    checkbox_page.checkbox_1().check()

    expect(
        checkbox_page.checkbox_1()
    ).to_be_checked()


def test_checkbox_2_can_be_unchecked(
        checkbox_page
):
    checkbox_page.navigate()

    checkbox_page.checkbox_2().uncheck()

    expect(
        checkbox_page.checkbox_2()
    ).not_to_be_checked()


def test_checkbox_1_remains_checked_after_action(
        checkbox_page
):
    checkbox_page.navigate()

    checkbox_page.checkbox_1().check()

    expect(
        checkbox_page.checkbox_1()
    ).to_be_checked()

    expect(
        checkbox_page.checkbox_1()
    ).to_be_checked()


def test_checkbox_2_remains_unchecked_after_action(
        checkbox_page
):
    checkbox_page.navigate()

    checkbox_page.checkbox_2().uncheck()

    expect(
        checkbox_page.checkbox_2()
    ).not_to_be_checked()

    expect(
        checkbox_page.checkbox_2()
    ).not_to_be_checked()