import re
from django.core.exceptions import ValidationError
from rest_framework.serializers import Serializer
from rest_framework import exceptions
from .serializer import cpncontextSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import cpncontext
from rest_framework.decorators import api_view
from django.shortcuts import render
# Create your views here.

class cpncontextAPIView(APIView):

	    #----------GET ALL LTL properties-----------
	def get(self,request):
		print("abc", request)
		try:
			if request.method == 'GET':
				cpnContext = cpncontext.objects.all()
				serializeLTLpro = cpncontextSerializer(cpnContext, many=True)
				return Response(serializeLTLpro.data, status=status.HTTP_202_ACCEPTED)
				# return render(request, 'ContextOfSmartContract.vue', {'cpncontext': serializeLTLpro}, status= status.HTTP_202_ACCEPTED)
		except Exception as e: 
			print("ERROR=====",e)
			return Response({"message": "Get Data Fail!!"}, status=status.HTTP_400_BAD_REQUEST)
	
	def post(self,request):
		try:
			if request.method == 'POST':
				serializeContext = cpncontextSerializer(data=request.data)
				if serializeContext.is_valid():
					serializeContext.save()
					return Response({"message":"Created"},status=status.HTTP_201_CREATED)
				return Response({"message":"Create fail!!!"},status=status.HTTP_400_BAD_REQUEST)
		except Exception:
			return Response({"message":"A"},status=status.HTTP_400_BAD_REQUEST)
	
	def put(self,request):
		try:
			if request.method == 'PUT':
				idContext = request.data['id']
				contextById = cpncontext.objects.get(id=idContext)
				serializeUpdate = cpncontextSerializer(instance=contextById, data=request.data)
				if serializeUpdate.is_valid():
					serializeUpdate.save()
					return Response({"message":"Update Successfully!!!"},status=status.HTTP_202_ACCEPTED)
				return Response({"message":"SmartConstract Data Invalid!!!"},status=status.HTTP_409_CONFLICT)
		except:
			return Response({"message":"Fail!!"},status=status.HTTP_404_NOT_FOUND)
	
	def delete(self,request):
		try:
			if request.method =='DELETE':
				idContextDelete = request.data['id']
				contextDelete = cpncontext.objects.get(id=idContextDelete)
				contextDelete.delete()
				return Response('Success',status=status.HTTP_200_OK)
		except:
			return Response({"message":"Fail!!"},status=status.HTTP_400_BAD_REQUEST)
