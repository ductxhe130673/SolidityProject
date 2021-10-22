from MySQLdb._mysql import result
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import status
from .serializers import SerializerCheckedbatchsc
from .models import  Checkedbatchsc
from django.db import connection

# Create your views here.
         
class Listofcheckedtransactions(APIView):
    def get(self,request):
        try:
            if request.method == 'GET':
                sql = '''SELECT ch.bid,co.lastname,ch.checkedDate,ch.noSC FROM soliditycpn.checkedbatchsc ch join soliditycpn.contact co on ch.aid = co.aid'''
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
    def get(self,request):
        try:
            if request.method == 'GET':
                sql = '''select c.lastname, lt.name, con.name, ch.noSC, ch.checkedDate, ch.status, ch.LTLformula, ch.result from
                        soliditycpn.checkedbatchsc ch join soliditycpn.contact c on ch.aid = c.aid
                        join soliditycpn.ltltemplate lt on ch.lteid = lt.lteid
                        join soliditycpn.cpncontext con on ch.cid = con.cid 
                        where ch.bid = %s'''
            cursor = connection.cursor()
            try:
                cursor.execute(sql,[request.GET['id']] )
                data = cursor.fetchall()
                return Response(data, status=status.HTTP_200_OK)
            except Exception as e:
                cursor.close
        except:
            return Response({"message": "Get Data Fail!!"}, status=status.HTTP_400_BAD_REQUEST)


