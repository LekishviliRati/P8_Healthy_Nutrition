import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class LoginTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_login(self):
        # Check if Django is working
        self.browser.get('http://localhost:8000')
        self.browser.maximize_window()
        self.assertIn('Pur Beurre', self.browser.title)
        time.sleep(3)

        # Check if Visitor succeed to reach login page.
        login_page = self.browser.find_element_by_id('Connexion')
        login_page.click()
        time.sleep(3)

        # Fill connexion fields and enter
        email_box = self.browser.find_element_by_id('id_username')
        email_box.send_keys('jean.martin@gmail.com')
        time.sleep(2)
        password_box = self.browser.find_element_by_id('id_password')
        password_box.send_keys('Django_74')
        time.sleep(2)
        password_box.send_keys(Keys.ENTER)
        time.sleep(7)


if __name__ == '__main__':
    unittest.main(warnings='ignore')
