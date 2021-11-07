from django.test import TestCase, SimpleTestCase
from django.http import response
from rest_framework import status

class SimpleTest(TestCase):
    def test_smartcontract_get_all(self):
        response = self.client.get('http://127.0.0.1:8000/smartconstract/select-smart-contract/')
        self.assertEqual(response.status_code,status.HTTP_200_OK)

# TESTCASE CHAY NHUNG POSTMAN CHUA CHAY
    def test_create_new_smartcontract(self):
        response = self.client.post('http://127.0.0.1:8000/smartconstract/select-smart-contract/', data={'name': 'abc', 'type': 'new', 'content': 'abc', 'description': 'abc', 'aid': '1'}) 
        self.assertEqual(response.status_code, status.HTTP_201_CREATED) 

# LOI
#    def test_update_smartcontract(self):
#        body={'name': 'abc', 'type': 'new', 'content': 'abc', 'description': 'abc', 'aid': '1'}
#        response = self.client.put('http://127.0.0.1:8000/smartconstract/select-smart-contract?id=1/', data=body) 
#        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED) 

# LOI
#    def test_delete_smartcontract(self):
#         data={'id': '40'}
#         response = self.client.delete('http://127.0.0.1:8000/smartconstract/select-smart-contract/',data=data) 
#         self.assertEqual(response.status_code, status.HTTP_200_OK) 


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

# LOI TESTCASE  , CON BEN POSTMAN CHAY OKE
#    def test_insert_into_initialmarking(self):
#        data={'num_user': '4', 'IM_type': 'new'}
#        response = self.client.post('http://127.0.0.1:8000/smartconstract/addnewinitialmarking',data=data) 
#        self.assertEqual(response.status_code, status.HTTP_201_CREATED)         

# LOI TESTCASE  , CON BEN POSTMAN CHAY OKE
#    def test_insertIntoFunctions(self):
#        data = {'fun_name':'test','sender_from' : '1','sender_to' : '10'} 
#        response =  self.client.post('http://127.0.0.1:8000/smartconstract/addnewimfunction',data=data)
#        self.assertEqual(response.status_code, status.HTTP_201_CREATED)  