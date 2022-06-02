from generic.base_setup import Base_Setup
from page.login_page import LoginPage
from page.Enter_time_track_page import EnterTimeTrackPage


class Test_ValidLogin(Base_Setup):

    def test_validlogin(self):
        # 1.	Enter valid username
        login_page = LoginPage(self.driver)
        login_page.set_username("admin")

        # 2.	Enter valid password
        login_page.set_password("manager")

        # 3.	Click login button
        login_page.click_loginbutton()

        # 4.	Verify that home page is displayed
        enter_time_trak_page = EnterTimeTrackPage(self.driver)
        result = enter_time_trak_page.verify_homepage_is_displayed(self.wait)
        assert result
