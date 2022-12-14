import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select



from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By

from Configurations.Base_class import Basefunc


class VendorCategory(Basefunc):
    vendor_mod_xpath = '//*[@id="main_nav"]/ul/li[2]/a'
    button_add_new_xpath = '//*[@id="main_nav"]/div/a'
    button_save_xpath = '//*[@id="form-vendor"]'
    button_cancel_xpath = '//*[@id="main_nav"]/div[2]/a'
    # subcategory add new items
    txt_vendor_name_xpath = "//input[@id='input_vendor_name']"
    txt_first_name_xpath = "//input[@id='input-first-name']"
    txt_last_name_xpath = "//input[@placeholder='LAST NAME']"
    txt_vendor_code_xpath = "//body/form[@id='vendorForm']/div[@id='content']/div[2]/div[1]/div[1]/div[2]/div[2]/div[2]/input[1]"
    txt_address_xpath = '//*[@id="input-address"]'
    txt_city_xpath = "//*[@id='input-city']"
    txt_state_xpath = "//*[@id='input-state']"
    txt_phone_xpath = "//input[@id='input-phone']"
    txt_zip_xpath = "//input[@id='input-zip']"
    txt_email_xpath = "//input[@id='vemail']"

    #
    # #######  Validating subcat add
    # link_subcatname_xpath='//tbody/tr/td/input'
    #
    # alert_msg="//*[contains(text(),'SubCategory Already Exist!!')]"
    #
    # textbox_search_subcatname_xpath='//*[@id="automplete-product"]'
    #
    # dropdown_text_subcat_CSS = '#ui-id-13'

    def _init_(self,driver):
        self.driver=driver

    def Vendor_Click(self):
        Ven=self.driver.find_element(By.XPATH, self.vendor_mod_xpath)
        Ven.click()
        time.sleep(2)

    # def inventory_subcategoryClick(self):
    #    #self.driver.find_element(By.XPATH, self.link_inventory_xpath).click()
    #    #time.sleep(2)
    #    inventory= self.driver.find_element(By.XPATH,self.link_inventory_xpath)
    #    subcategory=self.driver.find_element(By.XPATH,self.link_subcategory_xpath)
    #
    #    actions= ActionChains(self.driver)
    #    actions.move_to_element(inventory)
    #    actions.click(subcategory)
    #    actions.perform()
    #    time.sleep(2)

    def addNewSubCategoryClick(self):
       return  self.wait_presence_of_element_located(By.XPATH,self.button_addnewsubcat_xpath).click()

    def get_subcat_name(self):
        return self.wait_presence_of_element_located(By.ID, self.textbox_subcatname_id)

    def add_Subcat_name(self, Name):
        if(Name is None):
            pass
        else:
            for i in Name:
                self.get_subcat_name().send_keys(i)


    def add_Category_name(self,Category):
        if Category is None:
            pass
        else:
            dropdown=Select(self.wait_presence_of_element_located(By.ID,self.dropdown_category_id))
            dropdown.select_by_visible_text(Category)
            time.sleep(2)

    def saveSubCatClick(self,Name,Category):
        self.wait_presence_of_element_located(By.ID,self.button_savesubcat_id).click()
        if Name  is None:
            self.driver.switch_to.alert.accept()
            time.sleep(2)
        elif Category is None:
            self.driver.switch_to.alert.accept()
            time.sleep(2)
        else:
            print("in validate")
            self.validateSubcatAdd(Name)


    def validateSubcatAdd(self,Name):
        print("reached validate category")
        print("name=",Name)
        print(self.driver.title,"title of the page")

        try:
                if self.driver.title=="Customer-Alberta | Sub Category":
                    time.sleep(2)
                    for i in Name:
                        self.wait_presence_of_element_located(By.XPATH,self.textbox_search_subcatname_xpath).send_keys(i)
                    time.sleep(2)

                    print("**********************",Name)
                    subcat_name=self.wait_presence_of_element_located(By.XPATH,"//li[@class='ui-menu-item']//child::div[contains(text(),'" + Name + "')]")
                    time.sleep(2)
                    if(subcat_name.is_displayed()):
                        time.sleep(2)
                        subcat_name.click()
                        time.sleep(2)
                        print("SubCategory Added Successfully!!")

                    else:
                        print("Unable to add Subcategory")



        except NoSuchElementException:
            print("No such element exist")

    def cancelSubCatClick(self):
        self.wait_presence_of_element_located(By.XPATH,self.button_cancelsubcat_xpath)

    def addsubCategory(self,Name,Category):
        self.inventory_subcategoryClick()
        self.addNewSubCategoryClick()
        self.add_Subcat_name(Name)
        self.add_Category_name(Category)
        self.saveSubCatClick(Name, Category)