from django.http import response
from django.test import TestCase
from django.test.testcases import SimpleTestCase

# Create your tests here.
class SimpleTest(SimpleTestCase):
    def test_transaction_page_status(self):
        response = self.client.get('select-sc/')
        self.assertEquals(response.status_code, 200)
