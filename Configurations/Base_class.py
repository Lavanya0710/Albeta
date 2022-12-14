from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains as AC


class Basefunc():
    def __init__(self, driver):
        self.driver = driver

    def wait_presence_of_element_located(self, id_type, ele_id):
        wait = WebDriverWait(self.driver, 10)
        return wait.until(EC.presence_of_element_located((id_type, ele_id)))

    def wait_presence_of_all_elements_located(self, id_type, ele_id):
        wait = WebDriverWait(self.driver, 60)
        return wait.until(EC.presence_of_all_elements_located((id_type, ele_id)))

    def move_to_particular_element(self, elefunc):
        do = AC(self.driver)
        return do.move_to_element(elefunc)
