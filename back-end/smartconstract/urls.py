from django.contrib import admin
from django.urls import path
from .views import SmartConstractAPIView
from smartconstract import views

urlpatterns = [
    path('select-smart-contract',SmartConstractAPIView.as_view()),
    path('scbyid',views.getScById),
    path('globalvarialbe',views.getGBByScId),
    path('localvariable',views.getLocalVar),
    path('getfunction',views.getFuntionByScId),
    path('getvariablefunctionargu',views.getFunctionVarArgu),
    path('addnewinitialmarking',views.addNewInitialMarking),
    path('addnewimfunction',views.addNewIMFunction),
    path('addnewimargument',views.addNewIMArgument),
    path('addnewlnafile',views.addNewLNAFile),
    path('addnewcheckedbatchsc',views.addNewCheckedBatchSC),
    path('addnewcheckedsmartcontractdetail',views.addNewCheckedSmartContractDetail),
    path('addnewbalance',views.addNewBalance),
    path('getargubyfunctionid', views.getArguByFunctionId)
]
