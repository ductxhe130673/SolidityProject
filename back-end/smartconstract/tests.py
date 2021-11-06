from django.test import TestCase, SimpleTestCase
from django.http import response
from rest_framework import status

class SimpleTest(TestCase):
    def test_smartcontract_get_all(self):
        response = self.client.get('http://127.0.0.1:8000/smartconstract/select-smart-contract/')
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    def test_create_new_smartcontract(self):
        response = self.client.post('http://127.0.0.1:8000/smartconstract/select-smart-contract/', data={'name': 'abc', 'type': 'new', 'content': 'abc', 'description': 'abc', 'aid': '1'}) 
        self.assertEqual(response.status_code, status.HTTP_201_CREATED) 

#    def test_update_smartcontract(self):
#        body={'name': 'abc', 'type': 'new', 'content': 'abc', 'description': 'abc', 'aid': '1'}
#        response = self.client.put('http://127.0.0.1:8000/smartconstract/select-smart-contract?id=1/', data=body) 
#        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED) 

#    def test_delete_smartcontract(self):
#        response = self.client.delete('http://127.0.0.1:8000/smartconstract/select-smart-contract?id=1/') 
#        self.assertEqual(response.status_code, status.HTTP_200_OK) 
# LOI
#    def test_insert_into_initialmarking(self):
#        response = self.client.post('http://127.0.0.1:8000/smartconstract/addnewinitialmarking',data={'num_user': '4', 'IM_type': 'new'}) 
#        self.assertEqual(response.status_code, status.HTTP_201_CREATED) 