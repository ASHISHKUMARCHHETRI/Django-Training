from xml.dom.pulldom import START_DOCUMENT
from rest_framework import serializers
from .models import DamcoEmployee

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=DamcoEmployee
        fields=['id','Name','Experiance','Location']

