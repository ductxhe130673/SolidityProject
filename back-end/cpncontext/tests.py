from django.http import response
from django.test import TestCase, SimpleTestCase
from rest_framework import status

class SimpleTest(SimpleTestCase):
    def test_cpncontext_page_status(self):
        response = self.client.get('/api/')
        self.assertEquals(response.status_code, status.HTTP_202_ACCEPTED)

    def test_save_new_context(self):
        response = self.client.post('/api/', data={'name': 'abc', 'content': 'abc', 'context_type': 'type1', 'description': 'abc'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
