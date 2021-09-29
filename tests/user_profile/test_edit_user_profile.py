import pytest

from common.constans import ChangeConstant

from models.user_data import UserData, UserImage


class TestUserProfile:
    def test_edit_userprofile_valid_data(self, app, auth):
        """
        Steps
        1. Open auth page
        2. Auth with valid data
        3. Check auth result
        4. Go to page with editing personal data
        5. Edit basic personal data with valid data
        6. Check successfully editing
        """
        app.profile.edit_user()
        data = UserData.random()
        app.profile.edit_info(data)
        image = UserImage.random()
        app.profile.input_image(image)
        app.profile.more_info(data)
        app.profile.input_interests(data)
        app.profile.input_optional(data)
        app.profile.save_changes()
        assert (
            ChangeConstant.CHANGE_MESSAGE == app.profile.save_message()
        ), "Изменения не сохранены"

    @pytest.mark.parametrize("field", ["first_name", "last_name", "email"])
    def test_edit_basic_personal_data_without_required_field(self, app, auth, field):
        """
        Steps
        1. Open auth page
        2. Auth with valid data
        3. Go to page with editing personal data
        4. Edit basic personal data with invalid data
        5. Check editing is not successfully
        """

        app.profile.edit_user()
        data = UserData.random()
        setattr(data, field, "")
        app.profile.edit_info(data)
        image = UserImage.random()
        app.profile.input_image(image)
        app.profile.more_info(data)

        app.profile.save_changes()
        assert not app.profile.is_changed(), "Personal data should not be changed!"
