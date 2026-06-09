import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--browser-name",
        action="store",
        default="chromium",
        help="Browser to run tests on"
    )


@pytest.fixture(scope="session")
def browser_name(request):
    return request.config.getoption(
        "--browser-name"
    )