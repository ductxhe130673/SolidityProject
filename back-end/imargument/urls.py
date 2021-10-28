from django.contrib import admin
from django.urls import path
from .views import GetAllArgument, GetArgumentBySmartContractIDandFuntionID
from imargument import views

urlpatterns = [
    path('get-all-argument/',GetAllArgument.as_view()),
    path('argubyscidandfuid/',GetArgumentBySmartContractIDandFuntionID.as_view()),
]
