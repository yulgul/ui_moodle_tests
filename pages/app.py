from pages.create_course_page import CreateCoursePage
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage


class Application:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        self.login = LoginPage(self)
        self.profile = ProfilePage(self)
        self.course = CreateCoursePage(self)

    def open_main_page(self):
        self.driver.get(self.url)

    def quit(self):
        self.driver.quit()

    def open_auth_page(self):
        self.driver.get(self.url + "/login/index.php")

    def open_create_course_page(self):
        self.driver.get(self.url + "/admin/search.php#linkcourses")

    def open_manager_course_page(self):
        self.driver.get(self.url + "/course/management.php")