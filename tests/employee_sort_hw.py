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

        has_pagination = browser.find_elements(By.CLASS_NAME, 'paging')

        is_last_page = False
        previous = ''
        while not is_last_page:
            list_of_name_elements = browser.find_elements(By.XPATH, '//table[@id="resultTable"]/tbody/tr/td[3]/a')
            for name_element in list_of_name_elements:
                self.assertLessEqual(previous, name_element.text)
                previous = name_element.text

            if has_pagination:
                browser.find_element(By.CSS_SELECTOR, '.next>a').click()
                pagination_text = browser.find_element(By. CSS_SELECTOR, '.paging .desc').text
                pagination_pieces = pagination_text.split(' of ')
                is_last_page = pagination_pieces[-1] in pagination_pieces[0]





if __name__ == '__main__':
    unittest.main()
