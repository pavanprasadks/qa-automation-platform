import pytest

from playwright.sync_api import expect

from utils.data_loader import load_hover_data


hover_test_data = load_hover_data()


@pytest.mark.parametrize(
    "test_data",
    hover_test_data,
    ids=[data["test_case"] for data in hover_test_data]
)
def test_user_caption_is_visible_on_hover(
        hover_page,
        test_data
):
    hover_page.navigate()

    expect(
        hover_page.user_caption(test_data["user_number"])
    ).to_be_hidden()

    hover_page.hover_user(
        test_data["user_number"]
    )

    expect(
        hover_page.user_caption(test_data["user_number"])
    ).to_contain_text(
        test_data["expected_name"]
    )

    expect(
        hover_page.user_profile_link(test_data["user_number"])
    ).to_have_attribute(
        "href",
        test_data["expected_href"]
    )
