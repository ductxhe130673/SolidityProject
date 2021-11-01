from django.http import response
from django.test import TestCase
from django.test.testcases import SimpleTestCase

# Create your tests here.
class SimpleTest(TestCase):
    def test_transaction_page_status(self):
        response = self.client.get('http://127.0.0.1:8000/select-sc/listofcheckedtransactions/')
        self.assertEquals(response.status_code, 200)
        