from warnings import catch_warnings
from MySQLdb._mysql import result
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import status
from .serializers import SerializerCheckedbatchsc
from .models import Checkedbatchsc
from django.db import connection

# Create your views here.


class Listofcheckedtransactions(APIView):
    def get(self, request):
        try:
            if request.method == 'GET':
                sql = '''select cb.bid,co.lastname,cb.checkedDate,cb.noSC from soliditycpn.checkedbatchsc cb join soliditycpn.contact co on cb.aid = co.id'''
            cursor = connection.cursor()
            try:
                cursor.execute(sql)
                data = cursor.fetchall()
                return Response(data, status=status.HTTP_200_OK)
            except Exception as e:
                cursor.close
        except:
            return Response({"message": "Get Data Fail!!"}, status=status.HTTP_400_BAD_REQUEST)


class Checkreentrancydetail(APIView):
    def get(self, request):
        try:
            if request.method == 'GET':
                sql = '''select cb.bid,co.lastname,cb.checkedDate,cb.noSC,cb.result
                    from soliditycpn.checkedbatchsc cb join soliditycpn.contact co on cb.aid = co.id
                    where cb.bid = %s'''
            cursor = connection.cursor()
            try:
                cursor.execute(sql, [request.GET['id']])
                data = cursor.fetchall()
                return Response(data, status=status.HTTP_200_OK)
            except Exception as e:
                cursor.close
        except:
            return Response({"message": "Get Data Fail!!"}, status=status.HTTP_400_BAD_REQUEST)
