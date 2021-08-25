from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators


class LoginPage(BasePage):

    def auth(self, login: str, password: str):
        self.input_login(LoginPageLocators.LOGIN, login)
        self.input_password(LoginPageLocators.PASSWORD, password)
        self.click(LoginPageLocators.BUTTON_SUBMIT)