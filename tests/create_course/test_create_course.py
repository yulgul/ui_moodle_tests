from common.constans import DeleteCourseConstants
from models.auth import AuthData
from models.create_course import CreateCourseData


class TestCreateCourse:
    def test_create_course(self, app):
        app.open_auth_page()
        data = AuthData(login="admi-test", password="TestQa-1")
        app.profile.auto_login(data)
        app.open_create_course_page()
        data = CreateCourseData.random()
        app.course.create_course(data)
        assert (app.course.new_course_page() == data.full_course_name
        ), "The course was not created!"
        app.course.delete_creation_course(data)
        message = DeleteCourseConstants.DeleteCourse + data.short_course_name
        assert message == app.course.message_delete_course()



