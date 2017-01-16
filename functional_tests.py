from selenium import webdriver
import unittest

class HighscoresTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_that_result_list_is_presented_correctly(self):
        self.browser.get('http://localhost:8000/highscores/regions/')
        li = self.browser.find_elements_by_tag_name('li')
        self.assertEqual(len(li), 13)


if __name__ == '__main__':
    unittest.main(warnings='ignore')
