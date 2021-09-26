class LoginConstant:
    AUTH_ERROR = "Неверный логин или пароль, попробуйте заново."


class ChangeConstant:
    CHANGE_MESSAGE = "×\nИзменения сохранены"


class PersonalDataConstants:
    EMAIL_DISPLAY_MODES = {
        "hidden": "0",
        "all_can_see": "1",
        "show_to_course_participants": "2",
    }
    TIMEZONE_VALUES = (
        "99",  # server's timezone
        "Asia/Dubai",
        "America/Santiago",
        "Africa/Tunis",
        "Europe/Moscow",
        "Europe/Moscow",
        "UTC",
    )

class CreateCourseConstants:
    SECTION_NUMBER = 52
    COURSE_LANGUAGE = "ru"
    CURRENT_YEAR = 2021
    LAST_YEAR = 2050
    CHOICE_OF_TWO = {
        "first": "0",
        "second": "1",
    }
    FILE_SIZES_VALUES = [
        0,
        2097152,
        1048576,
        512000,
        102400,
        51200,
        10240,
    ]

class DeleteCourseConstants:
    DeleteCourse = "Удаление "