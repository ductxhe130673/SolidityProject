from django.http import response
from django.test import TestCase
from rest_framework import status

class SimpleTest(TestCase):
    #Test get all cpncontext
    def test_cpncontext_page_status(self):
        response = self.client.get('http://127.0.0.1:8000/cpncontext/api/')
        self.assertEquals(response.status_code, status.HTTP_202_ACCEPTED)

    #Test insert new cpncontext
    def test_save_new_context(self):
        response = self.client.post('http://127.0.0.1:8000/cpncontext/api/', data={'name': 'abc', 'content': 'abc', 'context_type': 'type1', 'description': 'abc'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    #Test update cpncontext information by id
    # def test_update_cpncontext_byid(self):
    #     response = self.client.put('http://127.0.0.1:8000/cpncontext/api/', data={'cid': '3', 'name': 'EtherGame Context', 'content': 'This is Content 3', 'context_type': 'type4', 'description': 'This is description'})
    #     self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)

    #Test delete cpncontext
    def test_delete_cpncontext(self):
        response = self.client.delete('http://127.0.0.1:8000/cpncontext/api/', data={'id': '4'})
        self.assertEquals(response.status_code, status.HTTP_200_OK)
