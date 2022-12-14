from selenium.webdriver.common.by import By
from Configurations.Base_class import Basefunc


class SearchVendor(Basefunc):
    # Add Vendor Page
    txt_SupplierCode_id = "supplier_code"
    txtVendorName_id = "vendor_name"
    txtPhoneNo_id = "phone"
    txtEmail_id = "email"
    # CheckBox_xpath = "//tr[1][starts-with(@id,'vendor-row')]//child::td[1]"


    results_xpath = "//tr[starts-with(@id,'vendor-row')]//child::input"
    nomatch_xpath = '//*[@id="vendor"]/tbody/tr/td'

    # tblSearchResults_xpath='//*[@id="vendor"]/tbody'
    # table_xpath='//*[@id="form-vendor"]/div'
    # tableRows_xpath='//*[@id="vendor-row"]'
    # tableColumns_xpath="//table[@id='customers-grid']//tbody/tr/td"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # def setSupplierCode(self, code):
    #     self.wait_presence_of_element_located(By.ID, self.txt_SupplierCode_id).clear()
        #self.wait_presence_of_element_located(By.ID, self.txt_SupplierCode_id).send_keys(code)

    def setVendorName(self, vname):
        self.wait_presence_of_element_located(By.ID, self.txtVendorName_id).clear()
        self.wait_presence_of_element_located(By.ID, self.txtVendorName_id).send_keys(vname)

    def setPhone(self, number):
        self.wait_presence_of_element_located(By.ID, self.txtPhoneNo_id).clear()
        self.wait_presence_of_element_located(By.ID, self.txtPhoneNo_id).send_keys(number)

    def setEmail(self, email):
        self.wait_presence_of_element_located(By.ID, self.txtEmail_id).clear()
        self.wait_presence_of_element_located(By.ID, self.txtEmail_id).send_keys(email)




    def disp_result(self):
        lst = self.wait_presence_of_element_located(By.XPATH, self.results_xpath)
        return lst

    def nomatch(self):
        return self.wait_presence_of_element_located(By.XPATH, self.nomatch_xpath)

    def set_searchvendor(self, code):
        return self.wait_presence_of_element_located(By.ID, self.txt_SupplierCode_id).send_keys(code)
            #self.setSupplierCode().send_keys(code)

    def display_Vendor_exist(self, code):
        code = str(code)
        print(code)
        print(self.disp_result().get_attribute("value"))
        # if code in self.disp_result().get_attribute("value"):
        #     # try:
        #     print("------------------------------------------")
        #     print(self.disp_result().get_attribute("value"))
        #
        # if code in self.nomatch().get_attribute("value"):
        #      print("**------------********")
        #      print('Value Does Not Exist')


        for i in self.disp_result():
            if i.get_attribute("value") == code:
                print('vender does not exist')
                assert True
            else:
                  print(self.nomatch().text(),"no matching found")
                  if self.nomatch().text() == 'No matching records found':
                      print('Vendor does not exist')
                      assert True
