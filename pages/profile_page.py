from locators.user_page_locators import UserPageLocators
from models.auth import AuthData
from models.user_data import UserData
from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators
from selenium.webdriver.remote.webelement import WebElement

class ProfilePage(BasePage):

    def login_input(self) -> WebElement:
        return self.find_element(LoginPageLocators.LOGIN)

    def password_input(self) -> WebElement:
        return self.find_element(LoginPageLocators.PASSWORD)

    def submit_button(self) -> WebElement:
        return self.find_element(LoginPageLocators.BUTTON_SUBMIT)

    def submit_user_profile(self):
        return self.find_element(UserPageLocators.USER_BUTTON)

    def submit_setting_button(self):
        """кнопка Настройки."""
        return self.find_element(UserPageLocators.SETTING_BUTTON)

    def submit_edit_button(self):
        """кнопка Редактировать информацию."""
        return self.find_element(UserPageLocators.EDIT_LINK)

    def input_name(self):
        return self.find_element(UserPageLocators.INPUT_FIRST_NAME)

    def input_email(self):
        return self.find_element(UserPageLocators.INPUT_EMAIL)

    def input_city(self):
        return self.find_element(UserPageLocators.INPUT_CITY)

    def submit_save_button(self):
        return self.find_element(UserPageLocators.SAVE_BUTTON)



    def auto_login(self, data: AuthData):
        self.input(self.login_input(), data.login)
        self.input(self.password_input(), data.password)
        self.click(self.submit_button())

    def edit_user(self):
        self.click(self.submit_user_profile())
        self.click(self.submit_setting_button())
        self.click(self.submit_edit_button())

    def input_data(self, data: UserData):
        self.input(self.input_name(), data.name)
        self.input(self.input_email(), data.email)
        self.input(self.input_city(), data.city)

    def save_changes(self):
        self.click(self.submit_save_button())

    def save_message(self):
        return self.find_element(UserPageLocators.SAVE_MESSAGE).text






