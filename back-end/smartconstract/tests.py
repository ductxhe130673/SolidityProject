from django.test import TestCase
from django.http import response
from rest_framework import status


class SimpleTest(TestCase):
    # test get all smartcontract
    def test_smartcontract_get_all(self):
        response = self.client.get('http://127.0.0.1:8000/smartconstract/select-smart-contract')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # test create new smartcontract
    def test_create_new_smartcontract(self):
        response = self.client.post('http://127.0.0.1:8000/smartconstract/select-smart-contract',
                                    data={
                                        'name': 'abc', 'type': 'new', 'content': 'abc', 'description': 'abc', 'aid': '1'},
                                    content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # test update smartcontract
    def test_update_smartcontract(self):
        response = self.client.put('http://127.0.0.1:8000/smartconstract/select-smart-contract',
                                   data={
                                       'id': '6', 'name': 'abc', 'type': 'new', 'content': 'abc', 'description': 'abc', 'aid': '1'},
                                   content_type='application/json')
        self.assertEquals(response.status_code, 202)
    # test delete smartcontract

    def test_delete_smartcontract(self):
        response = self.client.delete(
            'http://127.0.0.1:8000/smartconstract/select-smart-contract?id=6')

class TestFinalInsert(TestCase):
    # test new insert into initialmanrking
    def test_insert_into_initialmarking(self):
        response = self.client.post('http://127.0.0.1:8000/smartconstract/addnewinitialmarking',
                                    data={'num_user': '5', 'IM_type': 'new'},
                                    content_type='application/json')
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
