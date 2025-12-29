import time
import pytest
from pageObjects.AddCustomerPage import AddCustomer
from pageObjects.CustomerSearchPage import SearchCustomer
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import CustomLogger
from selenium.webdriver.common.by import By

class Test_005_SearchCustomerByName:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    # logger setup
    logger = CustomLogger.setup_logger()

    @pytest.mark.regression
    def test_searchCustomerByName(self, setup):
        self.logger.info("********** Test_005_SearchCustomerByName **********")

        # Setup WebDriver
        self.driver = setup
        
        # Navigate to URL
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        
        # Perform Login
        self.lp.set_username(self.username)
        self.lp.set_password(self.password)
        self.lp.click_login()

        self.logger.info("********** Login Successful **********")
        
        # Go to Customer Search Page
        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomersMenu()
        self.addcust.clickOnCustomersMenuItem()

        self.logger.info("********** Searching Customer by Name **********")

        self.searchcust = SearchCustomer(self.driver)
        self.searchcust.setFirstName("John")
        self.searchcust.setLastName("Smith")
        self.searchcust.clickSearch()
        time.sleep(3)
        status = self.searchcust.searchCustomerByName("John Smith")
        assert True == status
        self.logger.info("********** Search Customer by Name Successful **********")
        self.driver.close()
        self.logger.info("********** Test_005_SearchCustomerByName Finished **********")

