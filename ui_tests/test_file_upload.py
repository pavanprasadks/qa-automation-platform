from pathlib import Path

from playwright.sync_api import expect


def test_file_can_be_selected_for_upload(
        file_upload_page
):
    sample_file = Path(
        "test_data/upload_sample.txt"
    )

    file_upload_page.navigate()

    file_upload_page.file_input().set_input_files(
        sample_file
    )

    uploaded_file = (
        file_upload_page.file_input()
        .evaluate(
            "input => input.files[0].name"
        )
    )

    assert uploaded_file == (
        "upload_sample.txt"
    )


def test_file_upload_submit_shows_result_message(
        file_upload_page
):
    sample_file = Path(
        "test_data/upload_sample.txt"
    )

    file_upload_page.navigate()

    file_upload_page.upload_file(
        sample_file
    )

    expect(
        file_upload_page.upload_success_heading()
    ).to_have_text(
        "File Uploaded!"
    )

    expect(
        file_upload_page.uploaded_file_name()
    ).to_contain_text(
        "upload_sample.txt"
    )