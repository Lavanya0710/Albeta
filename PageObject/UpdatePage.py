import time

import selenium
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Configurations.Base_class import Basefunc


class UpdateVendor(Basefunc):
    upd_click_xpath = '//*[@id="vendor-row1"]/td[3]/a/span'
    # CheckBox_xpath = "//tr[starts-with(@id,'vendor-row')]//child::td"
    nomatch_xpath = '//*[@id="vendor"]/tbody/tr/td'
    search_vendor_name = "vendor_name"
    txtVendorName_id = "input-vendor-name"
    txtVendorResult_xpath = "//td[@class='text-left'][2]/a"
    all_v_name = "//tr//td[3]"
    single_name = "//tr[1]//td[3]"
    noMatchEle = '//tr//td'

    # CheckBox_xpath = "//tr[starts-with(@id,'vendor-row')]//child::td"
    # txtVendorResult_xpath = "//td[@class='text-left'][2]/a"
    # all_v_name = "//tr//td[3]"

    # txt_vendor_name_xpath = "//input[@id='input_vendor_name']"
    # drop_dwn_vendor_type_xpath = '//*[@id="input-vendor-type"]'
    # txt_first_name_xpath = "//input[@id='input-first-name']"
    # txt_last_name_xpath = "//input[@placeholder='LAST NAME']"
    # txt_vendor_code_xpath = "//body/form[@id='vendorForm']/div[@id='content']/div[2]/div[1]/div[1]/div[2]/div[2]/div[2]/input[1]"
    # txt_address_xpath = '//*[@id="input-address"]'
    # txt_city_xpath = "//*[@id='input-city']"
    # txt_state_xpath = "//*[@id='input-state']"
    # txt_phone_xpath = "//input[@id='input-phone']"
    # txt_zip_xpath = "//input[@id='input-zip']"
    # txt_email_xpath = "//input[@id='vemail']"
    # # drop_dwn_plcb_type_xpath = '//*[@id="content"]/div[2]/div/div/div[5]/div[1]/div[2]/select'
    # drop_dwn_plcb_type_xpath = "//body/form[@id='vendorForm']/div[@id='content']/div[2]/div[1]/div[1]/div[5]/div[1]/div[2]/select[1]"
    # drop_dwn_edi_xpath = '//*[@id="EDISelector"]'
    button_save_xpath = '//*[@id="form-vendor"]'
    button_cancel_xpath = '//*[@id="main_nav"]/div[2]/a'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # def click_CheckBox(self):
    #     self.wait_presence_of_element_located(By.XPATH, self.CheckBox_xpath).click()

    # def clickDelete(self):
    #     self.wait_presence_of_element_located(By.XPATH, self.Delete_xpath).click()
    def clickupdate(self):
        self.wait_presence_of_element_located(By.XPATH, self.upd_click_xpath).click()
        time.sleep(5)
    def clickOnSave(self):
        self.driver.find_element(By.XPATH, self.button_save_xpath).click()

    def setVendorName(self, vname):
        # try:
        self.wait_presence_of_element_located(By.ID, self.search_vendor_name).send_keys(vname)
        noMatch = self.wait_presence_of_element_located(By.XPATH,self.noMatchEle)
        if noMatch.text != vname:
            print("No vendor name matched here.")
            print('Driver is : ', self.driver)
            # self.driver.close()

        count = 0
        ele = self.wait_presence_of_all_elements_located(By.XPATH, self.all_v_name)

        if len(ele) >= 1:
            for i in ele:
                count += 1
                if i.text == vname:
                    ab = self.wait_presence_of_element_located(By.XPATH, '//tr[' + str(count) + '][starts-with(@id,"vendor-row")]//td[3]//a')
                    time.sleep(2)
                    ab.click()
                    # self.driver.close()
        else:
            print("No vendor name matched.")
            # self.driver.close()
        # except selenium.common.exceptions.InvalidSessionIdException:
        #     print ('SESSION IS invalid ....something is WRONG !! ')


    def UpVendorName(self, vname1):
        vendorField = self.wait_presence_of_element_located(By.ID, self.txtVendorName_id)
        vendorField.click()
        # time.sleep(1)
        vendorField.clear()
        # time.sleep(1)
        vendorField.send_keys(vname1)
        self.clickOnSave()


    # def UpVendorType(self, value):
    #     vendor_type_drp = Select(self.driver.find_element(By.XPATH, self.drop_dwn_vendor_type_xpath))
    #     vendor_type_drp.select_by_visible_text(value)

    # def setVendorType(self):
    #     vendor_type_drp = Select(self.driver.find_element(By.XPATH, self.drop_dwn_vendor_type_xpath))
    #     vendor_type_drp.select_by_index(2)

    # def UpFirstName(self, fname):
    #     self.wait_presence_of_element_located(By.XPATH, self.txt_first_name_xpath).click().clear()
    #     self.wait_presence_of_element_located(By.XPATH, self.txt_first_name_xpath).send_keys(fname)
    #
    # def UpLastName(self, lname):
    #     self.wait_presence_of_element_located(By.XPATH, self.txt_last_name_xpath).click().clear()
    #     self.wait_presence_of_element_located(By.XPATH, self.txt_last_name_xpath).send_keys(lname)
    #
    # def UpVendorCode(self, vendorcode):
    #     self.wait_presence_of_element_located(By.XPATH, self.txt_vendor_code_xpath).click().clear()
    #     self.wait_presence_of_element_located(By.XPATH, self.txt_vendor_code_xpath).send_keys(vendorcode)
    #
    # def UpAddress(self, address):
    #     self.wait_presence_of_element_located(By.XPATH, self.txt_address_xpath).click().clear()
    #     self.wait_presence_of_element_located(By.XPATH, self.txt_address_xpath).send_keys(address)
    #
    # def UpCity(self, city):
    #     self.wait_presence_of_element_located(By.XPATH, self.txt_city_xpath).click().clear()
    #     self.wait_presence_of_element_located(By.XPATH, self.txt_city_xpath).send_keys(city)
    #
    # def UpState(self, state):
    #     self.wait_presence_of_element_located(By.XPATH, self.txt_state_xpath).click().clear()
    #     self.wait_presence_of_element_located(By.XPATH, self.txt_state_xpath).send_keys(state)
    #
    # def Upphone(self, phone):
    #     self.wait_presence_of_element_located(By.XPATH, self.txt_phone_xpath).click().clear()
    #     self.wait_presence_of_element_located(By.XPATH, self.txt_phone_xpath).send_keys(phone)
    #
    # def UpZip(self, zip):
    #     self.wait_presence_of_element_located(By.XPATH, self.txt_zip_xpath).click().clear()
    #     self.wait_presence_of_element_located(By.XPATH, self.txt_zip_xpath).send_keys(zip)
    #
    # def UpEmail(self, email):
    #     self.wait_presence_of_element_located(By.XPATH, self.txt_email_xpath).click().clear()
    #     self.wait_presence_of_element_located(By.XPATH, self.txt_email_xpath).send_keys(email)

    # def UpPlcb(self):
    #     return self.wait_presence_of_element_located(By.XPATH, self.drop_dwn_plcb_type_xpath)
    # plcb_drp.select_by_visible_text(value1)

    # def drop_down_plcb(self):
    #     self.setPlcb().click()

    # def select_plcb(self,Schedule):
    #     select = Select(self.drop_down_plcb())
    #     select.select_by_visible_text(Schedule)

    # def UpEdi(self, value2):
    #     Edi_drp = Select(self.wait_presence_of_element_located(By.XPATH, self.drop_dwn_vendor_type_xpath))
    #     Edi_drp.select_by_visible_text(value2)

    # def clickOnSave(self):
    #     self.driver.find_element(By.XPATH, self.button_save_xpath).click()

    def clickOnCancel(self):
        self.wait_presence_of_element_located(By.XPATH, self.button_cancel_xpath).click()

    # # def Update(self,vname1,fname,lname,vcode,address,city,state,phone,vzip,email):
    # def Save(self):
    #     self.clickOnSave()
    #     time.sleep(1)
