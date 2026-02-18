import time
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver_path = r'C:\Users\BariSv01\.wdm\drivers\chromedriver\win64\144.0.7559.133\chromedriver-win32\chromedriver.exe'
        self.browser = webdriver.Chrome(service=Service(self.driver_path))
        self.browser.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')


    def tearDown(self):
        self.browser.quit()

    def test_valid_login(self):
        browser = self.browser
        browser.implicitly_wait(10)
        browser.find_element(By.NAME, 'username').send_keys('Admin')
        browser.find_element(By.NAME, 'password').send_keys('admin123')
        browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

        time.sleep(3)
        #after login we want to check the expected username is displayed
        self.assertEqual(browser.find_element(By.CSS_SELECTOR, '.oxd-userdropdown-name').text, 'manda user')
        self.assertIn('/dashboard/index', browser.current_url)


    def test_invalid_password(self):
        browser = self.browser
        browser.implicitly_wait(10)
        browser.find_element(By.NAME, 'username').send_keys('Admin')
        browser.find_element(By.NAME, 'password').send_keys('aDmin123')
        browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

        self.assertEqual( browser.find_element(By.CSS_SELECTOR, '.oxd-alert-content-text').text, 'Invalid credentials',)


    def test_no_password(self):
        browser = self.browser
        browser.find_element(By.ID, 'userName').send_keys('EllieSky')
        browser.find_element(By.ID, 'login').location_once_scrolled_into_view
        browser.find_element(By.ID, 'login').click()
        class_attr_value = browser.find_element(By.ID, 'password').get_attribute('class')
        self.assertIn('is-invalid', class_attr_value)


    def test_no_username(self):
        browser = self.browser
        browser.find_element(By.ID, 'login').location_once_scrolled_into_view
        browser.find_element(By.ID, 'login').click()
        class_attr_value = browser.find_element(By.ID, 'username').get_attribute('class')
        self.assertIn('is-invalid', class_attr_value)

if __name__ == '__main__':
    unittest.main()
