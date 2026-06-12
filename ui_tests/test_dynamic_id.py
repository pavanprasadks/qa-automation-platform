from playwright.sync_api import expect


def test_dynamic_id_button_is_located_without_using_dynamic_id(
        dynamic_id_page
):
    dynamic_id_page.navigate()

    expect(
        dynamic_id_page.dynamic_button()
    ).to_be_visible()

    dynamic_id_page.click_dynamic_button()


def test_dynamic_id_changes_after_reload(
        dynamic_id_page
):
    dynamic_id_page.navigate()

    first_id = dynamic_id_page.dynamic_button_id()

    dynamic_id_page.navigate()

    second_id = dynamic_id_page.dynamic_button_id()

    assert first_id != second_id
