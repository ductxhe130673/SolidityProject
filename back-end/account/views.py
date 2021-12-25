from rest_framework import serializers, status, permissions
from rest_framework.decorators import api_view
from .serializers import RegisterSerializer, LoginSerializer, sendEmail
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Contact
from account import dbcontext
# import base64
# import json
# Create your views here.


class RegisterView(APIView):
    sendEmail = sendEmail
    serializer_class = RegisterSerializer

    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class LoginAPIView(APIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class LogoutAPIView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response('oke', status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response("not oke ", status=status.HTTP_400_BAD_REQUEST)


class Test(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        return Response('oke')

@api_view(['GET'])
def getContactByAccountId(request):
    try:
        resData = dbcontext.getContactByAid(request.GET['id'])
        if resData is None:
            return Response({"message": "Something went wrong !!!"}, status=status.HTTP_400_BAD_REQUEST)
        return Response(resData, status=status.HTTP_201_CREATED)
    except Exception as e:
        print("ERROR ==== ", e)
        return Response({"message": "Get Contact by aid failed !!!"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def getAvatarAccountId(request):
    # CHANGE THIS BEFORE RUNNING
    path = "D:\Demo\SolidityProject\scripts\image"
    try:
        # GET AID 
        aId = request.GET['id']
        # SET IMAGE PATH AND RETURN IT
        imagePath = path +"\\"+ aId + ".jpg"  
        resData = dbcontext.read_blob(request.GET['id'], imagePath)
        # print(imagePath)
        if resData is not True:
            return Response({"message": "Something went wrong !!!"}, status=status.HTTP_400_BAD_REQUEST)
        return Response(imagePath, status=status.HTTP_201_CREATED)
    except Exception as e:
        print("ERROR ==== ", e)
        return Response({"message": "Get Avatar by aid failed !!!"}, status=status.HTTP_400_BAD_REQUEST)

# return image as json
# dbcontext.read_blob(
#             request.GET['id'], imagePath)
#         with open(imagePath, mode='rb') as file:
#             img = file.read()
#         resData['img'] = base64.encodebytes(img).decode('utf-8')

@api_view(['POST'])
def insertIntoContact(request):
    try:
        resData = dbcontext.InsertIntoContact(request.data['email'])
        if resData is None:
            return Response({"message":"Fail to Add New Contact !!!"},status=status.HTTP_400_BAD_REQUEST)
        return Response(resData,status=status.HTTP_201_CREATED)    
    except Exception as e:
        print("ERROR ==== ",e)
        return Response({"message":"Fail !!!"},status=status.HTTP_400_BAD_REQUEST)    

@api_view(['PUT'])
def updateContactInfor(request):
    try:
        resData = dbcontext.UpdateContactInfor(request.data['firstname'],request.data['lastname'],request.data['email'],request.data['phone'],request.data['birthDate'],request.data['avartar'],request.data['address'],request.data['aid'])
        if resData is None:
            return Response({"message":"Fail to Update Contact Information !!!"},status=status.HTTP_400_BAD_REQUEST)
        return Response(resData,status=status.HTTP_201_CREATED)    
    except Exception as e:
        print("ERROR ==== ",e)
        return Response({"message":"Fail !!!"},status=status.HTTP_400_BAD_REQUEST)            