from django.contrib import admin
from django.urls import path
from .views import SmartConstractAPIView
from smartconstract import views

urlpatterns = [
    path('select-smart-contract/',SmartConstractAPIView.as_view()),
    path('scbyid',views.getScById),
    path('func-and-argu-by-scid/',views.getFunctionAndArgumentBySmartcontractId),
    path('all-func-and-argu-by-scid/',views.getAllFunctionAndArgumentBySmartcontractId),
]
