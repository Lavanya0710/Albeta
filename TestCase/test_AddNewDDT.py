import time
import pytest
import softest
from ddt import ddt,data,unpack
from PageObject.LoginPage import LoginPage
from PageObject.AddVendorPage import AddVendor
from utilities.readproperties import ReadConfig
from utilities.xlread import Utilities


@ddt
class Test_alberta_git_search_dpt(softest.TestCase):
    baseURL = ReadConfig.getApplicationURL()
    User_Email = ReadConfig.getUseremail()
    User_Password = ReadConfig.getPassword()

    @pytest.fixture(autouse=True)
    def class_AddNew_setup(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        self.Vn = AddVendor(self.driver)

    @data(*Utilities.read_data_from_excel("C:\\Users\\getma\\PycharmProjects\\Alb\\TestData\\LoginData.xlsx","AddNew"))
    @unpack
    def test_searchven(self,vname,fname,lname,vcode,address,city,state,phone,vzip,email):
        self.lp.setUserName(self.User_Email)
        self.lp.setPassword(self.User_Password)
        self.lp.clickLogin()
        self.Vn.VendorModule()
        self.Vn.AddNewModule(vname,fname,lname,vcode,address,city,state,phone,vzip,email)
        time.sleep(5)
        self.driver.close()

