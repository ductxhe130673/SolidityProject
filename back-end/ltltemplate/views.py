from django.core.exceptions import ValidationError
from rest_framework.serializers import Serializer
from rest_framework import exceptions
from .serializer import ltltemplateSerializer, ltltemplateSerializerPost
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ltltemplate
from rest_framework.decorators import api_view
from ltltemplate import dbcontext
# Create your views here.

class ltltemplateAPIView(APIView):

	    #----------GET ALL LTL properties-----------
	def get(self,request):
		try:
			if request.method == 'GET':
				LTLproDB = ltltemplate.objects.all()
				serializeLTLpro = ltltemplateSerializer(LTLproDB, many=True)
				return Response(serializeLTLpro.data, status=status.HTTP_202_ACCEPTED)
		except Exception as e: 
			return Response({"message": "Get Data Fail!!"}, status=status.HTTP_400_BAD_REQUEST)			
	
	# def getCTById(request):
	# 	try:
	# 		if request.method == 'GET':
	# 			idClient = request.GET['id']
	# 			ContextFrontDBById = ltltemplate.objects.get(id=idClient)
	# 			serializeContext = ltltemplateSerializer(ContextFrontDBById)
	# 			return Response(serializeContext.data,status=status.HTTP_200_OK)
	# 	except:
	# 		return Response({"message":"Get Data Fail!!"},status=status.HTTP_400_BAD_REQUEST)
	
	def post(self,request):
		print(f'request {request}')
		print(f'request data {request.data}')
		try:
			if request.method == 'POST':
				serializerLTLTemplate = ltltemplateSerializerPost(data=request.data)
				if serializerLTLTemplate.is_valid():
					serializerLTLTemplate.save()
					return Response({"message":"Created"},status=status.HTTP_201_CREATED)
				return Response(serializerLTLTemplate.errors,status=status.HTTP_400_BAD_REQUEST)
		except Exception as e:
			print("ERROR====", e)
			return Response({"message":"A"},status=status.HTTP_400_BAD_REQUEST)

	def put(self,request):
		print(f'request Put {request}')
		print(f'request PUT data {request.data}')
		try:
			if request.method == 'PUT':
				idLTLTemplate = request.data['lteid']
				ltltemplateById = ltltemplate.objects.get(lteid=idLTLTemplate)
				serializeUpdate = ltltemplateSerializer(instance=ltltemplateById, data=request.data)
				if serializeUpdate.is_valid():
					serializeUpdate.save()
					return Response({"message":"Update Successfully!!!"},status=status.HTTP_202_ACCEPTED)
				return Response({"message":"LTLTemplate Data Invalid!!!"},status=status.HTTP_409_CONFLICT)
		except Exception as e:
			print("ERROR=====",e)
			return Response({"message":"Fail!!"},status=status.HTTP_404_NOT_FOUND)

	def delete(self,request):
		try:
			if request.method =='DELETE':
				idLTLDelete = request.GET['lteid']
				modify = dbcontext.modifyCheckedDetail(idLTLDelete)
				ltltemplateDelete = ltltemplate.objects.get(lteid=idLTLDelete)
				ltltemplateDelete.delete()
				return Response('Success',status=status.HTTP_200_OK)
		except Exception as e:
			print('ERROR====',e)
			return Response({"message":"Fail!!"},status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def getLTLTemplateById(request):
    try:
        if request.method == 'GET':
            idLTL = request.GET['lteid']
            ltltemplateDB = ltltemplate.objects.get(lteid=idLTL)
            serialiltltemplate = ltltemplateSerializer(ltltemplateDB)
            return Response(serialiltltemplate.data, status=status.HTTP_200_OK)
    except Exception as e:
		    print('ERROR====', e)
    return Response({"message": "Get LTL Template By ID Fail!!"}, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET'])
# def getLTLTemplateById(request):
#     try:
#         if request.method == 'GET':
#             sql = '''select * from soliditycpn.ltltemplate where lteid = %s'''
#         cursor = connection.cursor()
#         try:
#             print('ID====', request.GET['lteid'])
#             cursor.execute(sql, [request.GET['lteid']])
#             data = cursor.fetchall()
#             return Response(data, status=status.HTTP_200_OK)
#         except Exception as e:
# 			                  print('ERROR====', e)
#         cursor.close
#     except:
#         return Response({"message": "Get LTL Template By ID Fail!!"}, status=status.HTTP_400_BAD_REQUEST)	
