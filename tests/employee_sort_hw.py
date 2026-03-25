import unittest
import time
from selenium.webdriver.common.by import By
from fixtures.base_fixture import AdminLoginFixture


class EmployeeSort(AdminLoginFixture):
    first_middle_name_header = (By.XPATH, '//*[@id="resultTable"]//th[3]/a')

    def test_sort_by_first_middle_name(self):
        browser = self.browser
        browser.find_element(*self.first_middle_name_header).click()
        time.sleep(2)

        list_of_name_elements = browser.find_elements(By.XPATH, '//table[@id="resultTable"]/tbody/tr/td[3]/a')
        previous = ''
        for name_element in list_of_name_elements:
            self.assertLessEqual(previous, name_element.text)
            previous = name_element.text




if __name__ == '__main__':
    unittest.main()
