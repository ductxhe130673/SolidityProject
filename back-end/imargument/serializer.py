from django.db import models
from django.db.models import fields
from rest_framework import serializers
from . models import IMArgument

class GetIMArgumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = IMArgument
        fields= '__all__'