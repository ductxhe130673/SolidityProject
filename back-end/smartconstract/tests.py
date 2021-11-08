from django.test import TestCase,TransactionTestCase
from django.http import response
from rest_framework import status
#import pytest

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


class TestInsertInitialMarking(TransactionTestCase):
   # test new insert into initialmanrking
    def test_insert_into_initialmarking(self):
       response = self.client.post(
           'http://127.0.0.1:8000/smartconstract/addnewinitialmarking',
           data={'num_user': '5', 'IM_type': 'new'},
           content_type='application/json')
       self.assertEquals(response.status_code, status.HTTP_201_CREATED)

    # test new insert into balance
    def test_insert_into_Balance(self):
        response = self.client.post(
            'http://127.0.0.1:8000/smartconstract/addnewbalance',
            data={'balanceType': 'Fixed',  'blfrom': ' ', 'blto': ' ','blvalue': '14', 'blrange': ' '},
            content_type='application/json')
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

    # test new insert into IMFunction
    def test_insertIntoIMFunctions(self):
       response = self.client.post(
                                   'http://127.0.0.1:8000/smartconstract/addnewimfunction',
                                   data={'fun_name': 'test', 'sender_from': '1', 'sender_to': '10'},
                                   content_type='application/json')
       self.assertEquals(response.status_code, status.HTTP_201_CREATED)

    # test new insert into IMArgument
    def test_insertIntoIMArgument(self):
       response = self.client.post(
                                   'http://127.0.0.1:8000/smartconstract/addnewimargument',
                                   data={
                                       'arg_name': 'test', 'IMfrom': '1', 'IMto': '10'},
                                   content_type='application/json')
       self.assertEquals(response.status_code, status.HTTP_201_CREATED)

    # test new insert into CheckedBashSC
    def test_insertIntoCheckBashSC(self):
       response = self.client.post(
                                   'http://127.0.0.1:8000/smartconstract/addnewcheckedbatchsc',
                                   data={
                                       'aid': '1', 'lteid': '1', 'cid': '1', 'noSC': '4',
                                        'status': '1', 'LTLformula': 'test', 'result': 'test'},
                                   content_type='application/json')
       self.assertEquals(response.status_code, status.HTTP_201_CREATED)

    # test new insert into CheckedSmartContractDetail
    def test_insertIntoCheckSmartContractDetail(self):
       response = self.client.post(
                                   'http://127.0.0.1:8000/smartconstract/addnewcheckedsmartcontractdetail',
                                   data={'sid': '1'},content_type='application/json')
       self.assertEquals(response.status_code, status.HTTP_201_CREATED)

class TestInsertLNAFile(TestCase):
    # test new insert into lnafile
    def test_insert_into_lnafile(self):
        response = self.client.post(
            'http://127.0.0.1:8000/smartconstract/addnewlnafile',
            data={'hcpnfile': 'D:\\Solidity\\SolidityNew\\SolidityProject\\scripts\\XMLfile\\finnal_model.lna', 
            'propfile': 'D:\\Solidity\\SolidityNew\\SolidityProject\\scripts\\XMLfile\\finnal_model.prop.lna'},
            content_type='application/json')
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

# DANG LOI
# class TestGetSCById(TestCase):
#     # BEN  VIEWS.PY  DANG DUNG SERIALIZER
#     # test get smartcontract by smartcontract ID
#     def test_get_sc_by_Id(self):
#          response =  self.client.get('http://127.0.0.1:8000/smartconstract/scbyid?id=2')
#          self.assertEqual(response.status_code, status.HTTP_200_OK)

class TestGetGlobalvariablebySCId(TestCase):
    # test get global variable by smartcontract ID
    def test_get_globalvariable_by_SCId(self):
        response =  self.client.get('http://127.0.0.1:8000/smartconstract/globalvarialbe?id=4')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class TestGetFunctionBySCId(TestCase):
    # test get function by smartcontract ID
    def test_get_function_by_SCId(self):
        response =  self.client.get('http://127.0.0.1:8000/smartconstract/getfunction?id=4')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class TestGetLocalValByFunctionId(TestCase):
    # test get global variable by function ID
    def test_get_localVar_by_FunctionID(self):
        response =  self.client.get('http://127.0.0.1:8000/smartconstract/localvariable?id=1')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class TestGetFunctionVarArguBySCId(TestCase):
    # test get Function, Variable,Argument by smartcontract ID
    def test_getFunctionVarArgu_by_SCId(self):
        response =  self.client.get('http://127.0.0.1:8000/smartconstract/getvariablefunctionargu?id=1')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class TestGetArgumentByFunctionId(TestCase):
    # test get argument by function ID
    def test_getArgument_by_FunctionId(self):
        response =  self.client.get('http://127.0.0.1:8000/smartconstract/getargubyfunctionid?id=4')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)