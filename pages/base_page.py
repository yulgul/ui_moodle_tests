from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait



class BasePage:
    def __init__(self, app):
        self.app = app

    def input_login(self, locator, text: str, wait_time: int = 10) -> WebElement:
        element = self.find_element(locator, wait_time)
        element.send_keys(text)
        return element

    def input_password(self, locator, text: str, wait_time: int = 10) -> WebElement:
        element = self.find_element(locator, wait_time)
        element.send_keys(text)
        return element

    def click(self, locator):
        element = self.find_element(locator)
        element.click()

    def find_element(self, locator, wait_time=10):
        return WebDriverWait(self.app, wait_time).until(
            EC.presence_of_element_located(locator),
            message=f"Can't find element by locator {locator}")

