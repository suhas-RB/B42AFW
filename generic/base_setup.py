import pytest
from pyjavaproperties import Properties
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.wait import WebDriverWait

class Base_Setup:

    @pytest.fixture(autouse=True)
    def pre_condition(self):
        pfile = Properties()
        pfile.load(open("config.properties"))
        ITO=pfile["ITO"]
        ETO=pfile["ETO"]
        URL=pfile["URL"]
        GRID=pfile["GRID"]
        GRID_URL=pfile["GRID_URL"]
        BROWSER=pfile["BROWSER"]

        if GRID=="Yes":
            print("Using grid for script execution")
            if BROWSER=="chrome":
                browser_type=webdriver.ChromeOptions()
            else:
                browser_type=webdriver.FirefoxOptions()

            print("Opening the ",BROWSER," browser in remote system")
            self.driver = webdriver.Remote(command_executor=GRID_URL,options=browser_type)
        else:
            print("Using local system for script execution")
            print("Opening the ", BROWSER, " browser in local system")
            if BROWSER == "chrome":
                self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
            else:
                self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

        self.driver.implicitly_wait(ITO)
        self.driver.maximize_window()
        self.driver.get(URL)
        self.wait=WebDriverWait(self.driver,ETO)

    @pytest.fixture(autouse=True)
    def post_condition(self):
        yield
        print("Closing the browser")
        self.driver.quit()
