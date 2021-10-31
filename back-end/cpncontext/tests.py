from django.http import response
from django.test import TestCase, SimpleTestCase, TransactionTestCase
from rest_framework import status

class SimpleTest(TestCase):
    def test_cpncontext_page_status(self):
        response = self.client.get('http://127.0.0.1:8000/cpncontext/api/')
        self.assertEquals(response.status_code, status.HTTP_202_ACCEPTED)

    def test_save_new_context(self):
        response = self.client.post('http://127.0.0.1:8000/cpncontext/api/', data={'name': 'abc', 'content': 'abc', 'context_type': 'type1', 'description': 'abc'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
