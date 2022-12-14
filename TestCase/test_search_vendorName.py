import time
import pytest
from PageObject.LoginPage import LoginPage
from PageObject.AddVendorPage import AddVendor
from PageObject.SearchVendorPage import SearchVendor
from utilities.customlogger import LogGen
from utilities.readproperties import ReadConfig


class Test_SearchVendorName_005:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_SearchVendorName(self,setup):
        self.logger.info("************* Search_005 **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************* Login succesful **********")

        self.logger.info("******* Starting Search vendor **********")

        self.Vn = AddVendor(self.driver)
        self.Vn.clickOnVendorMenu()

        self.logger.info("************* searching the Vendor **********")

        sv = SearchVendor(self.driver)
        sv.setVendorName('test')
        # sv.clickCheckBox()
        time.sleep(1)

        self.driver.close()

        self.logger.info("***************  TC_ByName_005 Finished  *********** ")