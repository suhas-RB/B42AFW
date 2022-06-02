import pytest

from generic.base_setup import Base_Setup
from page.login_page import LoginPage
from page.Enter_time_track_page import EnterTimeTrackPage
from generic.utility import Excel

class TestValidLogin(Base_Setup):

    @pytest.mark.run(order=1)
    def test_valid_login(self):
        un=Excel.get_data(self.xl_path,"Sheet1",2,1)
        pw=Excel.get_data(self.xl_path,"Sheet1",2,2)

        # 1.	Enter valid username
        login_page = LoginPage(self.driver)
        login_page.set_username(un)

        # 2.	Enter valid password
        login_page.set_password(pw)

        # 3.	Click login button
        login_page.click_loginbutton()

        # 4.	Verify that home page is displayed
        enter_time_track_page = EnterTimeTrackPage(self.driver)
        result = enter_time_track_page.verify_homepage_is_displayed(self.wait)
        assert result
