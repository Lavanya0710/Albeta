import time

import softest
from ddt import ddt, data, unpack
import pytest
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
import chromedriver_autoinstaller

from PageObject.AddVendorPage import AddVendor
from PageObject.LoginPage import Login_credentials
from PageObject.SearchVendorPage import SearchVendor
from PageObject.broswer_close import Close_browser
from utilities.xlread import Utilities


@ddt
class TestAlberta(softest.TestCase):
    driver = webdriver.Chrome(service=Service(chromedriver_autoinstaller.install()))
    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.ut = Utilities()
        self.lc = Login_credentials(self.driver)
        self.close_b = Close_browser(self.driver)
        self.Vn = AddVendor(self.driver)
        self.src = SearchVendor(self.driver)

# Step 1: Login
    @data(*Utilities.read_data_from_excel("C:\\Users\\getma\\PycharmProjects\\Alb\\TestData\\LoginData.xlsx","Login"))
    @unpack
    def test_alberta_login(self, User_Email, User_Password, URL):
        self.lc.login_page_credentials(User_Email, User_Password, URL)

#Step 2: Click on VendorModule
        # self.Vn.ClickModule()
        # self.Vn.VendorModule()

# Step 2:Add vendor
    @data(('subhash1','subhash','kumar','654321','fjkwsjglwsjdflsjkfk','sfhkwsjflwsjd','jsfnkejhfkwsrjdf','7894561237','654321','dfsd@gmail.com'))
    # @data(*Utilities.read_data_from_excel("C:\\Users\\getma\\PycharmProjects\\Alb\\TestData\\LoginData.xlsx","AddNew"))
    @unpack
    def test_addven(self, vname, fname, lname, vcode, address, city, state, phone, vzip, email):
        self.Vn.AddNewModule(vname, fname, lname, vcode, address, city, state, phone, vzip, email)
        time.sleep(10)
#
# #Step 3: Search vendor
    # @data(*Utilities.read_data_from_excel("C:\\Users\\getma\\PycharmProjects\\Alb\\TestData\\LoginData.xlsx", "Vname"))
    # @unpack
    # def test_searchven(self, vendorname):
    #
    #     self.Vn.VendorModule()
    #     self.src.setVendorName(vendorname)
    #     time.sleep(15)

# Step 4: Close browser
    def test_z_close_b(self):
        self.close_b.browser_close()


