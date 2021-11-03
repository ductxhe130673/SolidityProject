from django.http import response
from django.test import TestCase
from rest_framework import status

class SimpleTest(TestCase):

    #test get all template
    def test_get_all_template(self):
        response = self.client.get('http://127.0.0.1:8000/ltltemplate/api/')
        self.assertEquals(response.status_code, 202)