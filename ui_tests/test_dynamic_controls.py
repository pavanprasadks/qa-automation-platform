from playwright.sync_api import expect


def test_checkbox_control_can_remove_and_add_checkbox(
        dynamic_controls_page
):
    dynamic_controls_page.navigate()

    expect(
        dynamic_controls_page.checkbox()
    ).to_be_visible()

    dynamic_controls_page.click_checkbox_control_button()

    expect(
        dynamic_controls_page.message()
    ).to_have_text(
        "It's gone!"
    )

    dynamic_controls_page.click_checkbox_control_button()

    expect(
        dynamic_controls_page.checkbox()
    ).to_be_visible()

    expect(
        dynamic_controls_page.message()
    ).to_have_text(
        "It's back!"
    )


def test_input_control_can_enable_and_disable_input(
        dynamic_controls_page
):
    dynamic_controls_page.navigate()

    expect(
        dynamic_controls_page.input_field()
    ).to_be_disabled()

    dynamic_controls_page.click_input_control_button()

    expect(
        dynamic_controls_page.input_field()
    ).to_be_enabled()

    expect(
        dynamic_controls_page.message()
    ).to_have_text(
        "It's enabled!"
    )

    dynamic_controls_page.click_input_control_button()

    expect(
        dynamic_controls_page.input_field()
    ).to_be_disabled()

    expect(
        dynamic_controls_page.message()
    ).to_have_text(
        "It's disabled!"
    )