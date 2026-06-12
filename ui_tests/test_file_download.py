from playwright.sync_api import expect


def test_download_page_lists_downloadable_files(
        file_download_page
):
    file_download_page.navigate()

    expect(
        file_download_page.download_links().first
    ).to_be_visible()

    assert file_download_page.download_links().count() > 0


def test_first_file_can_be_downloaded(
        file_download_page,
        page
):
    file_download_page.navigate()

    with page.expect_download() as download_info:
        file_download_page.first_download_link().click()

    download = download_info.value

    assert download.suggested_filename
