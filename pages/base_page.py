from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, app):
        self.app = app

    def input(self, element, text: str):
        element.clear()
        if text:
            element.send_keys(text)
            return element

    def find_elements(self, locator):
        return self.app.driver.find_elements(*locator)

    def click(self, element):
        element.click()

    def find_element(self, locator, wait_time=10):
        element = WebDriverWait(self.app.driver, wait_time).until(
            EC.presence_of_element_located(locator),
            message=f"Can't find element by locator {locator}",
        )
        return element

    def find_select_element(self, locator):
        select_element = Select(self.find_element(locator))
        return select_element

    def select_value(self, select_element, value):
        select_element.select_by_value(value)

    def find_clickable_element(self, locator, wait_time=10):
        element = WebDriverWait(self.app.driver, wait_time).until(
            EC.element_to_be_clickable(locator),
            message=f"Element not clickable {locator}",
        )
        return element

    def input_file(self, element, image):
        element.send_keys(image)
