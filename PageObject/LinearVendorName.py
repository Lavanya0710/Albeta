import time

import chromedriver_autoinstaller

from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service(chromedriver_autoinstaller.install()))

driver.get("https://gitcustomer.albertapayments.com/")
driver.maximize_window()
time.sleep(1)

textbox_username_id = "input_email"
textbox_password_id = "input-password"
button_login_xpath = "//*[@id='card']/div/form/button"
button_logout_xpath = "/html/body/header/div/div/div/div[3]/ul/li[4]/a/i"
vendor_mod_xpath = "//a[@class='nav-link sub text-uppercase']"
txt_vendor_name_xpath = "//input[@id='vendor_name']"

driver.find_element(By.ID, textbox_username_id).send_keys('harikt@gmail.com')
time.sleep(1)
driver.find_element(By.ID, textbox_password_id).send_keys('123456')
time.sleep(1)
driver.find_element(By.XPATH, button_login_xpath).click()
time.sleep(0.1)
driver.find_element(By.XPATH, vendor_mod_xpath).click()
time.sleep(0.1)
v_s_name = 'test'
driver.find_element(By.XPATH, txt_vendor_name_xpath).send_keys(v_s_name)
time.sleep(0.1)
ele = driver.find_elements(By.XPATH, "//tr//td[3]")
print(len(ele))
v_cnt = 0
for i in ele:
    print(i.text)
    v_cnt+=1
    if i.text == v_s_name:
        v_c = v_cnt
        pass
        # sel = '//tr[',v_cnt,']//td[1]'
# print("//tr["v_cnt"]//td[1]")
time.sleep(1)
ab = driver.find_element(By.XPATH,'//tr[' + str(v_c) + ']//td[1]')
ab.click()
# '//tr[2]//td[1]'
time.sleep(4)
