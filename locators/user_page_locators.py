from selenium.webdriver.common.by import By


class UserPageLocators:
    USER_BUTTON = (By.CLASS_NAME, "userbutton")
    SETTING_BUTTON = (By.ID, "actionmenuaction-5")
    EDIT_LINK = (By.LINK_TEXT, "Редактировать информацию")
    CLICK_EXPAND_ALL = (By.LINK_TEXT, "Развернуть всё")
    INPUT_FIRST_NAME = (By.ID, "id_firstname")
    INPUT_LAST_NAME = (By.ID, "id_lastname")
    INPUT_EMAIL = (By.ID, "id_email")
    INPUT_CITY = (By.ID, "id_city")
    SAVE_BUTTON = (By.ID, "id_submitbutton")
    SAVE_MESSAGE = (By.CLASS_NAME, "alert-success")
    EMAIL_DISPLAY = (By.ID, "id_maildisplay")
    INPUT_MOODLENET = (By.ID, "id_moodlenetprofile")
    TIME_ZONE = (By.ID, "id_timezone")


class AddImageLocators:
    ADD = (By.CLASS_NAME, "fp-btn-add")
    INPUT_FILE = (By.NAME, "repo_upload_file")
    UPLOAD_BUTTON = (By.CLASS_NAME, "fp-upload-btn")
    INPUT_DESCRIPTION = (By.ID, "id_imagealt")


class MoreInfoLocators:
    MORE_FIRST_NAME = (By.ID, "id_firstnamephonetic")
    MORE_LAST_NAME = (By.ID, "id_lastnamephonetic")
    MORE_MIDDLE_NAME = (By.ID, "id_middlename")
    ALTER_NAME = (By.ID, "id_alternatename")
    BODY = (By.ID, "region-main-box")
    CHANGE = (By.CLASS_NAME, "alert-success")


class InterestsLocators:
    INPUT_INTEREST = (By.CSS_SELECTOR, "input[placeholder='Введите теги...']")


class OptionalLocators:
    INPUT_NUMBER = (By.ID, "id_idnumber")
    INPUT_ORGANIZATION = (By.ID, "id_institution")
    INPUT_DEPARTMENT = (By.ID, "id_department")
    INPUT_PHONE = (By.ID, "id_phone1")
    INPUT_MOB_PHONE = (By.ID, "id_phone2")
    INPUT_ADDRESS = (By.ID, "id_address")
