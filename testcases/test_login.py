import pytest
from Login.Login import Login
from utility.Baseclass import Basepage
@pytest.mark.usefixtures("setup")

class Testlogin:
    @pytest.mark.parametrize('username, password', [
        ("Admin", "admin123"),
        ("kannan", "admin123"),
        ("Admin", "sunil123"),
        ("sanjala", "sanjala123") ])

    def test_Login(self,username,password):
        driver = self.driver
        obj = Login(driver)
        obj.login(username,password)
