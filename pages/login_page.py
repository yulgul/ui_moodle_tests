import logging

from models.auth import AuthData
from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators
from selenium.webdriver.remote.webelement import WebElement

logger = logging.getLogger("moodle")


class LoginPage(BasePage):
    def is_auth(self):
        self.find_element(LoginPageLocators.FORM)
        element = self.find_elements(LoginPageLocators.USER_BUTTON)
        if len(element) > 0:
            return True
        return False

    def is_exit_confirm_button(self):
        element = self.find_elements(LoginPageLocators.EXIT_CONFIRM)
        if len(element) > 0:
            return True
        return False

    def login_input(self) -> WebElement:
        return self.find_element(LoginPageLocators.LOGIN)

    def password_input(self) -> WebElement:
        return self.find_element(LoginPageLocators.PASSWORD)

    def submit_button(self) -> WebElement:
        return self.find_element(LoginPageLocators.BUTTON_SUBMIT)

    def user_menu(self) -> WebElement:
        return self.find_element(LoginPageLocators.USER_MENU)

    def exit(self) -> WebElement:
        return self.find_element(LoginPageLocators.EXIT)

    def exit_confirm(self) -> WebElement:
        return self.find_element(LoginPageLocators.EXIT_CONFIRM)

    def auth(self, data: AuthData):
        logger.info(f"User email is {data.login}")
        logger.info(f"User password is {data.password}")
        if self.is_auth():
            self.click(self.user_menu())
            self.click(self.exit())
        if self.is_exit_confirm_button():
            self.click(self.exit_confirm())
        self.input(self.login_input(), data.login)
        self.input(self.password_input(), data.password)
        self.click(self.submit_button())

    def auth_error(self) -> str:
        return self.find_element(LoginPageLocators.LOGIN_ERROR).text

    def sign_out(self):
        if self.is_auth():
            self.click(self.user_menu())
            self.click(self.exit())
        if self.exit_confirm():
            self.click(self.exit_confirm())
