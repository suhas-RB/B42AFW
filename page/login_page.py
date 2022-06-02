from selenium.webdriver.common.by import By


class LoginPage:
    __unTB = (By.ID, "username")
    __pwTB = (By.NAME, "pwd")
    __loginBTN = (By.XPATH, "//div[.='Login ']")

    def __init__(self, driver):
        self.driver = driver

    def set_username(self, un):
        self.driver.find_element(*self.__unTB).send_keys(un)

    def set_password(self, pw):
        self.driver.find_element(*self.__pwTB).send_keys(pw)

    def click_loginbutton(self):
        self.driver.find_element(*self.__loginBTN).click()
