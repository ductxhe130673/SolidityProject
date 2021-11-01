from django.contrib import admin
from django.urls import path
from .views import SmartConstractAPIView
from smartconstract import views

urlpatterns = [
    path('select-smart-contract/',SmartConstractAPIView.as_view()),
    path('scbyid',views.getScById),
    path('globalvarialbe',views.getGBByScId),
    path('localvariable',views.getLocalVar),
    path('getfunction',views.getFuntionByScId),
    path('getvariablefunctionargu',views.getFunctionVarArgu),
    path('getargubyfunctionid', views.getArguByFunctionId)
]
