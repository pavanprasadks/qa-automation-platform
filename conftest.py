import pytest

from pages.login_page import LoginPage
from pages.checkbox_page import CheckboxPage
from pages.dropdown_page import DropdownPage
from pages.dynamic_loading_page import DynamicLoadingPage
from pages.dynamic_controls_page import DynamicControlsPage
from pages.dynamic_id_page import DynamicIdPage
from pages.alerts_page import AlertsPage
from pages.frames_page import FramesPage
from pages.file_upload_page import FileUploadPage
from pages.file_download_page import FileDownloadPage
from pages.tables_page import TablesPage
from pages.hover_page import HoverPage
from pages.drag_and_drop_page import DragAndDropPage
from pages.multiple_windows_page import MultipleWindowsPage
from pages.secure_download_page import SecureDownloadPage
from pages.shadow_dom_page import ShadowDomPage
from pages.base_page import BasePage


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
def base_page(page):
    return BasePage(page)


@pytest.fixture
def login_page(page):
    return LoginPage(page)


@pytest.fixture
def checkbox_page(page):
    return CheckboxPage(page)


@pytest.fixture
def dropdown_page(page):
    return DropdownPage(page)


@pytest.fixture
def dynamic_loading_page(page):
    return DynamicLoadingPage(page)


@pytest.fixture
def dynamic_controls_page(page):
    return DynamicControlsPage(page)


@pytest.fixture
def dynamic_id_page(page):
    return DynamicIdPage(page)


@pytest.fixture
def alerts_page(page):
    return AlertsPage(page)


@pytest.fixture
def frames_page(page):
    return FramesPage(page)


@pytest.fixture
def file_upload_page(page):
    return FileUploadPage(page)


@pytest.fixture
def file_download_page(page):
    return FileDownloadPage(page)


@pytest.fixture
def tables_page(page):
    return TablesPage(page)


@pytest.fixture
def hover_page(page):
    return HoverPage(page)


@pytest.fixture
def drag_and_drop_page(page):
    return DragAndDropPage(page)


@pytest.fixture
def multiple_windows_page(page):
    return MultipleWindowsPage(page)

@pytest.fixture
def secure_download_page(page):
    return SecureDownloadPage(page)


@pytest.fixture
def shadow_dom_page(page):
    return ShadowDomPage(page)
@pytest.fixture
def context(browser, browser_name):
    context = browser.new_context()
    yield context
    context.close()


@pytest.fixture
def page(context):
    page = context.new_page()
    yield page
    page.close()
