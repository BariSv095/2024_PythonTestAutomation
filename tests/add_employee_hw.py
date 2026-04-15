import unittest
from telnetlib import EC

from faker import Faker
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from fixtures.base_fixture import AdminLoginFixture


class AddEmployee(AdminLoginFixture):
    def add_employee(self):
        # create new employee/create first and last name, save generated user's ID
        browser = self.browser
        fake = Faker()
        first_name = fake.first_name()
        last_name = fake.last_name()

        browser.find_element(By.ID, 'btnAdd').click()
        browser.find_element(By.ID, 'firstName').send_keys(first_name)
        browser.find_element(By.ID, 'lastName').send_keys(last_name)
        new_employee_id = browser.find_element(By.ID, 'employeeId').get_attribute('value')
        return first_name, last_name, new_employee_id


    def create_employee_credentials(self, first_name,new_employee_id):
        # check 'Create login details' and create user name and user's password
        browser = self.browser
        fake = Faker()
        user_name = f"{first_name}{new_employee_id}"
        password = fake.password()
        browser.find_element(By.ID, 'chkLogin').click()
        browser.find_element(By.ID, 'user_name').send_keys(user_name)
        browser.find_element(By.ID, 'user_password').send_keys(password)
        browser.find_element(By.ID, 're_password').send_keys(password)
        browser.find_element(By.ID, 'btnSave').click()
        return user_name, password

    def verify_new_employee_added(self, first_name, last_name, new_employee_id):
        browser = self.browser
        self.assertEqual(first_name, browser.find_element(By.ID, 'personal_txtEmpFirstName').get_attribute('value'))
        self.assertEqual(last_name, browser.find_element(By.ID, 'personal_txtEmpLastName').get_attribute('value'))
        self.assertEqual(new_employee_id, browser.find_element(By.ID, 'personal_txtEmployeeId').get_attribute('value'))
        self.assertIn(new_employee_id, browser.current_url)

    def test_new_employee_added(self):
        first_name, last_name, new_employee_id = self.add_employee()
        user_name, password = self.create_employee_credentials(first_name, new_employee_id)
        self.verify_new_employee_added(first_name, last_name, new_employee_id)

    def logout(self):
        browser = self.browser
        browser.find_element(By.ID, 'welcome').click()
        browser.find_element(By.LINK_TEXT, 'logout').click()

    def login_as_new_employee(self, user_name, password, first_name):
        browser = self.browser
        browser.find_element(By.ID, 'txtUsername').send_keys(user_name)
        browser.find_element(By.ID, 'txtPassword').send_keys(password)
        browser.find_element(By.ID, 'btnLogin').click()
        self.wait = WebDriverWait(browser, 5)
        self.assertIn(first_name, browser.find_element(By.ID, 'welcome').text)
    def test_login_as_new_employee(self):
        browser = self.browser
        first_name, last_name, new_employee_id = self.add_employee()
        user_name, password = self.create_employee_credentials(first_name, new_employee_id)
        self.verify_new_employee_added(first_name, last_name, new_employee_id)
        browser.find_element(By.ID, 'txtUsername').send_keys(user_name)
        browser.find_element(By.ID, 'txtPassword').send_keys(password)
        browser.find_element(By.ID, 'btnLogin').click()
        self.wait = WebDriverWait(browser, 5)
        self.assertIn(first_name, browser.find_element(By.ID, 'welcome').text)


if __name__ == '__main__':
    unittest.main()
