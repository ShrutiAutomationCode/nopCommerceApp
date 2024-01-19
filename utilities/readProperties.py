import configparser

"""
here we have configparser package which have RawConfigParser() class 
which will read config.ini file's 
so we have create an object of RawConfigParser() to read ini file with read method
"""

config = configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")

"""
Now question here is I have read the ini file now how we can fetch the data of ini file
so we need to create a class and we need to create a method for each variable of ini file
To access object without creating any object so will do method as static.
"""


class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url = config.get("common Info", "baseURL")
        return url

    @staticmethod
    def getApplicationUserName():
        username = config.get("common Info", "username")
        return username

    @staticmethod
    def getApplicationPassword():
        password = config.get("common Info", "password")
        return password
