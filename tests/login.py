import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver_path = r'C:\Users\BariSv01\.wdm\drivers\chromedriver\win64\144.0.7559.133\chromedriver-win32\chromedriver.exe'
        self.browser = webdriver.Chrome(service=Service(self.driver_path))
        self.browser.get('http://demoqa.com/login')

    def tearDown(self):
        self.browser.quit()

    def test_valid_login(self):
        browser = self.browser
        browser.find_element(By.ID, 'userName').send_keys('EllieSky')
        browser.find_element(By.ID, 'password').send_keys('Password1!')
        browser.find_element(By.ID, 'login').location_once_scrolled_into_view
        browser.find_element(By.ID, 'login').click()

    def test_invalid_password(self):
        pass

    def test_no_password(self):        pass


if __name__ == '__main__':
    unittest.main()
