def test_browser_fixture(
    browser_name
):
    print(
        f"\nRunning on: {browser_name}"
    )

    assert browser_name is not None