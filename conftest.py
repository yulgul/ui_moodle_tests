import logging

import allure
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from webdriver_manager.chrome import ChromeDriverManager

from models.auth import AuthData
from pages.app import Application

logger = logging.getLogger("moodle")


@pytest.fixture(scope="session")
def app(request):
    base_url = request.config.getoption("--base-url")
    chrome_options = Options()
    chrome_options.headless = request.config.getoption("--headless")
    fixture = Application(
        webdriver.Chrome(
            ChromeDriverManager().install(), chrome_options=chrome_options
        ),
        base_url,
    )
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
        "--password",
        action="store",
        default="TestQa-1",
        help="enter password",
    ),

    parser.addoption(
        "--headless",
        action="store_true",
        default=False,
        help="launching browser without gui",
    ),


@pytest.fixture
def auth(app, request):
    username = request.config.getoption("--login")
    password = request.config.getoption("--password")
    app.open_auth_page()
    auth_data = AuthData(login=username, password=password)
    app.login.auth(auth_data)
    assert app.login.is_auth(), "You are not auth"


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        try:
            if "app" in item.fixturenames:
                web_driver = item.funcargs["app"]
            else:
                logger.error("Fail to take screen-shot")
                return
            logger.info("Screen-shot done")
            allure.attach(
                web_driver.driver.get_screenshot_as_png(),
                name="screenshot",
                attachment_type=allure.attachment_type.PNG,
            )
        except Exception as e:
            logger.error("Fail to take screen-shot: {}".format(e))
