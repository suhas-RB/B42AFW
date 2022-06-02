from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions


class EnterTimeTrackPage:
    __logoutLink=(By.ID,"logoutLink")

    def __init__(self, driver):
        self.driver = driver

    def verify_homepage_is_displayed(self,wait):
        try:
            wait.until(expected_conditions.visibility_of_element_located(self.__logoutLink))
            print("Home page is displayed")
            return True
        except:
            print("Home page is not displayed")
            return False