from django.shortcuts import render
from .serializer import GetIMArgumentSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import IMArgument
from rest_framework.decorators import api_view
from django.db import connection
# Create your views here.
# moi class la 1 man ?


class GetAllArgument(APIView):
    def get(self, request):
        try:
            if request.method == 'GET':
                sql = '''SELECT * FROM soliditycpn.argument'''
            cursor = connection.cursor()
            try:
                cursor.execute(sql)
                data = cursor.fetchall()
                return Response(data, status=status.HTTP_200_OK)
            except Exception as e:
                cursor.close
        except:
            return Response({"message": "Get Data Fail!!"}, status=status.HTTP_400_BAD_REQUEST)


class GetArgumentBySmartContractIDandFuntionID(APIView):
    def get(self, request):
        try:
            if request.method == 'GET':
                sql = '''select ssc.sid ,ssc.name as smartcontract_name,sft.fid ,sft.name as function_name,
                         sag.id,sag.name as argument_name
                         from soliditycpn.smartcontract ssc join soliditycpn.functions sft 
                         join soliditycpn.argument sag on sft.fid = sag.fid
                         on ssc.sid=sft.sid
                         where ssc.sid=%s and sft.fid = %s'''
            cursor = connection.cursor()
            try:
                cursor.execute(sql, [request.GET['sid']], [request.GET['fid']])
                data = cursor.fetchall()
                return Response(data, status=status.HTTP_200_OK)
            except Exception as e:
                cursor.close
        except:
            return Response({"message": "Get Data Fail!!"}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        try:
            if request.method == 'POST':
                sql = '''INSERT INTO IMArgument (arg_name,IMfrom,IMto,imfid) VALUES (%s,%s,%s,%s)'''
                cursor = connection.cursor()
                # chua lay dc du lieu tu session, dang fix du lieu mac dinh
                multi = [
                    ("IMArgument1", 20, 35, 1),
                    ("IMArgument2", 30, 45, 2),
                    ("IMArgument3", 21, 42, 3),
                ]
            try:
                cursor.executemany(sql, multi)
                data = cursor.fetchall()
                return Response(data, status=status.HTTP_200_OK)
            except Exception as e:
                cursor.close
        except:
            return Response({"message": "Get Data Fail!!"}, status=status.HTTP_400_BAD_REQUEST)


# insert into
# mycursor = mydb.cursor()
# sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# val = ("Michelle", "Blue Village")
# mycursor.execute(sql, val)
# mydb.commit()
