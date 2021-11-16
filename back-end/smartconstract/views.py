from .serializer import GetSmartConstractSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers, status
from .models import Smartcontract
from rest_framework.decorators import api_view
from smartconstract import dbcontext
# Create your views here.


class SmartConstractAPIView(APIView):
    def get(self, request):
        try:
            if request.method == 'GET':
                smartConstractDB = Smartcontract.objects.all()
                serialiSmartConstract = GetSmartConstractSerializer(smartConstractDB, many=True)
                return Response(serialiSmartConstract.data, status=status.HTTP_200_OK)
        except Exception as e:
            print("ERROR====", e)
            return Response({"message": "Get Data Fail!!"}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        try:
            if request.method == 'POST':
                serializeClient = GetSmartConstractSerializer(data=request.data)
                if serializeClient.is_valid():
                    serializeClient.save()
                    return Response({"message": "Created"}, status=status.HTTP_201_CREATED)
                return Response({"message": "Create fail!!!"}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print('ERROR======',e)
            return Response({"message": "A"}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        print(f'request Put {request}')
        print(f'request PUT data {request.data}')
        try:
            if request.method == 'PUT':
                idClient = request.data['id']
                SmartConstractByID = Smartcontract.objects.get(sid=idClient)
                serializeUpdate = GetSmartConstractSerializer(
                    instance=SmartConstractByID, data=request.data)
                if serializeUpdate.is_valid():
                    serializeUpdate.save()
                    return Response({"message": "Update Successfully!!!"}, status=status.HTTP_202_ACCEPTED)
                return Response({"message": "SmartConstract Data Invalid!!!"}, status=status.HTTP_409_CONFLICT)
        except:
            return Response({"message": "Fail!!"}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request):
        print('DELETE', request.GET['id'])
        try:
            if request.method == 'DELETE':
                idClient = request.GET['id']

                modifyGlo = dbcontext.updateGlobalVariable(idClient)
                modifyFunction = dbcontext.updateFunction(idClient)
                deleteDetail = dbcontext.deleteCheckedDetail(idClient)
                if modifyGlo is None or modifyFunction is None or deleteDetail is None:
                    print("Not ready to delete")
                SmartConstractByID = Smartcontract.objects.get(sid=idClient)
                SmartConstractByID.delete()
                return Response('Success', status=status.HTTP_200_OK)
        except:
            return Response({"message": "Fail!!"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def getScById(request):
    try:
        if request.method == 'GET':
            idClient = request.GET['id']
            smartConstractDB = Smartcontract.objects.get(sid=idClient)
            serialiSmartConstract = GetSmartConstractSerializer(
                smartConstractDB)
            return Response(serialiSmartConstract.data, status=status.HTTP_200_OK)
    except Exception as e:
        print('ERROR !!!', e)
        return Response({"message": "Get Data Fail!!"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def getGBByScId(request):
    try:
        resData = dbcontext.getGlobalVarBySmartContractId(request.GET['id'])
        if resData is None:
            return Response({"message": "Something Wrong!!!"}, status=status.HTTP_400_BAD_REQUEST)
        return Response(resData, status=status.HTTP_201_CREATED)
    except Exception as e:
        print(e)
        return Response({"message": "Faill!!!"}, status=status.HTTP_400_BAD_REQUEST)

# Get functions by smartcontract id
@api_view(['GET'])
def getFuntionByScId(request):
    try:
        resData = dbcontext.getFunctionBySCId(request.GET['id'])
        if resData is None:
            return Response({"message": "Something Wrong!!!"}, status=status.HTTP_400_BAD_REQUEST)
        return Response(resData, status=status.HTTP_201_CREATED)
    except Exception as e:
        print(e)
        return Response({"message": "Faill!!!"}, status=status.HTTP_400_BAD_REQUEST)        


# Get Argument 
@api_view(['GET'])
def getLocalVar(request):
    try:
        resData = dbcontext.getLocalVarByFuncId(request.GET['id'])
        if resData is None:
            return Response({"message": "Something Wrong!!!"}, status=status.HTTP_400_BAD_REQUEST)
        return Response(resData, status=status.HTTP_201_CREATED)
    except Exception as e:
        print(e)
        return Response({"message": "Faill!!!"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def getFunctionVarArgu(request):
    try:
        funcDB = dbcontext.getFunctionBySCId(request.GET['id'])
        gloVar = dbcontext.getGlobalVarBySmartContractId(request.GET['id'])
        resData = {
            "functions":funcDB,
            "globalVar":gloVar
        }
        if resData['functions'] is None or resData['globalVar'] is None:
            return Response({"message":"No Content"}, status=status.HTTP_400_BAD_REQUEST)
        return Response(resData, status=status.HTTP_201_CREATED)
    except Exception as e:
        print(e)
        return Response({"message": "Faill!!!"}, status=status.HTTP_400_BAD_REQUEST)

# INSERT INTO INITIAL MARKING
@api_view(['POST'])
def addNewInitialMarking(request):
    print('Number======',request.GET['num_user'])
    try:
        resData = dbcontext.addNewInitialMarking(request.data['num_user'],request.data['IM_type'])
        if resData is None :
            return Response({"message": "Fail To Add New InitialMarking!!!"}, status=status.HTTP_400_BAD_REQUEST)
        return Response(resData, status=status.HTTP_201_CREATED)
    except Exception as e:
        print('ERROR========',e)
        return Response({"message": "Faill!!!"}, status=status.HTTP_400_BAD_REQUEST)

# INSERT INTO IMFUNCTION
@api_view(['POST'])
def addNewIMFunction(request):
    try:
        resData = dbcontext.addNewIMFunction(request.data['fun_name'],request.data['sender_from'],request.data['sender_to'])
        if resData is None :
            return Response({"message": "Fail To Add New IMFunction!!!"}, status=status.HTTP_400_BAD_REQUEST)
        return Response(resData, status=status.HTTP_201_CREATED)
    except Exception as e:
        print(e)
        return Response({"message": "Faill!!!"}, status=status.HTTP_400_BAD_REQUEST) 

# INSERT INTO IMARGUMENT
@api_view(['POST'])
def addNewIMArgument(request):
    try:
        resData = dbcontext.addNewIMArgument(request.data['arg_name'],request.data['IMfrom'],request.data['IMto'])
        if resData is None :
            return Response({"message": "Fail To Add New IMArgumentt!!!"}, status=status.HTTP_400_BAD_REQUEST)
        return Response(resData, status=status.HTTP_201_CREATED)
    except Exception as e:
        print(e)
        return Response({"message": "Faill!!!"}, status=status.HTTP_400_BAD_REQUEST) 

# INSERT INTO LNAFILE
@api_view(['POST'])
def addNewLNAFile(request):
    try:
        resData = dbcontext.addNewLNAFile(request.data['hcpnfile'],request.data['propfile'])
        if resData is None :
            return Response({"message": "Fail To Add New LNAFile!!!"}, status=status.HTTP_400_BAD_REQUEST)
        return Response(resData, status=status.HTTP_201_CREATED)
    except Exception as e:
        print(e)
        return Response({"message": "Faill!!!"}, status=status.HTTP_400_BAD_REQUEST) 

# INSERT INTO CHECKEDBATHCSC
@api_view(['POST'])
def addNewCheckedBatchSC(request):
    try:
        resData = dbcontext.addNewCheckedBatchSC(request.data['aid'],request.data['lteid'],request.data['cid']
        ,request.data['noSC'],request.data['status'],request.data['LTLformula'],request.data['result'])
        if resData is None :
            return Response({"message": "Fail To Add New CheckedBatchSC!!!"}, status=status.HTTP_400_BAD_REQUEST)
        return Response(resData, status=status.HTTP_201_CREATED)
    except Exception as e:
        print(e)
        return Response({"message": "Faill!!!"}, status=status.HTTP_400_BAD_REQUEST) 

# INSERT INTO CHECKEDSMARTCONTRACTDETAIL        
@api_view(['POST'])
def addNewCheckedSmartContractDetail(request):
    try:
        resData = dbcontext.addNewCheckedSmartContractDetail(request.data['sid'])
        if resData is None :
            return Response({"message": "Fail To Add New CheckedSmartContractDetail !!!"}, status=status.HTTP_400_BAD_REQUEST)
        return Response(resData, status=status.HTTP_201_CREATED)
    except Exception as e:
        print(e)
        return Response({"message": "Faill!!!"}, status=status.HTTP_400_BAD_REQUEST) 

# INSERT INTO BALANCE
@api_view(['POST'])
def addNewBalance(request):
    try:
        resData = dbcontext.addNewBalance(request.data['balanceType'],request.data['blfrom'],request.data['blto'],request.data['blvalue'],request.data['blrange'])
        if resData is None :
            return Response({"message": "Fail To Add New Balance!!!"}, status=status.HTTP_400_BAD_REQUEST)
        return Response(resData, status=status.HTTP_201_CREATED)
    except Exception as e:
        print(e)
        return Response({"message": "Faill!!!"}, status=status.HTTP_400_BAD_REQUEST)         
    
@api_view(['GET'])
def getArguByFunctionId(request):
    try:
        resData = dbcontext.getArgumentByFuncID(request.GET['id'])
        return Response(resData, status=status.HTTP_201_CREATED)
    except Exception as e:
        print(e)
        return Response({"message": "Faill!!!"}, status=status.HTTP_400_BAD_REQUEST)


#@api_view(['PUT'])     
#def updateSC(request, pk):
#    try:
#         SmartConstractByID = Smartcontract.objects.get(pk=pk)
#         print(pk)
#    except Smartcontract.DoesNotExist:
#        return Response(status=status.HTTP_404_NOT_FOUND)

#    if request.method == 'PUT':
#        serializer = GetSmartConstractSerializer(SmartConstractByID,data=request.data) 
#        print(serializer)
#        if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.errors, status=status.HTTP_202_ACCEPTED)
#        return Response({"message": "SmartConstract Data Invalid!!!"}, status=status.HTTP_409_CONFLICT)

#@api_view(['DELETE'])     
#def deleteSC(request, pk):
#    try:
#         SmartConstractByID = Smartcontract.objects.get(pk=pk)
#         print(SmartConstractByID)
#    except Smartcontract.DoesNotExist:
#        return Response('Fail !!!',status=status.HTTP_404_NOT_FOUND)

#    if  request.method == 'DELETE':
#          SmartConstractByID.delete()
#          return Response('Success', status=status.HTTP_204_NO_CONTENT)