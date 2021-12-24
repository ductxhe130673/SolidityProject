from django.core.exceptions import ValidationError
from rest_framework.serializers import Serializer
from rest_framework import exceptions
from .serializer import cpncontextSerializer, cpncontextSerializerPost
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import cpncontext
from cpncontext import dbcontext
from rest_framework.decorators import api_view
# Create your views here.


class cpncontextAPIView(APIView):

    # ----------GET ALL LTL properties-----------
    def get(self, request):
        try:
            if request.method == 'GET':
                cpnContext = cpncontext.objects.all()
                serializeLTLpro = cpncontextSerializer(cpnContext, many=True)
                return Response(serializeLTLpro.data, status=status.HTTP_202_ACCEPTED)
                # return render(request, 'ContextOfSmartContract.vue', {'cpncontext': serializeLTLpro}, status= status.HTTP_202_ACCEPTED)
        except Exception as e:
            return Response({"message": "Get Data Fail!!"}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        print(f'request {request}')
        print(f'request data {request.data}')
        try:
            if request.method == 'POST':
                serializeContext = cpncontextSerializerPost(data=request.data)
                if serializeContext.is_valid():
                    serializeContext.save()
                    return Response({"message": "Created"}, status=status.HTTP_201_CREATED)
                return Response({"message": "Create fail!!!"}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print("ERROR======", e)
            return Response({"message": "A"}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        # print('ID====',request.GET['cid'])
        print(f'request Put {request}')
        print(f'request PUT data {request.data}')
        try:
            if request.method == 'PUT':
                idContext = request.data['cid']
                print("ID======", idContext)
                contextById = cpncontext.objects.get(cid=idContext)

                serializeUpdate = cpncontextSerializer(
                    instance=contextById, data=request.data)
                if serializeUpdate.is_valid():
                    serializeUpdate.save()
                    return Response({"message": "Update Successfully!!!"}, status=status.HTTP_202_ACCEPTED)
                return Response({"message": "CPNContext Data Invalid!!!"}, status=status.HTTP_409_CONFLICT)
        except Exception as e:
            print('ERROR=====', e)
            return Response({"message": "Fail!!"}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request):
        try:
            if request.method == 'DELETE':
                idContextDelete = request.GET['cid']
                modify = dbcontext.modifyCheckedDetail(idContextDelete)
                contextDelete = cpncontext.objects.get(cid=idContextDelete)
                contextDelete.delete()
                return Response('Success', status=status.HTTP_200_OK)
        except Exception as e:
            print('ERROR====', e)
            return Response({"message": "Fail!!"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def getCPNcontextById(request):
    try:
        if request.method == 'GET':
            idCPN = request.GET['cid']
            cpncontextDB = cpncontext.objects.get(cid=idCPN)
            serialicpncontext = cpncontextSerializer(cpncontextDB)
            return Response(serialicpncontext.data, status=status.HTTP_200_OK)
    except Exception as e:
        print('ERROR====', e)
    return Response({"message": "Get CPNContext By ID Fail!!"}, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET'])
# def getCPNContextById(request):
#     try:
#         if request.method == 'GET':
#             sql = '''select * from soliditycpn.cpncontext where cid = %s'''
#         cursor = connection.cursor()
#         try:
#             print('ID====', request.GET['cid'])
#             cursor.execute(sql, [request.GET['cid']])
#             data = cursor.fetchall()
#             return Response(data, status=status.HTTP_200_OK)
#         except Exception as e:
# 			                  print('ERROR====', e)
#         cursor.close
#     except:
#         return Response({"message": "Get CPNContext By ID Fail!!"}, status=status.HTTP_400_BAD_REQUEST)
