from pyexpat.errors import messages
from urllib.request import AbstractDigestAuthHandler
from django.shortcuts import render

from permissions.serializers import EmployeeSerializer
from .models import DamcoEmployee
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset=DamcoEmployee.objects.all()
    serializer_class=EmployeeSerializer
    authentication_classes=[BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
