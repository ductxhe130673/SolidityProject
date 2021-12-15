from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import ltltemplate

class ltltemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ltltemplate
        fields = '__all__'

class ltltemplateSerializerPost(serializers.ModelSerializer):
    class Meta:
        model = ltltemplate
        fields = ['name', 'formula', 'template_type', 'description', 'aid', 'createdDate' ]