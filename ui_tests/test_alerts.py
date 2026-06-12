import pytest

from playwright.sync_api import expect

from utils.data_loader import load_alerts_data


confirm_test_data = load_alerts_data()


def test_js_alert_can_be_accepted(
        alerts_page,
        page
):
    messages = []

    page.once(
        "dialog",
        lambda dialog: (
            messages.append(dialog.message),
            dialog.accept()
        )
    )

    alerts_page.navigate()
    alerts_page.click_alert()

    assert messages == ["I am a Js Alert"]

    expect(
        alerts_page.result()
    ).to_have_text("OK")


@pytest.mark.parametrize(
    "test_data",
    confirm_test_data,
    ids=[data["test_case"] for data in confirm_test_data]
)
def test_js_confirm_accept_and_dismiss(
        alerts_page,
        page,
        test_data
):
    page.once(
        "dialog",
        lambda dialog: dialog.accept()
        if test_data["accept"]
        else dialog.dismiss()
    )

    alerts_page.navigate()
    alerts_page.click_confirm()

    expected = "Ok" if test_data["accept"] else "Cancel"

    expect(
        alerts_page.result()
    ).to_have_text(expected)


def test_js_prompt_accepts_text(
        alerts_page,
        page
):
    prompt_text = "Playwright SDET"

    page.once(
        "dialog",
        lambda dialog: dialog.accept(prompt_text)
    )

    alerts_page.navigate()
    alerts_page.click_prompt()

    expect(
        alerts_page.result()
    ).to_have_text(prompt_text)