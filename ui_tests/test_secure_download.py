from playwright.sync_api import expect


def test_secure_download_requires_authorization(
        secure_download_page
):
    response = secure_download_page.navigate()

    assert response.status == 401

    expect(
        secure_download_page.page_body()
    ).to_contain_text(
        "Not authorized"
    )
