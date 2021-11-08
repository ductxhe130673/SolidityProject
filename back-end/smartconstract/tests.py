from django.test import TestCase
from django.http import response
from rest_framework import status


class SimpleTest(TestCase):
    # test get all smartcontract
    def test_smartcontract_get_all(self):
        response = self.client.get(
            'http://127.0.0.1:8000/smartconstract/select-smart-contract')
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
        self.assertEquals(response.status_code, status.HTTP_202_ACCEPTED)

    # test delete smartcontract
    def test_delete_smartcontract(self):
        response = self.client.delete(
            'http://127.0.0.1:8000/smartconstract/select-smart-contract?id=6')


class TestFinalInsert(TestCase):
    # test new insert into initialmanrking
    def test_insert_into_initialmarking(self):
        response = self.client.post(
            'http://127.0.0.1:8000/smartconstract/addnewinitialmarking',
            data={'num_user': '5', 'IM_type': 'new'},
            content_type='application/json')
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

class TestInsertIntoBalance(TestCase):
    # test new insert into balance
    def test_insert_into_Balance(self):
        response = self.client.post(
            'http://127.0.0.1:8000/smartconstract/addnewbalance',
            data={'balanceType': 'Fixed', 'blvalue': '14', 'blfrom': '', 'blto': '', 'blrange': ''},
            content_type='application/json')
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

class TestInsertIntoIMFunction(TestCase):
    # LOI TESTCASE  , CON BEN POSTMAN CHAY OKE
    def test_insertIntoIMFunctions(self):
        response = self.client.post(
                                    'http://127.0.0.1:8000/smartconstract/addnewimfunction',
                                    data={
                                        'fun_name': 'test', 'sender_from': '1', 'sender_to': '10'},
                                    content_type='application/json')
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

    def test_insertIntoIMArgument(self):
        response = self.client.post(
                                    'http://127.0.0.1:8000/smartconstract/addnewimargument',
                                    data={
                                        'arg_name': 'test', 'IMfrom': '1', 'IMto': '10'},
                                    content_type='application/json')
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

class TestInsertLNAFile(TestCase):
    # test new insert into lnafile
    def test_insert_into_lnafile(self):
        response = self.client.post(
            'http://127.0.0.1:8000/smartconstract/addnewlnafile',
            data={'hcpnfile': '"D:\Document\CapStone\CapstoneProject\SolidityProject\scripts\XMLfile\finnal_model.lna', 
            'propfile': 'D:\Document\CapStone\CapstoneProject\SolidityProject\scripts\XMLfile\finnal_model.prop.lna'},
            content_type='application/json')
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

# class TestAllGetFunction(TestCase):
# LOI 400 , DO DUNG SERIALIER ??????
#    def test_get_sc_by_Id(self):
#        data = {'id':'4'}
#        response =  self.client.get('http://127.0.0.1:8000/smartconstract/scbyid',data=data)
#        self.assertEqual(response.status_code, status.HTTP_200_OK)

#    def test_get_globalvariable_by_SCId(self):
#        data = {'id':'4'}
#        response =  self.client.get('http://127.0.0.1:8000/smartconstract/globalvarialbe',data=data)
#        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

#    def test_get_function_by_SCId(self):
#        data = {'id':'4'}
#        response =  self.client.get('http://127.0.0.1:8000/smartconstract/getfunction',data=data)
#        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

#    def test_get_localVar_by_FunctionID(self):
#        data = {'id':'1'}
#        response =  self.client.get('http://127.0.0.1:8000/smartconstract/localvariable',data=data)
#        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

#    def test_getFunctionVarArgu_by_SCId(self):
#        data = {'id':'1'}
#        response =  self.client.get('http://127.0.0.1:8000/smartconstract/getvariablefunctionargu',data=data)
#       self.assertEqual(response.status_code, status.HTTP_201_CREATED)

#    def test_getArgument_by_FunctionId(self):
#        data = {'id':'4'}
#        response =  self.client.get('http://127.0.0.1:8000/smartconstract/getargubyfunctionid',data=data)
#        self.assertEqual(response.status_code, status.HTTP_201_CREATED)