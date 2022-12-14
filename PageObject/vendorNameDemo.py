from selenium.webdriver.common.by import By
from Configurations.Base_class import Basefunc

class DeleteVendor(Basefunc):
    Delete_xpath = "//button[@id='vender_delete']"
    CheckBox_xpath = "//tr[starts-with(@id,'vendor-row')]//child::td"
    ele = "//tr[starts-with(@id,'vendor-row')]//child::td[3]"
    txtVendorName_id = "vendor_name"
    v_count = 0

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
    def click_CheckBox(self):
        self.wait_presence_of_element_located(By.XPATH, self.CheckBox_xpath).click()

    def clickDelete(self):
        self.wait_presence_of_element_located(By.XPATH, self.Delete_xpath).click()

    def setVendorName(self, vname):
        self.wait_presence_of_element_located(By.ID, self.txtVendorName_id).send_keys(vname)

    def vendorNameList(self):
        vname_list = self.wait_presence_of_all_elements_located(By.XPATH,self.ele)
        if len(vname_list) == 0:
            print('No such record match.')
        elif len(vname_list)>1:
            for i in vname_list:
                v_count =+1
                if i.text() == self.vname:
                    self.wait_presence_of_element_located(By.XPATH, ).click()


