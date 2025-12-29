import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SearchCustomer:
    # Search customer page locators
    txt_email_id = 'SearchEmail'
    txt_firstname_id = 'SearchFirstName'
    txt_lastname_id = 'SearchLastName'
    btn_search_id = 'search-customers'

    tbl_search_results_xpath = "//table[@id='customers-grid']"
    tbl_rows_xpath = "//table[@id='customers-grid']//tbody/tr"
    tbl_columns_xpath = "//table[@id='customers-grid']//tbody/tr/td"

    def __init__(self, driver):
        self.driver = driver

    def setEmail(self, email):
        self.driver.find_element(By.ID, self.txt_email_id).clear()
        self.driver.find_element(By.ID, self.txt_email_id).send_keys(email)
        
    def setFirstName(self, fname):
        self.driver.find_element(By.ID, self.txt_firstname_id).clear()
        self.driver.find_element(By.ID, self.txt_firstname_id).send_keys(fname)

    def setLastName(self, lname):
        self.driver.find_element(By.ID, self.txt_lastname_id).clear()
        self.driver.find_element(By.ID, self.txt_lastname_id).send_keys(lname)

    def clickSearch(self):
        self.driver.find_element(By.ID, self.btn_search_id).click()
        time.sleep(3)

    def getNoOfRows(self):
        return len(self.driver.find_elements(By.XPATH, self.tbl_rows_xpath))

    def getNoOfColumns(self):
        return len(self.driver.find_elements(By.XPATH, self.tbl_columns_xpath))
    
    def searchCustomerByEmail(self, email):
        flag = False
        # Search customer by email
        for r in range(1, self.getNoOfRows() + 1):
            # Find the table and extract email from the current row
            table = self.driver.find_element(By.XPATH, self.tbl_search_results_xpath)
            # Find the email in the current row
            emailid = table.find_element(By.XPATH, "//table[@id='customers-grid']//tbody/tr[" + str(r) + "]/td[2]").text
            # print(emailid)
            if emailid == email:
                flag = True
                break
        return flag
    
    def searchCustomerByName(self, Name):
        flag = False
        # Search customer by Name
        for r in range(1, self.getNoOfRows() + 1):
            # Find the table and extract name from the current row
            table = self.driver.find_element(By.XPATH, self.tbl_search_results_xpath)
            # Find the name in the current row
            name = table.find_element(By.XPATH, "//table[@id='customers-grid']//tbody/tr[" + str(r) + "]/td[3]").text
            # print(name)
            if name == Name:
                flag = True
                break
        return flag