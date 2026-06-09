import pytest

from playwright.sync_api import Page, expect

from pages.secure_page import SecurePage

from utils.data_loader import load_login_data


login_test_data = load_login_data()


@pytest.mark.parametrize(
    "test_data",
    login_test_data,
    ids=[data["test_case"] for data in login_test_data]
)
def test_login(
        page: Page,
        login_page,
        test_data
):

    secure_page = SecurePage(page)

    login_page.navigate()

    login_page.login(
        test_data["username"],
        test_data["password"]
    )

    expect(
        login_page.flash_message()
    ).to_contain_text(
        test_data["expected_message"]
    )

    if test_data["expected_result"] == "success":

        expect(page).to_have_url(
            secure_page.SECURE_URL
        )