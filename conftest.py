import pytest

from pages.login_page import LoginPage
from pages.dropdown_page import DropdownPage


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


@pytest.fixture
def login_page(page):
    return LoginPage(page)


@pytest.fixture
def dropdown_page(page):
    return DropdownPage(page)
