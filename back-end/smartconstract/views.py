
from .serializer import GetSmartConstractSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
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

@api_view(['POST'])
def addNewInitialMarking(request):
    try:
        resData = dbcontext.addNewInitialMarking(request.GET['num_user'],request.GET['IM_type'])
        # print(request.GET['IM_type'])
        # print(request.GET['num_user'])
        # print(resData)
        if resData is None :
            return Response({"message": "Fail To Add New InitialMarking!!!"}, status=status.HTTP_400_BAD_REQUEST)
        return Response(resData, status=status.HTTP_201_CREATED)
    except Exception as e:
        print(e)
        return Response({"message": "Faill!!!"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def addNewBalanceTypeFixed(request):
    try:
        resData = dbcontext.addNewBalanceTypeFixed(request.GET['blvalue'],request.GET['imid'])
        if resData is None :
            return Response({"message": "Fail To Add New Balance!!!"}, status=status.HTTP_400_BAD_REQUEST)
        return Response(resData, status=status.HTTP_201_CREATED)
    except Exception as e:
        print(e)
        return Response({"message": "Faill!!!"}, status=status.HTTP_400_BAD_REQUEST)      

@api_view(['POST'])
def addNewBalanceTypeRandom(request):
    try:
        resData = dbcontext.addNewBalanceTypeRandom(request.GET['blfrom'],request.GET['blto'],request.GET['blvalue'],request.GET['imid'])
        if resData is None :
            return Response({"message": "Fail To Add New Balance!!!"}, status=status.HTTP_400_BAD_REQUEST)
        return Response(resData, status=status.HTTP_201_CREATED)
    except Exception as e:
        print(e)
        return Response({"message": "Faill!!!"}, status=status.HTTP_400_BAD_REQUEST) 

@api_view(['POST'])
def addNewIMFunction(request):
    try:
        resData = dbcontext.addNewIMFunction(request.GET['fun_name'],request.GET['sender_from'],request.GET['sender_to'],request.GET['imid'])
        if resData is None :
            return Response({"message": "Fail To Add New IMFunction!!!"}, status=status.HTTP_400_BAD_REQUEST)
        return Response(resData, status=status.HTTP_201_CREATED)
    except Exception as e:
        print(e)
        return Response({"message": "Faill!!!"}, status=status.HTTP_400_BAD_REQUEST) 

@api_view(['POST'])
def addNewIMArgument(request):
    try:
        resData = dbcontext.addNewIMFunction(request.GET['arg_name'],request.GET['IMfrom'],request.GET['IMto'],request.GET['imfid'])
        if resData is None :
            return Response({"message": "Fail To Add New IMArgumentt!!!"}, status=status.HTTP_400_BAD_REQUEST)
        return Response(resData, status=status.HTTP_201_CREATED)
    except Exception as e:
        print(e)
        return Response({"message": "Faill!!!"}, status=status.HTTP_400_BAD_REQUEST) 

@api_view(['POST'])
def addNewLNAFile(request):
    try:
        resData = dbcontext.addNewLNAFile(request.GET['hcpnfile'],request.GET['propfile'])
        if resData is None :
            return Response({"message": "Fail To Add New LNAFile!!!"}, status=status.HTTP_400_BAD_REQUEST)
        return Response(resData, status=status.HTTP_201_CREATED)
    except Exception as e:
        print(e)
        return Response({"message": "Faill!!!"}, status=status.HTTP_400_BAD_REQUEST) 

@api_view(['POST'])
def addNewCheckedBatchSC(request):
    try:
        resData = dbcontext.addNewIMFunction(request.GET['aid'],request.GET['lnid'],request.GET['lteid'],request.GET['cid'],
        request.GET['imid'],request.GET['noSC'],request.GET['checkedDate'],request.GET['status'],request.GET['LTLformula'],request.GET['result'])
        if resData is None :
            return Response({"message": "Fail To Add New CheckedBatchSC!!!"}, status=status.HTTP_400_BAD_REQUEST)
        return Response(resData, status=status.HTTP_201_CREATED)
    except Exception as e:
        print(e)
        return Response({"message": "Faill!!!"}, status=status.HTTP_400_BAD_REQUEST) 

@api_view(['POST'])
def addNewCheckedSmartContractDetail(request):
    try:
        resData = dbcontext.addNewIMFunction(request.GET['sid'],request.GET['bid'])
        if resData is None :
            return Response({"message": "Fail To Add New CheckedSmartContractDetail !!!"}, status=status.HTTP_400_BAD_REQUEST)
        return Response(resData, status=status.HTTP_201_CREATED)
    except Exception as e:
        print(e)
        return Response({"message": "Faill!!!"}, status=status.HTTP_400_BAD_REQUEST) 

@api_view(['GET'])
def demo(request):
    try:
        resData = dbcontext.getArgumentByFuncID(request.GET['id'])
        return Response(resData, status=status.HTTP_201_CREATED)
    except Exception as e:
        print(e)
        return Response({"message": "Faill!!!"}, status=status.HTTP_400_BAD_REQUEST)
