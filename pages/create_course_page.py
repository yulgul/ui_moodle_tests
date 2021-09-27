import logging

from selenium.webdriver.remote.webelement import WebElement

from locators.create_course_locators import CreateCourseLocators
from models.create_course import CreateCourseData
from pages.base_page import BasePage

logger = logging.getLogger("moodle")

class CreateCoursePage(BasePage):

    def click_add_course(self):
        return self.find_element(CreateCourseLocators.CLICK_ADD_COURSE)

    def click_expand_all(self):
        expand_all = self.find_element(CreateCourseLocators.CLICK_EXPAND_ALL)
        return self.click(expand_all)


    def input_full_course_name(self, text):
        full_course_name = self.find_element(CreateCourseLocators.INPUT_FULL_COURSE_NAME)
        return self.input(full_course_name, text)


    def input_short_course_name(self):
        return self.find_element(CreateCourseLocators.INPUT_SHORT_COURSE_NAME)

    def select_end_day(self):
        end_day = self.find_select_element(CreateCourseLocators.SELECT_END_DAY)
        return end_day

    def select_value_end_day(self, value):
        self.select_value(self.select_end_day(), value)

    def select_end_month(self):
        end_month = self.find_select_element(CreateCourseLocators.SELECT_END_MONTH)
        return end_month

    def select_value_end_month(self, value):
        self.select_value(self.select_end_month(), value)

    def select_end_year(self):
        end_year = self.find_select_element(CreateCourseLocators.SELECT_END_YEAR)
        return end_year

    def select_value_end_year(self, value):
        self.select_value(self.select_end_year(), value)

    def select_end_hour(self):
        end_hour = self.find_select_element(CreateCourseLocators.SELECT_END_HOUR)
        return end_hour

    def select_value_end_hour(self, value):
        self.select_value(self.select_end_hour(), value)

    def select_end_minute(self):
        end_minute = self.find_select_element(CreateCourseLocators.SELECT_END_MINUTE)
        return end_minute

    def select_value_end_minute(self, value):
        self.select_value(self.select_end_minute(), value)

    def input_description_course(self, text):
        description_course = self.find_clickable_element(CreateCourseLocators.INPUT_DESCRIPTION_COURSE)
        return self.input(description_course, text)

    def select_count_section(self):
        count_section = self.find_select_element(CreateCourseLocators.SELECT_COUNT_SECTION)
        return count_section

    def select_value_count_section(self, value):
        self.select_value(self.select_count_section(), value)

    def select_displaying_hidden_section(self):
        count_section = self.find_select_element(CreateCourseLocators.SELECT_DISPLAYING_HIDDEN_SECTIONS)
        return count_section

    def select_value_displaying_hidden_section(self, value):
        self.select_value(self.select_displaying_hidden_section(), value)

    def select_presentation_course(self):
        presentation_course = self.find_select_element(CreateCourseLocators.SELECT_PRESENTATION_COURSE)
        return presentation_course

    def select_value_presentation_course(self, value):
        self.select_value(self.select_presentation_course(), value)

    def select_course_language(self):
        course_language = self.find_select_element(CreateCourseLocators.SELECT_COURSE_LANGUAGE)
        return course_language

    def select_value_course_language(self, value):
        self.select_value(self.select_course_language(), value)

    def select_number_ads(self):
        number_ads = self.find_select_element(CreateCourseLocators.SELECT_NUMBER_ADS)
        return number_ads

    def select_value_number_ads(self, value):
        self.select_value(self.select_number_ads(), value)

    def select_max_bytes(self):
        max_bytes = self.find_select_element(CreateCourseLocators.SELECT_MAX_BYTES)
        return max_bytes

    def select_value_max_bytes(self, value):
        self.select_value(self.select_max_bytes(), value)

    def input_manager(self, text):
        manager = self.find_element(CreateCourseLocators.INPUT_MANAGER)
        return self.input(manager, text)

    def input_teacher(self, text):
        teacher = self.find_element(CreateCourseLocators.INPUT_TEACHER)
        return self.input(teacher, text)

    def input_student(self, text):
        student = self.find_element(CreateCourseLocators.INPUT_STUDENT)
        return self.input(student, text)

    def submit_change(self):
        submit_change = self.find_clickable_element(CreateCourseLocators.SUBMIT_CHANGE)
        return self.click(submit_change)


    def create_course(self, data: CreateCourseData):
        self.click(self.click_add_course())
        self.click_expand_all()
        logger.info(f'Full course name is "{data.full_course_name}".')
        self.input_full_course_name(data.full_course_name)
        logger.info(f'Short course name is "{data.short_course_name}".')
        self.input(self.input_short_course_name(), data.short_course_name)
        self.select_value_end_day(data.end_day)
        self.select_value_end_month(data.end_month)
        self.select_value_end_year(data.end_year)
        self.select_value_end_hour(data.end_hour)
        self.select_value_end_minute(data.end_minute)
        self.input_description_course(data.description_course)
        self.select_value_count_section(data.section_number)
        self.select_value_displaying_hidden_section(data.displaying_hidden_section)
        self.select_value_presentation_course(data.presentation_course)
        self.select_value_course_language(data.course_language)
        self.select_value_number_ads(data.number_ads)
        self.select_value_max_bytes(data.max_bytes)
        self.input_manager(data.manager_name)
        self.input_teacher(data.teacher_name)
        self.input_student(data.student_name)
        logger.info("Submitting changes.")
        self.submit_change()

    def new_course_page(self):
        return self.find_element(CreateCourseLocators.NEW_COURSE_HEADER).text

    def input_course_by_full_name(self, text) -> WebElement:
        course_by_full_name = self.find_element(CreateCourseLocators.INPUT_SEARCH_COURSE)
        return self.input(course_by_full_name, text)

    def click_find_course_by_full_name(self):
        click_course_by_full_name = self.find_element(CreateCourseLocators.BUTTON_SEARCH_COURSE)
        return self.click(click_course_by_full_name)

    def delete_course(self):
        delete = self.find_element(CreateCourseLocators.DELETE_COURSE_BUTTON)
        return self.click(delete)

    def confirm_delete(self) -> WebElement:
        confirm_delete = self.find_element(CreateCourseLocators.CONFIRM_DELETE_BUTTON)
        return self.click(confirm_delete)


    def delete_creation_course(self, data: CreateCourseData):
        self.app.open_manager_course_page()
        self.input_course_by_full_name(data.full_course_name)
        self.click_find_course_by_full_name()
        self.delete_course()
        self.confirm_delete()

    def message_delete_course(self):
        return self.find_element(CreateCourseLocators.COURSE_DELETE_CONFIRMATION).text

    def is_full_course_name_error(self) -> bool:
        element = self.find_elements(CreateCourseLocators.FULLNAME_ERROR)
        if len(element) > 0:
            return True
        return False

    def is_short_course_name_error(self) -> bool:
        element = self.find_elements(CreateCourseLocators.SHORTNAME_ERROR)
        if len(element) > 0:
            return True
        return False

    def is_course_name_error(self):
        if self.is_short_course_name_error() or self.is_full_course_name_error():
            return True
        return False






