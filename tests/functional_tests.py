from selenium import webdriver
import unittest

"""
Check that Django is installed.
This test below has to confirm that we cas spin up Django's developmet server, 
and see it serving up a web page, in our web browser.
"""


# browser = webdriver.Firefox()
# browser.get('http://localhost:8000')
#
# assert 'Pur Beurre' in browser.title

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Checkout Home Page
        self.browser.get('http://localhost:8000')

        # Title
        self.assertIn('Pur Beurre', self.browser.title)
        # self.fail('Finish the test')


if __name__ == '__main__':
    unittest.main(warnings='ignore')
