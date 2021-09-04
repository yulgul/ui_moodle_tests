import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from webdriver_manager.chrome import ChromeDriverManager

from pages.app import Application


@pytest.fixture(scope="session")
def app(request):
    base_url = request.config.getoption("--base-url")
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    fixture = Application(webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options), base_url)
    yield fixture
    fixture.quit()


def pytest_addoption(parser):
    parser.addoption(
        "--base-url",
        action="store",
        default="https://qacoursemoodle.innopolis.university",
        help="enter base_url",
    ),
    parser.addoption(
        "--login",
        action="store",
        default="admi-test",
        help="enter userlogin",
    ),
    parser.addoption(
        "--password", action="store", default="TestQa-1", help="enter password",
    ),
