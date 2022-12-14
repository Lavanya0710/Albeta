from selenium.webdriver.common.by import By

from Configurations.Base_class import Basefunc

#
# class LoginPage(Basefunc):
#     textbox_username_id = "input_email"
#     textbox_password_id = "input-password"
#     button_login_xpath = "//*[@id='card']/div/form/button"
#     button_logout_xpath = "/html/body/header/div/div/div/div[3]/ul/li[4]/a/i"
#
#     def __init__(self, driver):
#         super().__init__(driver)
#         self.driver = driver
#
#     def setUserName(self, username):
#         self.wait_presence_of_element_located(By.ID, self.textbox_username_id).clear()
#         self. wait_presence_of_element_located(By.ID, self.textbox_username_id).send_keys(username)
#
#     def setPassword(self, password):
#         self. wait_presence_of_element_located(By.ID, self.textbox_password_id).clear()
#         self. wait_presence_of_element_located(By.ID, self.textbox_password_id).send_keys(password)
#
#     def clickLogin(self):
#         self. wait_presence_of_element_located(By.XPATH, self.button_login_xpath).click()
#
#     def clickLogout(self):
#         self. wait_presence_of_element_located(By.XPATH, self.button_logout_xpath).click()


class LoginPage(Basefunc):
    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    # Locaters:
    User_Email_Txtbox_XPATH =  "//input[@ID='input_email']"
    User_Password_Txtbox_ID ="input-password"
    Login_Btn_XPATH="//button"

    def get_usr_email(self):
        return self.wait_presence_of_element_located(By.XPATH,self.User_Email_Txtbox_XPATH)

    def get_usr_password(self):
        return self.wait_presence_of_element_located(By.ID,self.User_Password_Txtbox_ID)

    def get_login_btn(self):
        return self.wait_presence_of_element_located(By.XPATH,self.Login_Btn_XPATH)

    def user_login_email(self,User_Email):
       self.get_usr_email().send_keys(User_Email)


    def user_login_password(self,User_Password):
        try:
            self.get_usr_password().send_keys(User_Password)
        except:
            print("Please provide appropriate data")
    def perform_click(self):
        self.get_login_btn().click()

    def login_page_credentials(self,User_Email,User_Password, URL):
        self.driver.get(URL)
        self.user_login_email(User_Email)
        self.user_login_password(User_Password)
        self.perform_click()