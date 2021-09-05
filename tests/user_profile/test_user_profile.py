import time

from common.constans import ChangeConstant
from models.auth import AuthData
from models.user_data import UserData


class TestUserProfile:
    def test_edit_userprofile(self, app):
        """
                Steps
                1. Auth with valid data
                2.
                3.

               """
        app.open_auth_page()
        data = AuthData(login="admi-test", password="TestQa-1")
        app.profile.auto_login(data)
        app.profile.edit_user()
        data = UserData.random()
        app.profile.input_data(data)
        app.profile.save_changes()
        assert ChangeConstant.CHANGE_MESSAGE == app.profile.save_message(), "Изменения не сохранены"




