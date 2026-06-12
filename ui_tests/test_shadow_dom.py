from playwright.sync_api import expect


def test_shadow_dom_page_loads_shadow_host(
        shadow_dom_page
):
    shadow_dom_page.navigate()

    expect(
        shadow_dom_page.page_heading()
    ).to_have_text(
        "Shadow DOM page for Automation Testing Practice"
    )

    expect(
        shadow_dom_page.shadow_host()
    ).to_be_visible()


def test_shadow_dom_button_is_accessible(
        shadow_dom_page
):
    shadow_dom_page.navigate()

    expect(
        shadow_dom_page.shadow_button()
    ).to_be_visible()

    shadow_dom_page.shadow_button().click()
