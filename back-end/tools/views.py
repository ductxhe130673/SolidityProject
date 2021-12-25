from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .runscripts import *

# Create your views here.

# -----------receive data-------------------


@api_view(['POST'])
def calltools(request):
    try:
        if request.method == 'POST':
            data = request.data
            # ------test data------
            # print (data)
            print ('***data keys:', data.keys())
            name = data['name']
            print ('***name:', name)

            #------save-to-temporary--------
            if (name == 'unfolding'):
                savetotemporary(data=data)  
                output = unfolding() 
                if len(output["err"]) > 0:
                    print("aaaaaaa")
                    return Response({"detail":output["err"]}, status= status.HTTP_500_INTERNAL_SERVER_ERROR)
                else:
                    hcpn_content = ""
                    prop_content = ""
                    context_content = ""
                    print(output["file_path"] + output["file_name"])
                    try:
                        with open(output["file_path"] + output["file_name"] + ".context.lna", "r") as f:
                            context_content = f.read()
                        with open(output["file_path"] + output["file_name"] + ".lna", "r") as f:
                            hcpn_content = f.read()
                        with open(output["file_path"] + output["file_name"] + ".prop.lna", "r") as f:
                            prop_content = f.read()
                        return Response({"hcpn" : {"name":output["file_name"]+".lna", "content":hcpn_content},
                                        "prop":{"name":output["file_name"]+".prop.lna", "content":prop_content},
                                        "context": {"name":output["file_name"]+".context.lna", "content":context_content, "context_type":"CPN"}}
                                        , status = status.HTTP_200_OK)
                    except:
                        return Response({"message": "Generate file error"}, status = status.HTTP_500_INTERNAL_SERVER_ERROR)
                #return Response({"message": "Run Unfolding Successfully"}, status=status.HTTP_200_OK) 
            #------helena-----------               
            elif (name == 'helena'):
                result = runHelena()
                #print(result)
                return Response({"message": result}, status=status.HTTP_200_OK)
            return Response({"message": "Run Tool Successfully"}, status=status.HTTP_200_OK)
    except:
        return Response({"message": "Run Tool Fail!!"}, status=status.HTTP_400_BAD_REQUEST)
        

