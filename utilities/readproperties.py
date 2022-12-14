import configparser

config = configparser.RawConfigParser()
path = 'C:\\Users\\getma\\PycharmProjects\\Alb\\Configurations\\Config.ini'
config.read(path)

class ReadConfig():
    @staticmethod
    def getApplicationURL():
        url=config.get('casual','baseURL')
        return url
    @staticmethod
    def getUseremail():
        User_Name = config.get('casual', 'useremail')
        return User_Name
    @staticmethod
    def getPassword():
        Password = config.get('casual', 'password')
        return Password
