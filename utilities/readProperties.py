import configparser

config = configparser.RawConfigParser()
config.read(".\\configurations\\config.ini")

class ReadConfig:

    @staticmethod
    def getApplicationURL():
        url = config.get('credentials', 'baseURL')
        return url

    @staticmethod
    def getUsername():
        username = config.get('credentials', 'username')
        return username

    @staticmethod
    def getPassword():
        password = config.get('credentials', 'password')
        return password

