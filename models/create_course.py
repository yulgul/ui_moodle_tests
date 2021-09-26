import random

from faker import Faker

from common.constans import CreateCourseConstants

fake = Faker('Ru-ru')


class CreateCourseData:
    def __init__(self, full_course_name=None, short_course_name=None,
                 end_day=None, end_month=None, end_year=None,
                 end_hour=None, end_minute=None, description_course=None,
                 section_number=None, displaying_hidden_section=None,
                 presentation_course=None, course_language=None,
                 number_ads=None, max_bytes=None, manager_name=None,
                 teacher_name=None, student_name=None):
        self.full_course_name = full_course_name
        self.short_course_name = short_course_name
        self.end_day = end_day
        self.end_month = end_month
        self.end_year = end_year
        self.end_hour = end_hour
        self.end_minute = end_minute
        self.description_course = description_course
        self.section_number = section_number
        self.displaying_hidden_section = displaying_hidden_section
        self.presentation_course = presentation_course
        self.course_language = course_language
        self.number_ads = number_ads
        self.max_bytes = max_bytes
        self.manager_name = manager_name
        self.teacher_name = teacher_name
        self.student_name = student_name

    @staticmethod
    def random():
        full_course_name = fake.job()+fake.building_number()
        short_course_name = fake.word()
        end_day = str(random.randint(1, 31))
        end_month = str(random.randint(1, 12))
        end_year = str(
            random.randint(
                CreateCourseConstants.CURRENT_YEAR, CreateCourseConstants.LAST_YEAR
            )
        )
        end_hour = str(random.randint(0, 23))
        end_minute = str(random.randint(0, 59))
        description_course = fake.word()
        section_number = str(random.randint(0, CreateCourseConstants.SECTION_NUMBER))
        displaying_hidden_section = random.choice(
            list(CreateCourseConstants.CHOICE_OF_TWO.values())
        )
        presentation_course = random.choice(
            list(CreateCourseConstants.CHOICE_OF_TWO.values())
        )
        course_language = CreateCourseConstants.COURSE_LANGUAGE
        number_ads = str(random.randint(0, 10))
        max_bytes = str(random.choice(CreateCourseConstants.FILE_SIZES_VALUES))
        manager_name = fake.word()
        teacher_name = fake.word()
        student_name = fake.word()
        return CreateCourseData(full_course_name, short_course_name,
                                end_day, end_month, end_year, end_hour, end_minute,
                                description_course, section_number,
                                displaying_hidden_section, presentation_course, course_language,
                                number_ads, max_bytes, manager_name,
                                teacher_name, student_name )
