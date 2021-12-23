from django.test import TestCase, TransactionTestCase
from rest_framework import response, status
# Create your tests here.


class TestContactGetMethods(TestCase):
    # test get contact by account id
    def test_get_contact_by_accountId(self):
        response = self.client.get(
            'http://127.0.0.1:8000/auth/getcontactbyaid?id=1')
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

class TestContactGetMethods1(TestCase):
    # test get avartar by account id
    def test_get_avatar_by_aid(self):
        response = self.client.get(
            'http://127.0.0.1:8000/auth/getavatarbyaid?id=1')
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)


# class TestInsertMethods(TransactionTestCase):
#     # test update contact information
#     def test_update_contact_info(self):
#         response = self.client.put(
#             'http://127.0.0.1:8000/auth/updatecontactbyaid',
#             data={'firstname': 'leo', 'lastname': 'messi', 'email': 'messi@gmail.com',
#                   'phone': '0987654321', 'birthDate': '1998-09-09',
#                   'avartar': 'D:\\Solidity\\SolidityNew\\SolidityProject\\scripts\\image\\index2.jpeg', 'address': 'Paris', 'aid': '6'},
#             content_type='application/json')
#         self.assertEquals(response.status_code, status.HTTP_201_CREATED)

    # test insert into contact
    # def test_insert_into_contact(self):
    #     response = self.client.post(
    #         'http://127.0.0.1:8000/auth/insertintocontact',
    #         data={'email': 'test'}, content_type='application/json')
    #     self.assertEquals(response.status_code, status.HTTP_201_CREATED)        
