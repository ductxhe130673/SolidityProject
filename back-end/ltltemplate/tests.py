from django.http import response
from django.test import TestCase
from rest_framework import status


class SimpleTest(TestCase):

    # test get all template
    def test_get_all_template(self):
        response = self.client.get('http://127.0.0.1:8000/ltltemplate/api')
        self.assertEquals(response.status_code, 202)

    # test create new template
    def test_create_new_template(self):
        response = self.client.post('http://127.0.0.1:8000/ltltemplate/api',
                                    data={"name": "new template", "formula": "new formula",
                                          "template_type": "new type", "description": "This is description", "aid": "1"},
                                    content_type='application/json')
        self.assertEquals(response.status_code, 201)

    # test update template information
    def test_update_template(self):
        response = self.client.put('http://127.0.0.1:8000/ltltemplate/api',
                                   data={"lteid": "12", "name": "new template", "formula": "new formula",
                                         "template_type": "new type", "description": "This is description", "aid": "1"},
                                   content_type='application/json')
        self.assertEqual(response.status_code, 202)

    # test delete template
    def test_delete_template(self):
        response = self.client.delete(
            'http://127.0.0.1:8000/ltltemplate/api?lteid=12')
        self.assertEquals(response.status_code, 200)

# Test cac ham GET
class TestGetLTLTemplateById(TestCase):
    # test get ltltemplate by ltltemplate ID
    def test_get_ltltemplate_by_Id(self):
         response =  self.client.get('http://127.0.0.1:8000/ltltemplate/ltltemplatebyid?lteid=2')
         self.assertEqual(response.status_code, status.HTTP_200_OK)