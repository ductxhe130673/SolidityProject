from django.test import TestCase
from django.http import request, response
from django.test import TestCase,SimpleTestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse

# Create your tests here.
#class SimpleTests(SimpleTestCase):
#   def test_list_checked_transactions(self):
        # lay dg dan ,thanh cong thi tra ve 200
        #response = self.client.get('/select-sc/listofcheckedtransactions/')
        #self.assertEquals(response.status_code, 200)
        # python manage.py test Transactions

#       response = self.client.get(reverse('get1'))
#        self.assertEqual(response.status_code, status.HTTP_200_OK)

#    def test_check_reentrancy_details(self):
        # lay dg dan ,thanh cong thi tra ve 200
#        response = self.client.get('/select-sc/checkreentrancydetail/id=1')
#        self.assertEquals(response.status_code, 200)
        # python manage.py test Transactions