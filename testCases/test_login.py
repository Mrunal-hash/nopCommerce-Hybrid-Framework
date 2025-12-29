import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.readProperties import ReadConfig
from utilities.customLogger import CustomLogger

class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    logger = CustomLogger.setup_logger()

    @pytest.mark.regression
    def test_home_page_title(self,setup):

        # Logging
        self.logger.info("********** Test_001_Login **********")
        self.logger.info("********** Verifying Home Page Title **********")
        
        # Setup WebDriver
        self.driver = setup
        
        # Navigate to URL
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        
        # Assertion
        if act_title == "nopCommerce demo store. Login":
            self.driver.close()
            assert True
            self.logger.info("********** Home Page Title Test Passed **********")
        
        else:   
            self.driver.save_screenshot(".\\screenshots\\" + "test_home_page_title.png")
            self.driver.close()
            assert False
            self.logger.error("********** Home Page Title Test Failed **********")  

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_login(self,setup):

        self.logger.info("********** Verifying Login Test **********")

        # Setup WebDriver
        self.driver = setup
        
        # Navigate to URL
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        
        # Perform Login
        self.lp.set_username(self.username)
        self.lp.set_password(self.password)
        self.lp.click_login()
        
        # Wait for Dashboard title
        WebDriverWait(self.driver, 10).until(
            EC.title_contains("Dashboard")
        )
        act_title = self.driver.title
        
        # Assertion
        if act_title == "Dashboard / nopCommerce administration":
            self.driver.close()
            assert True
            self.logger.info("********** Login Test Passed **********")
        
        else:
            self.driver.save_screenshot(".\\screenshots\\" + "test_login.png")
            self.driver.close()
            assert False
            self.logger.error("********** Login Test Failed **********")