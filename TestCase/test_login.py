import time

import pytest

from PageObject.LoginPage import LoginPage
from utilities.customlogger import LogGen
from utilities.readproperties import ReadConfig

class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_homePageTitle(self,setup):
        self.logger.info("***************** Test_001_Login **************************")
        self.logger.info("---Verifying Home Page Title---")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        if act_title == "Administration | Login":
            assert True
            self.driver.close()
            self.logger.info("---Home Page Title Test Is Passed---")
        else:
            self.driver.save_screenshot(".\\Alb\\Screenshots\\"+"test_homePageTitle1.png")
            self.driver.close()
            self.logger.error("---Home Page Title Test Is Failed---")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_Login(self, setup):
        self.logger.info("---Verifying Login Test---")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(1)
        act_title = self.driver.title
        if act_title == "Customer-Alberta | Dashboard":
            self.driver.close()
            self.logger.info("---Login Page Test Is Passed---")
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_Login1")
            self.driver.close()
            self.logger.error("---Login Page Test Is Failed---")
            assert False
