import time
import pytest
import softest
from ddt import ddt,data,unpack
from PageObject.LoginPage import LoginPage
from PageObject.AddVendorPage import AddVendor
from PageObject.SearchVendorPage import SearchVendor
from utilities.readproperties import ReadConfig
from utilities.xlread import Utilities


@ddt
class Test_alberta_git_search_dpt(softest.TestCase):
    baseURL = ReadConfig.getApplicationURL()
    User_Email = ReadConfig.getUseremail()
    User_Password = ReadConfig.getPassword()

    @pytest.fixture(autouse=True)
    def class_srcven_setup(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        self.Vn = AddVendor(self.driver)
        self.src = SearchVendor(self.driver)


    @data(*Utilities.read_data_from_excel("C:\\Users\\getma\\PycharmProjects\\Alb\\TestData\\LoginData.xlsx","Gmail"))
    @unpack
    def test_searchven(self,email):
        self.lp.setUserName(self.User_Email)
        self.lp.setPassword(self.User_Password)
        self.lp.clickLogin()
        self.Vn.SrchModule()
        self.src.setEmail(email)
        time.sleep(2)
        self.driver.close()
