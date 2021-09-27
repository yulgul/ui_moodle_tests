
from common.constans import ChangeConstant

from models.user_data import UserData, UserImage


class TestUserProfile:
    def test_edit_userprofile_valid_data(self, app, auth):
        app.profile.edit_user()
        data = UserData.random()
        app.profile.edit_info(data)
        image = UserImage.random()
        app.profile.input_image(image)
        app.profile.more_info(data)
        app.profile.input_interests(data)
        app.profile.input_optional(data)
        app.profile.save_changes()
        assert ChangeConstant.CHANGE_MESSAGE == app.profile.save_message(), "Изменения не сохранены"




