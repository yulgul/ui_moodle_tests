import logging

from locators.user_page_locators import UserPageLocators, AddImageLocators, MoreInfoLocators, InterestsLocators, \
    OptionalLocators
from models.auth import AuthData
from models.user_data import UserData, UserImage
from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators
from selenium.webdriver.remote.webelement import WebElement

logger = logging.getLogger("moodle")

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
        return self.find_element(UserPageLocators.SETTING_BUTTON)

    def submit_edit_button(self):
        return self.find_element(UserPageLocators.EDIT_LINK)

    def click_expand_all(self):
        expand_all = self.find_element(UserPageLocators.CLICK_EXPAND_ALL)
        return self.click(expand_all)

    def input_first_name(self):
        return self.find_element(UserPageLocators.INPUT_FIRST_NAME)

    def input_last_name(self):
        return self.find_element(UserPageLocators.INPUT_LAST_NAME)

    def input_email(self):
        return self.find_element(UserPageLocators.INPUT_EMAIL)

    def email_display_select(self) -> WebElement:
        email_display = self.find_select_element(UserPageLocators.EMAIL_DISPLAY)
        return email_display

    def select_email_display(self, value):
        self.select_value(self.email_display_select(), value)

    def input_moodlenet(self):
        return self.find_element(UserPageLocators.INPUT_MOODLENET)

    def input_city(self):
        return self.find_element(UserPageLocators.INPUT_CITY)

    def time_zone_select(self) -> WebElement:
        time_zone = self.find_select_element(UserPageLocators.TIME_ZONE)
        return time_zone

    def select_time_zone(self, value):
        self.select_value(self.time_zone_select(), value)

    def add_image(self):
        return self.find_clickable_element(AddImageLocators.ADD)

    def upload_file(self):
        return self.find_clickable_element(AddImageLocators.INPUT_FILE)

    def description_image(self):
        return self.find_clickable_element(AddImageLocators.INPUT_DESCRIPTION)

    def button_upload(self):
        return self.find_element(AddImageLocators.UPLOAD_BUTTON)

    def more_first_name(self):
        return self.find_element(MoreInfoLocators.MORE_FIRST_NAME)

    def more_last_name(self):
        return self.find_element(MoreInfoLocators.MORE_LAST_NAME)

    def input_middle_name(self):
        return self.find_element(MoreInfoLocators.MORE_MIDDLE_NAME)

    def input_alter_name(self):
        return self.find_element(MoreInfoLocators.ALTER_NAME)

    def interests(self):
        return self.find_element(InterestsLocators.INPUT_INTEREST)

    def input_id_number(self):
        return self.find_element(OptionalLocators.INPUT_NUMBER)

    def input_institution(self):
        return self.find_element(OptionalLocators.INPUT_ORGANIZATION)

    def input_department(self):
        return self.find_element(OptionalLocators.INPUT_DEPARTMENT)

    def input_phone1(self):
        return self.find_element(OptionalLocators.INPUT_PHONE)

    def input_phone2(self):
        return self.find_element(OptionalLocators.INPUT_MOB_PHONE)

    def input_address(self):
        return self.find_element(OptionalLocators.INPUT_ADDRESS)

    def submit_save_button(self):
        return self.find_clickable_element(UserPageLocators.SAVE_BUTTON)

    def auto_login(self, data: AuthData):
        self.input(self.login_input(), data.login)
        self.input(self.password_input(), data.password)
        self.click(self.submit_button())

    def edit_user(self):
        self.click(self.submit_user_profile())
        self.click(self.submit_setting_button())
        self.click(self.submit_edit_button())

    def edit_info(self, data: UserData):
        logger.info(
            f"Editing basic personal data with next values:\n"
            f"name: {data.first_name}\n"
            f"lastname: {data.last_name}\n"
            f"email: {data.email}\n"
            f"moodle_net_profile: {data.moodlenet}\n"
            f"city: {data.city}\n"
            f"timezone: {data.time_zone}\n"

        )
        self.click_expand_all()
        self.input(self.input_first_name(), data.first_name)
        self.input(self.input_last_name(), data.last_name)
        self.input(self.input_email(), data.email)
        self.select_email_display(data.email_display_mode)
        self.select_time_zone(data.time_zone)
        self.input(self.input_moodlenet(), data.moodlenet)
        self.input(self.input_city(), data.city)

    def input_image(self, image: UserImage):
        self.click(self.add_image())
        self.input_file(self.upload_file(), image.image)
        self.click(self.button_upload())
        self.input(self.description_image(), image.description)

    def more_info(self, data: UserData):
        self.input(self.more_first_name(), data.first_name)
        self.input(self.more_last_name(), data.last_name)
        self.input(self.input_middle_name(), data.middle_name)
        self.input(self.input_alter_name(), data.first_name)

    def input_interests(self, data: UserData):
        self.input(self.interests(), data.interest)

    def input_optional(self, data: UserData):
        self.input(self.input_id_number(), data.id_number)
        self.input(self.input_institution(), data.institution)
        self.input(self.input_department(), data.department)
        self.input(self.input_phone1(), data.phone)
        self.input(self.input_phone2(), data.phone)
        self.input(self.input_address(), data.address)

    def save_changes(self):
        self.click(self.submit_save_button())

    def save_message(self):
        return self.find_element(UserPageLocators.SAVE_MESSAGE).text

    def is_changed(self):
        self.find_element(MoreInfoLocators.BODY)
        element = self.find_elements(MoreInfoLocators.CHANGE)
        if len(element) > 0:
            return True
        return False