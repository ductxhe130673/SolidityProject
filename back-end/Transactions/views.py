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

    def post(self,request):
        try:
            if request.method == 'POST':
                serializeTransaction = SerializerCheckedbatchsc(data=request.data)
                if serializeTransaction.is_valid():
                    serializeTransaction.save()
                    return Response({"message":"Created"},status=status.HTTP_201_CREATED)
                return Response({"message":"Create fail!!!"},status=status.HTTP_400_BAD_REQUEST)
        except Exception:
            return Response({"message":"A"},status=status.HTTP_400_BAD_REQUEST)
    
    def put(self,request):
        try:
            if request.method == 'PUT':
                idTransaction = request.data['id']    
                transactionByID = Checkedbatchsc.objects.get(id=idTransaction)
                serializeUpdate = SerializerCheckedbatchsc(instance=transactionByID,data=request.data)
                if serializeUpdate.is_valid():
                    serializeUpdate.save()
                    return Response({"message":"Update Successfully!!!"},status=status.HTTP_202_ACCEPTED)
                return Response({"message":"SmartConstract Data Invalid!!!"},status=status.HTTP_409_CONFLICT)
        except:
            return Response({"message":"Fail!!"},status=status.HTTP_404_NOT_FOUND)

    def delate(self,request):
        try:
            if request.method == 'DELETE':
                idTran = request.GET['id']
                transactionById = Checkedbatchsc.objects.get(id=idTran)
                transactionById.delete()
                return Response('Success',status=status.HTTP_200_OK)
        except:
            return Response({"message":"Fail!!"},status=status.HTTP_400_BAD_REQUEST)

class Checkreentrancydetail(APIView):
    def get(self,request):
        try:
            if request.method == 'GET':
                sql = '''select result from soliditycpn.checkedbatchsc where bid = %s'''
            cursor = connection.cursor()
            try:
                cursor.execute(sql,[request.GET['id']] )
                data = cursor.fetchall()
                return Response(data, status=status.HTTP_200_OK)
            except Exception as e:
                cursor.close
        except:
            return Response({"message": "Get Data Fail!!"}, status=status.HTTP_400_BAD_REQUEST)


