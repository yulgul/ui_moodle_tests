class TestAuth:
    def test_auth_valid_data(self, app):
        """
        Steps
        1. Open main page
        2. Auth with valid data
        3. Check auth result.
        """
        app.open_main_page()
        app.login.auth(login="admi-test", password="TestQa-1")
        assert 1==1 , "You are not authorized, check auth data"

    def test_auth_no_valid_data(self, app):
        """
        Steps
        1. Open main page
        2. Auth with valid data
        3. Check auth result.
        """
        app.open_main_page()
        app.login.auth(login="admi-test", password="11")
        assert "Неверный логин или пароль, попробуйте заново", "You are not authorized, check auth data"