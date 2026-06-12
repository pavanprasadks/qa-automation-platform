from playwright.sync_api import expect


def test_iframes_are_visible(
        frames_page
):
    frames_page.navigate()

    expect(
        frames_page.youtube_iframe()
    ).to_be_visible()

    expect(
        frames_page.email_iframe()
    ).to_be_visible()


def test_email_subscription_form_inside_iframe(
        frames_page
):
    frames_page.navigate()

    frames_page.subscribe(
        "sdet@example.com"
    )

    expect(
        frames_page.success_message()
    ).to_be_visible()
