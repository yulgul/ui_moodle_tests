import pytest

from common.constans import DeleteCourseConstants
from models.create_course import CreateCourseData


class TestCreateCourse:
    def test_create_course(self, app, auth):
        """
        Steps
        1. Authorize under admin.
        2. Go to Create Course page.
        3. Fill in fields: «Полное название курса», «Краткое название курса».
        4. Enter day, month, year and time for course end date.
        5. In section "Общие" fill in fields:  «Дата окончания курса», «Описание».
        6. In section "Формат курса" choose number in  «Количество секций».
        7. In section "Внешний вид" choose Russian language
            in dropdown «Принудительный язык».
        8. In section "Файлы и загрузки" choose value
            in dropdown «Максимальный размер загружаемого файла».
        9. In section "Переименование Ролей" fill in fields:
            «Ваше слово вместо «Управляющий»»,
            «Ваше слово вместо «Учитель»»,
            «Ваше слово вместо «Студент»».
        10. Click button «Сохранить и показать».
        11. Click button «Перейти к курсу».
        12. Check if the created course name is in the page header.
        13. Go to manager course page.
        14. Click button «Управление курсами».
        15. Find the created course name on the page.
        16. Click delete button next to the new course name.
        17. Confirm deletion by clicking «Удалить».
        18. Check for text "{the new course name} был полностью удален".
                """
        app.open_create_course_page()
        data = CreateCourseData.random()
        app.course.create_course(data)
        assert (app.course.new_course_page() == data.full_course_name
        ), "The course was not created!"
        app.course.delete_creation_course(data)
        message = DeleteCourseConstants.DeleteCourse + data.short_course_name
        assert message == app.course.message_delete_course()

    @pytest.mark.parametrize(
        "full_course_name, short_course_name",
        [[CreateCourseData.random().full_course_name, None], [None, CreateCourseData.random().short_course_name]],
    )
    def test_invalid_course_creation(self, app, auth, full_course_name, short_course_name):
        """
        Steps
        1. Authorize under admin.
        2. Go to Create Course page.
        3. Do not fill in the required field  «Полное название курса».
        4. Fill in field «Краткое название курса».
        5. Click button «Сохранить и показать».
        6. Check for text "- Заполните поле" или "- Не указано краткое название".
        """
        app.open_create_course_page()
        course_info = CreateCourseData.random()
        setattr(course_info, "full_course_name", full_course_name)
        setattr(course_info, "short_course_name", short_course_name)
        app.course.create_course(course_info)
        assert (
                app.course.is_course_name_error() is True
        ), "The course was created without required field!!"

