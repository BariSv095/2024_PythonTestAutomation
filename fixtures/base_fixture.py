import os.path
import time
import unittest

from faker import Faker
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

from fixtures.pages import Pages
from lib.base_methods import BaseMethods
from lib.browser import get_browser
from menus.main_menu import MainMenu
from menus.user_menu import UserMenu
from pages.login import LoginPage
from tests import DEFAULT_WAIT, DOMAIN, PROJECT_DIR


class BrowserFixture(unittest.TestCase, BaseMethods):
    def setUp(self):
        self.browser = get_browser()
        self.wait = WebDriverWait(self.browser, DEFAULT_WAIT)
        self.fake_data = Faker()

    def tearDown(self):
        if ((hasattr(self._outcome, 'errors') and self._outcome.errors[1][1]) or
                (self._outcome.result.failures and self._outcome.result.failures[0][1])):

            test_results = os.path.join(PROJECT_DIR, 'test_results')

            if not os.path.exists(test_results):
                os.mkdir(test_results)

            pieces = self._outcome.result.current_test_id.split('.')
            test_name = pieces.pop()

            folder_path = test_results
            for piece in pieces:
                folder_path = os.path.join(folder_path, piece)
                if not os.path.exists(folder_path):
                    os.mkdir(folder_path)

            screenshot_path = os.path.join(folder_path, f'{test_name}.png')
            self.browser.save_screenshot(screenshot_path)


            page_src_path = os.path.join(folder_path, f'{test_name}.html')
            file = open(page_src_path,'w')
            file.write(self.browser.page_source)
            file.close()

        self.browser.quit()


class HRMBaseFixture(BrowserFixture):
    def setUp(self):
        super().setUp()
        # self.browser.get(DOMAIN)
        self.page = Pages(self.browser)
        self.user_menu = UserMenu(self.browser)
        self.main_menu = MainMenu(self.browser)


class AdminLoginFixture(unittest.TestCase):
    welcome_message_element = (By.ID, 'welcome')

    def setUp(self):
        # 1. Initialize the browser without a manual path.
        # Selenium Manager handles the version matching automatically.

        self.browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.browser.get('http://hrm-online.portnov.com/')
        self.login_page = LoginPage(self.browser)
        self.login_page.authenticate()
        self.wait = WebDriverWait(self.browser, 5)
        self.wait.until(EC.presence_of_element_located(self.welcome_message_element))

        def tearDown(self):
            self.browser.quit()

        # super().setUp()
        #
        # self.page.login_page.go_to_page()
        # self.page.login_page.authenticate()
        # self.page.login_page.wait_for_successful_login()
        # self.wait.until(EC.presence_of_element_located(self.welcome_message_element))
        # OR
        # self.wait.until(EC.url_contains('/pim/viewEmployeeList'))