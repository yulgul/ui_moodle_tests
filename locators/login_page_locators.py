from selenium.webdriver.common.by import By

class LoginPageLocators:
    LOGIN = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    BUTTON_SUBMIT = (By.ID, "loginbtn")