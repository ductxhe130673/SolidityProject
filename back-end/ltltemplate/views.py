from django.core.exceptions import ValidationError
from rest_framework.serializers import Serializer
from rest_framework import exceptions
from .serializer import ltltemplateSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ltltemplate
from rest_framework.decorators import api_view
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
		try:
			if request.method == 'POST':
				serializerLTLTemplate = ltltemplateSerializer(data=request.data)
				if serializerLTLTemplate.is_valid():
					serializerLTLTemplate.save()
					return Response({"message":"Created"},status=status.HTTP_201_CREATED)
				return Response({"message":"Create fail!!!"},status=status.HTTP_400_BAD_REQUEST)
		except Exception:
			return Response({"message":"A"},status=status.HTTP_400_BAD_REQUEST)

	def put(self,request):
		try:
			if request.method == 'PUT':
				idLTLTemplate = request.data['id']
				ltltemplateById = ltltemplate.objects.get(id=idLTLTemplate)
				serializeUpdate = ltltemplateSerializer(instance=ltltemplateById, data=request.data)
				if serializeUpdate.is_valid():
					serializeUpdate.save()
					return Response({"message":"Update Successfully!!!"},status=status.HTTP_202_ACCEPTED)
				return Response({"message":"SmartConstract Data Invalid!!!"},status=status.HTTP_409_CONFLICT)
		except:
			return Response({"message":"Fail!!"},status=status.HTTP_404_NOT_FOUND)