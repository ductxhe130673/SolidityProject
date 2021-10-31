from django.http import response
from django.test import TestCase, SimpleTestCase

class SimpleTest(SimpleTestCase):
    def test_cpncontext_page_status(self):
        response = self.client.get('cpncontext/')
        self.assertEquals(response.status_code, 200)