import time
import pytest
from PageObject.LoginPage import LoginPage
from utilities import XLUtils
from utilities.customlogger import LogGen
from utilities.readproperties import ReadConfig


class Test_002_DDT_Login:
    baseURL = ReadConfig.getApplicationURL()
    path = ".\\TestData\\LoginData.xlsx"
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_Login_ddt(self, setup):
        self.logger.info("*****Test_002_DDT_Login*****")
        self.logger.info("---Verifying Login DDT Test---")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.rows = XLUtils.getRowCount(self.path, 'Login')
        print("Total number of rows:", self.rows)

        lst_status = []

        for r in range(2, self.rows + 1):
            self.user = XLUtils.readData(self.path, 'Login', r, 1)
            self.password = XLUtils.readData(self.path, 'Login', r, 2)
            self.exp = XLUtils.readData(self.path, 'Login', r, 3)
            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(3)

            act_title = self.driver.title
            exp_title = "Customer-Alberta | Dashboard"
            if act_title == exp_title:
                if self.exp == "Pass":
                    self.logger.info("---Passed---")
                    self.lp.clickLogout()
                    lst_status.append("Pass")
                elif self.exp == "Fail":
                    self.logger.info("---Failed---")
                    self.lp.clickLogout()
                    lst_status.append("Fail")
            elif act_title != exp_title:
                if self.exp == "Pass":
                    self.logger.info("---Failed---")
                    self.lp.clickLogout()
                    lst_status.append("Fail")
                elif self.exp == "Fail":
                    self.logger.info("---Passed---")
                    self.driver.close()
                    # self.lp.clickLogout()
                    lst_status.append("Pass")

        if "Fail" not in lst_status:
            self.logger.info("---Login DDT test Passed---")
            self.logger.info("***End of the Login DDT Test***")
            self.logger.info("***completed Test_002_DDT_Login***")
            assert True
        else:
            self.logger.info("---Login DDT test Failed---")
            self.driver.close()
            assert False
        self.logger.info("***End of the Login DDT Test***")
        self.logger.info("***completed Test_002_DDT_Login***")

