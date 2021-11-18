from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import cpncontext

class cpncontextSerializer(serializers.ModelSerializer):
    class Meta:
        model = cpncontext
        # fields = ['name', 'description', ]
        fields = '__all__'
class cpncontextSerializerPost(serializers.ModelSerializer):
    class Meta:
        model = cpncontext
        fields = ['name', 'content', 'context_type','createdDate', 'description', 'aid',]