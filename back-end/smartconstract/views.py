from .serializer import GetSmartConstractSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Smartcontract
from rest_framework.decorators import api_view
from django.db import connection
# Create your views here.


class SmartConstractAPIView(APIView):
    def get(self, request):
        try:
            if request.method == 'GET':
                smartConstractDB = Smartcontract.objects.all()
                serialiSmartConstract = GetSmartConstractSerializer(
                    smartConstractDB, many=True)
                return Response(serialiSmartConstract.data, status=status.HTTP_200_OK)
        except:
            return Response({"message": "Get Data Fail!!"}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        try:
            if request.method == 'POST':
                serializeClient = GetSmartConstractSerializer(
                    data=request.data)
                if serializeClient.is_valid():
                    serializeClient.save()
                    return Response({"message": "Created"}, status=status.HTTP_201_CREATED)
                return Response({"message": "Create fail!!!"}, status=status.HTTP_400_BAD_REQUEST)
        except Exception:
            return Response({"message": "A"}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        try:
            if request.method == 'PUT':
                idClient = request.data['id']
                SmartConstractByID = Smartcontract.objects.get(id=idClient)
                serializeUpdate = GetSmartConstractSerializer(
                    instance=SmartConstractByID, data=request.data)
                if serializeUpdate.is_valid():
                    serializeUpdate.save()
                    return Response({"message": "Update Successfully!!!"}, status=status.HTTP_202_ACCEPTED)
                return Response({"message": "SmartConstract Data Invalid!!!"}, status=status.HTTP_409_CONFLICT)
        except:
            return Response({"message": "Fail!!"}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request):
        try:
            if request.method == 'DELETE':
                idClient = request.GET['id']
                SmartConstractByID = Smartcontract.objects.get(id=idClient)
                SmartConstractByID.delete()
                return Response('Success', status=status.HTTP_200_OK)
        except:
            return Response({"message": "Fail!!"}, status=status.HTTP_400_BAD_REQUEST)




@api_view(['GET'])
def getScById(request):
    try:
        if request.method == 'GET':
            idClient = request.GET['id']
            smartConstractDB = Smartcontract.objects.get(id=idClient)
            serialiSmartConstract = GetSmartConstractSerializer(
                smartConstractDB)
            return Response(serialiSmartConstract.data, status=status.HTTP_200_OK)
    except:
        return Response({"message": "Get Data Fail!!"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def getFunctionAndArgumentBySmartcontractId(request):
    try:
        if request.method == 'GET':
            sql = '''select ssc.sid ,ssc.name as smartcontract_name,sft.fid as fucntion_id,sft.name as function_name,
                     sag.id as argument_id,sag.name as argument_name
                     from soliditycpn.smartcontract ssc join soliditycpn.functions sft 
                     join soliditycpn.argument sag on sft.fid = sag.fid
                     on ssc.sid=sft.sid
                     where ssc.sid = %s'''
        cursor = connection.cursor()
        try:
            cursor.execute(sql, [request.GET['id']])
            data = cursor.fetchall()
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            cursor.close
    except:
        return Response({"message": "Get Data Fail!!"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def getAllFunctionAndArgumentBySmartcontractId(request):
    try:
        if request.method == 'GET':
            sql = '''select ssc.sid ,ssc.name as smartcontract_name,sft.fid as fucntion_id,sft.name as function_name,
                     sag.id as argument_id,sag.name as argument_name
                     from soliditycpn.smartcontract ssc join soliditycpn.functions sft 
                     join soliditycpn.argument sag on sft.fid = sag.fid
                     on ssc.sid=sft.sid'''
        cursor = connection.cursor()
        try:
            cursor.execute(sql)
            data = cursor.fetchall()
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            cursor.close
    except:
        return Response({"message": "Get Data Fail!!"}, status=status.HTTP_400_BAD_REQUEST)
