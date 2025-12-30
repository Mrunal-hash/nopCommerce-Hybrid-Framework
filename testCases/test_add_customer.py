import pytest
import time
from pageObjects.AddCustomerPage import AddCustomer
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import CustomLogger
from selenium.webdriver.common.by import By
import string
import random


def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))

class Test_003_AddCustomer:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    # logger setup
    logger = CustomLogger.setup_logger()

    @pytest.mark.sanity
    def test_addCustomer(self,setup):
        self.logger.info("********** Test_003_AddCustomer **********")

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
        
        # Add Customer
        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomersMenu()
        self.addcust.clickOnCustomersMenuItem()
        self.addcust.clickOnAddnew()

        self.logger.info("********** Providing Customer Info **********")

        self.email = random_generator() + "@gmail.com"
        self.addcust.setEmail(self.email)
        self.addcust.setPassword("test123")
        self.addcust.setFirstName("John")
        self.addcust.setLastName("Doe")
        self.addcust.setGender("Male")
        self.addcust.setCompanyName("ABC Pvt Ltd")
        self.addcust.setCustomerRoles("Registered")
        self.addcust.setManagerOfVendor("Vendor 1")
        self.addcust.setAdminComment("This is for testing.........")
        self.addcust.clickOnSave()
        self.logger.info("********** Saving Customer Info **********")

        self.msg = self.driver.find_element(By.TAG_NAME, "body").text
        # print(self.msg)
        
        if "The new customer has been added successfully." in self.msg:
            assert True
            self.logger.info("********** Add Customer Test Passed **********")
            self.driver.quit()
        
        else:
            self.driver.save_screenshot(".\\screenshots\\" + "test_addCustomer.png")
            self.logger.error("********** Add Customer Test Failed **********")
            assert False
            self.driver.quit()
        
        self.logger.info("********** Ending Test_003_AddCustomer **********")


