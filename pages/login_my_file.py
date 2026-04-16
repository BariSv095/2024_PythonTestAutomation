

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    welcome_message_element = (By.ID, 'welcome')
    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(browser, 10)

    def authenticate(self):

        browser = self.browser
        browser.find_element(By.ID, 'txtUsername').send_keys('admin')
        browser.find_element(By.ID, 'txtPassword').send_keys('password')
        browser.find_element(By.ID, 'btnLogin').click()
        self.wait = WebDriverWait(browser, 5)
        self.wait.until(EC.presence_of_element_located(self.welcome_message_element))

