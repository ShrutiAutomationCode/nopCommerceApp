import pytest

from utilities.customLogger import LogGen
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig


class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getApplicationUserName()
    password = ReadConfig.getApplicationPassword()

    logger = LogGen().loggen()

    @pytest.mark.sanity
    def test_homepageTitle(self, setup):
        self.logger.info("***************Test_001_Login******************")
        self.logger.info("***************Verifying HomePage******************")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_Title = self.driver.title
        if act_Title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("*************** HomePage test cases passed ******************")

        else:
            self.driver.save_screenshot(".\\screenshots\\test_homepageTitle.png")
            self.driver.close()
            self.logger.error("*************** HomePage test cases failed ******************")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self, setup):
        self.logger.info("***************Test_001_Login******************")
        self.logger.info("***************Verifying LoginTest******************")
        self.driver = setup
        self.driver.implicitly_wait(1000)
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_Title = self.driver.title
        self.driver.save_screenshot(".\\screenshots\\" + "test_homepageTitle1.png")
        self.lp.clickLogout()
        self.driver.implicitly_wait(1000)
        if act_Title == "Dashboard / nopCommerce administration":
            assert True
            self.logger.info("*************** Login test cases Passed ******************")
            self.driver.close()

        else:
            self.driver.save_screenshot(".\\screenshots\\" + "test_homepageTitle.png")
            self.logger.error("*************** Login test cases failed ******************")
            self.driver.close()
            assert False
