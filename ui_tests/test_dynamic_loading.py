from playwright.sync_api import expect


def test_dynamic_loading_landing_page_links_are_visible(
        dynamic_loading_page
):
    dynamic_loading_page.navigate()

    expect(
        dynamic_loading_page.page_heading()
    ).to_have_text(
        "Dynamically Loaded Page Elements"
    )

    expect(
        dynamic_loading_page.example_1_link()
    ).to_be_visible()

    expect(
        dynamic_loading_page.example_2_link()
    ).to_be_visible()


def test_hidden_element_becomes_visible_after_loading(
        dynamic_loading_page
):
    dynamic_loading_page.navigate_to_example_1()

    dynamic_loading_page.start_button().click()

    expect(
        dynamic_loading_page.page.locator(
            "body"
        )
    ).to_contain_text(
        "Hello World!"
    )