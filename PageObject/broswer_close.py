from Configurations.Base_class import Basefunc


class Close_browser(Basefunc):
    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    def browser_close(self):
        self.driver.close()