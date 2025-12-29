import time
import pytest
from pageObjects.AddCustomerPage import AddCustomer
from pageObjects.CustomerSearchPage import SearchCustomer
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import CustomLogger
from selenium.webdriver.common.by import By

class Test_004_SearchCustomerByEmail:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    # logger setup
    logger = CustomLogger.setup_logger()

    @pytest.mark.regression
    def test_searchCustomerByEmail(self, setup):
        self.logger.info("********** Test_004_SearchCustomerByEmail **********")

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

        self.logger.info("********** Searching Customer by Email ID **********")

        self.searchcust = SearchCustomer(self.driver)
        self.searchcust.setEmail("steve_gates@nopCommerce.com")
        self.searchcust.clickSearch()
        time.sleep(3)
        status = self.searchcust.searchCustomerByEmail("steve_gates@nopCommerce.com")
        assert True == status
        self.logger.info("********** Search Customer by Email ID Successful **********")
        self.driver.close()
        self.logger.info("********** Test_004_SearchCustomerByEmail Finished **********")

