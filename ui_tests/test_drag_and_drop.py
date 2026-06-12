from playwright.sync_api import expect


def test_columns_have_default_order(
        drag_and_drop_page
):
    drag_and_drop_page.navigate()

    expect(
        drag_and_drop_page.column_a()
    ).to_have_text(
        "A"
    )

    expect(
        drag_and_drop_page.column_b()
    ).to_have_text(
        "B"
    )


def test_column_a_can_be_dragged_to_column_b(
        drag_and_drop_page
):
    drag_and_drop_page.navigate()

    drag_and_drop_page.drag_column_a_to_column_b()

    expect(
        drag_and_drop_page.column_a()
    ).to_have_text(
        "B"
    )

    expect(
        drag_and_drop_page.column_b()
    ).to_have_text(
        "A"
    )
