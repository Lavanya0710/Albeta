import time

from selenium.webdriver.common.by import By
from Configurations.Base_class import Basefunc

class DeleteVendor(Basefunc):
    Delete_xpath = "//button[@id='vender_delete']"
    CheckBox_xpath = "//tr[starts-with(@id,'vendor-row')]//child::td"
    nomatch_xpath = '//*[@id="vendor"]/tbody/tr/td'
    txtVendorName_id = "vendor_name"
    txtVendorResult_xpath = "//td[@class='text-left'][2]/a"
    all_v_name = "//tr//td[3]"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
    def click_CheckBox(self):
        self.wait_presence_of_element_located(By.XPATH, self.CheckBox_xpath).click()

    def clickDelete(self):
        self.wait_presence_of_element_located(By.XPATH, self.Delete_xpath).click()

    def setVendorName(self, vname):
        self.wait_presence_of_element_located(By.ID, self.txtVendorName_id).send_keys(vname)
        count = 0
        ele = self.wait_presence_of_all_elements_located(By.XPATH, self.all_v_name)
        if len(ele)==0:
            print("No vendor name matched.")
        elif len(ele) == 1:
            self.click_CheckBox()
        elif len(ele)>1:
            for i in ele:
                count += 1
                if i.text == vname:
                    ab = self.wait_presence_of_element_located(By.XPATH, '//tr['+str(count)+'][starts-with(@id,"vendor-row")]//td[1]')
                    time.sleep(2)
                    ab.click()