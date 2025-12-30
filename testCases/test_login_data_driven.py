import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.readProperties import ReadConfig
from utilities.customLogger import CustomLogger
from utilities import ExcelUtils

class Test_002_Data_Driven_Login:
    baseURL = ReadConfig.getApplicationURL()
    path = ".\\testData\\LoginData.xlsx"

    logger = CustomLogger.setup_logger()

    @pytest.mark.regression
    def test_login(self,setup):
        self.logger.info("********** Test_002_Data_Driven_Login **********")
        self.logger.info("********** Verifying Data Driven Login Test **********")

        # Setup WebDriver
        self.driver = setup
        
        # Navigate to URL
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        
        # Read data from Excel
        self.rows = ExcelUtils.getRowCount(self.path, 'Sheet1')
        status = [] # create empty list variable

        for r in range(2, self.rows + 1):
            self.username = ExcelUtils.readData(self.path, 'Sheet1', r, 1)
            self.password = ExcelUtils.readData(self.path, 'Sheet1', r, 2)
            self.expected = ExcelUtils.readData(self.path, 'Sheet1', r, 3)
        
            # Perform Login
            self.lp.set_username(self.username)
            self.lp.set_password(self.password)
            self.lp.click_login()
            
            # Wait for Dashboard title
            # WebDriverWait(self.driver, 10).until(
            #     EC.title_contains("Dashboard")
            # )

            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            if act_title == exp_title:

                if self.expected == "Pass":
                    self.logger.info("********** Passed **********")
                    self.lp.click_logout()
                    status.append("Pass")   

                elif self.expected == "Fail":
                    self.logger.info("********** Failed **********")
                    self.lp.click_logout()
                    status.append("Fail")
            
            elif act_title != exp_title:

                if self.expected == "Pass":
                    self.logger.info("********** Failed **********")
                    status.append("Fail")

                elif self.expected == "Fail":
                    self.logger.info("********** Passed **********")
                    status.append("Pass")

        # Final Assertion
        if "Fail" not in status:
            self.logger.info("********** Data Driven Login Test Passed **********")
            self.driver.quit()
            assert True
        else:
            self.logger.info("********** Data Driven Login Test Failed **********")
            self.driver.quit()
            assert False
        
        self.logger.info("********** End of Data Driven Login Test **********")
        self.logger.info("********** Completed Test_002_Data_Driven_Login **********")
    