from django.test import TestCase, TransactionTestCase
from rest_framework import response, status
# Create your tests here.


class TestGetContactByAccountId(TestCase):
    # test get contact by account id
    def test_get_contact_by_accountId(self):
        response = self.client.get(
            'http://127.0.0.1:8000/auth/getcontactbyaid?id=1')
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)


class TestGetAvartarByAccountId(TestCase):
    # test get avartar by account id
    def test_get_avatar_by_aid(self):
        response = self.client.get(
            'http://127.0.0.1:8000/auth/getavatarbyaid?id=1')
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

class TestCheckEmailExisted(TestCase):
    # test check email existed
    def test_check_email_existed(self):
        response = self.client.get(
            'http://127.0.0.1:8000/auth/checkemailexited?email=vinhhq@fpt.edu.vna')
        self.assertEquals(response.data , "Valid")    
        self.assertEquals(response.status_code, status.HTTP_200_OK)        


class TestInsertMethods(TransactionTestCase):
        # test update contact information
        def test_update_contact_info(self):
            response = self.client.put(
                'http://127.0.0.1:8000/auth/updatecontactbyaid',
                data={'firstname': 'leo', 'lastname': 'messi', 'email': 'messi@gmail.com',
                      'phone': '0987654321', 'birthDate': '1998-09-09',
                      'avartar': 'D:\\Solidity\\SolidityNew\\SolidityProject\\scripts\\image\\index2.jpeg', 'address': 'Paris', 'aid': '7'},
                content_type='application/json')
            self.assertEquals(response.status_code, status.HTTP_201_CREATED)

    # test insert into contact
    # def test_insert_into_contact(self):
    #     response = self.client.post(
    #         'http://127.0.0.1:8000/auth/insertintocontact',
    #         data={'email': 'test'}, content_type='application/json')
    #     self.assertEquals(response.status_code, status.HTTP_201_CREATED)

class TestPostMethods(TransactionTestCase):
    # test register method
    def testPostRegister(self):
        response = self.client.post('http://127.0.0.1:8000/auth/register/',
                                    data={
                                        'username': 'testuser3', 'password': 'testpassword', 'role': 'user'},
                                    content_type='application/json')
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

    # test login method
    def testPostLogin(self):
        response = self.client.post('http://127.0.0.1:8000/auth/login',
                                    data={
                                        'username': 'xuanduc', 'password': 'admin'},
                                    content_type='application/json')
        self.assertEquals(response.status_code, status.HTTP_200_OK)
