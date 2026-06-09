from playwright.sync_api import expect

def test_tc001_verify_dropdown_default_value(
        dropdown_page
):
    dropdown_page.navigate()

    expect(
        dropdown_page.simple_dropdown()
    ).to_have_value(
        ""
    )

    expect(
        dropdown_page.selected_simple_dropdown_option()
    ).to_have_text(
        "Please select an option"
    )


def test_tc002_select_option_1_and_verify_selected_value(
        dropdown_page
):
    dropdown_page.navigate()

    dropdown_page.select_simple_option(
        "1"
    )

    expect(
        dropdown_page.simple_dropdown()
    ).to_have_value(
        "1"
    )


def test_tc003_select_option_2_and_verify_selected_value(
        dropdown_page
):
    dropdown_page.navigate()

    dropdown_page.select_simple_option(
        "2"
    )

    expect(
        dropdown_page.simple_dropdown()
    ).to_have_value(
        "2"
    )


def test_tc004_verify_selected_option_text(
        dropdown_page
):
    dropdown_page.navigate()

    dropdown_page.select_simple_option(
        "1"
    )

    expect(
        dropdown_page.selected_simple_dropdown_option()
    ).to_have_text(
        "Option 1"
    )


def test_tc005_verify_dropdown_contains_expected_options(
        dropdown_page
):
    dropdown_page.navigate()

    expect(
        dropdown_page.simple_dropdown_options()
    ).to_have_text(
        [
            "Please select an option",
            "Option 1",
            "Option 2"
        ]
    )

    expect(
        dropdown_page.simple_dropdown_option_by_value("")
    ).to_have_text(
        "Please select an option"
    )

    expect(
        dropdown_page.simple_dropdown_option_by_value("1")
    ).to_have_text(
        "Option 1"
    )

    expect(
        dropdown_page.simple_dropdown_option_by_value("2")
    ).to_have_text(
        "Option 2"
    )
