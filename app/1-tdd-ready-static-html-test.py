from lib.app import app
from pyquery import PyQuery as pq
import unittest

class TddReadyStaticHtml(unittest.TestCase):

    def setUp(self):
        self.driver = app.test_client(self) 
        self.response = self.driver.get('/', content_type='html/text')       

    def test_home_page_can_be_reached(self):        
        self.assertEqual(self.response.status_code, 200)

    def test_expected_greetings(self):        
        page = pq(self.response.data)
        
        self.assertEqual(page('#greetings').text(), 'Hello, Service BC :)')


if __name__ == '__main__':
    unittest.main()