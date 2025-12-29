import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AddCustomer:
    # Add customer page locators
    lnk_customers_menu_xpath = "//p[normalize-space()='Customers']"
    # //i[contains(@class,'right fas fa-angle-left')]"
    lnk_customers_menuitem_xpath = "//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    btn_addnew_xpath = "//a[@class='btn btn-primary']"
    
    txt_email_id_xpath = "//input[@id='Email']"
    txt_password_id_xpath = "//input[@id='Password']"
    txt_firstname_id_xpath = "//input[@id='FirstName']"
    txt_lastname_id_xpath = "//input[@id='LastName']"
    
    rdo_male_id = "Gender_Male"
    rdo_female_id = "Gender_Female"
    txt_company_name_id = "Company"
    chk_is_tax_exempt_id = "IsTaxExempt"
    
    txt_customer_roles_xpath = "//span[@class='select2-selection__rendered']"
    lstitem_administrators_xpath = "//li[contains(text(),'Administrators')]"
    lstitem_forum_moderators_xpath = "//li[contains(text(),'Forum Moderators')]"
    lstitem_guests_xpath = "//li[contains(text(),'Guests')]"
    lstitem_registered_xpath = "//li[contains(text(),'Registered')]"
    lstitem_vendors_xpath = "//li[contains(text(),'Vendors')]"
    
    drp_manager_of_vendor_id = "VendorId"
    # drptitem_vendor1_xpath = "//option[contains(text(),'Vendor 1')]"
    # drpitem_vendor2_xpath = "//option[contains(text(),'Vendor 2')]"
    
    chk_active_id = "Active"
    chk_customer_must_password_id = "MustChangePassword"
    txt_admin_comment_id = "AdminComment"
    
    btn_save_xpath = "//button[@name='save']"
    # msg_successfull_xpath = "//span[normalize-space()='The customer has been updated successfully.']"

    def __init__(self, driver):
        self.driver = driver

    def clickOnCustomersMenu(self):
        self.driver.find_element(By.XPATH, self.lnk_customers_menu_xpath).click()

    def clickOnCustomersMenuItem(self):
        self.driver.find_element(By.XPATH, self.lnk_customers_menuitem_xpath).click()

    def clickOnAddnew(self):
        self.driver.find_element(By.XPATH, self.btn_addnew_xpath).click()

    def setEmail(self, email):
        self.driver.find_element(By.XPATH, self.txt_email_id_xpath).send_keys(email)

    def setPassword(self, password):
        self.driver.find_element(By.XPATH, self.txt_password_id_xpath).send_keys(password)

    def setFirstName(self, fname):
        self.driver.find_element(By.XPATH, self.txt_firstname_id_xpath).send_keys(fname)

    def setLastName(self, lname):
        self.driver.find_element(By.XPATH, self.txt_lastname_id_xpath).send_keys(lname)

    def setGender(self, gender):
        if gender == 'Male':
            self.driver.find_element(By.ID, self.rdo_male_id).click()
        
        elif gender == 'Female':
            self.driver.find_element(By.ID, self.rdo_female_id).click()
        
        else:
            self.driver.find_element(By.ID, self.rdo_male_id).click()

    def setCompanyName(self, comname):
        self.driver.find_element(By.ID, self.txt_company_name_id).send_keys(comname)

    def setCustomerRoles(self, role):   
        self.driver.find_element(By.XPATH, self.txt_customer_roles_xpath).click()
        time.sleep(3)

        if role == 'Administrators':
            self.listitem = self.driver.find_element(By.XPATH, self.lstitem_administrators_xpath)

        elif role == 'Forum Moderators':
            self.listitem = self.driver.find_element(By.XPATH, self.lstitem_forum_moderators_xpath)

        elif role == 'Guests':
            time.sleep(3)

            # Click the delete button for the selected role
            self.driver.find_element(By.XPATH, "//span[@role='presentation'][normalize-space()='×']").click()
            self.listitem = self.driver.find_element(By.XPATH, self.lstitem_guests_xpath)

        elif role == 'Registered':
            self.listitem = self.driver.find_element(By.XPATH, self.lstitem_registered_xpath)

        elif role == 'Vendors':
            self.listitem = self.driver.find_element(By.XPATH, self.lstitem_vendors_xpath)

        else:
            self.listitem = self.driver.find_element(By.XPATH, self.lstitem_guests_xpath)

        self.listitem.click()
        # Click the list item using JavaScript executor to avoid issues with hidden elements or overlays
        # self.driver.execute_script("arguments[0].click();", self.listitem)
        time.sleep(3)

    def setManagerOfVendor(self, value):
        drp = Select(self.driver.find_element(By.ID, self.drp_manager_of_vendor_id))
        drp.select_by_visible_text(value)

    def setActive(self):
        self.driver.find_element(By.ID, self.chk_active_id).click()
    
    def setCustomerMustChangePassword(self):
        self.driver.find_element(By.ID, self.chk_customer_must_password_id).click()

    def setAdminComment(self, comment):
        self.driver.find_element(By.ID, self.txt_admin_comment_id).send_keys(comment)

    def clickOnSave(self):
        self.driver.find_element(By.XPATH, self.btn_save_xpath).click()

    # def getSuccessMessage(self):
    #     return self.driver.find_element(By.XPATH, self.msg_successfull_xpath).text
    
