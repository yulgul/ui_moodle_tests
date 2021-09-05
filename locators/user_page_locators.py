from selenium.webdriver.common.by import By

class UserPageLocators:
    USER_BUTTON = (By.CLASS_NAME, "userbutton")
    SETTING_BUTTON = (By.ID, "actionmenuaction-5")
    EDIT_LINK = (By.LINK_TEXT, "Редактировать информацию")
    INPUT_FIRST_NAME = (By.ID, "id_firstname")
    INPUT_EMAIL = (By.ID, "id_email")
    INPUT_CITY = (By.ID, "id_city")
    SAVE_BUTTON = (By.ID, "id_submitbutton")
    SAVE_MESSAGE = (By.CLASS_NAME, "alert-success")