from django.shortcuts import render
from rest_framework.response import Response
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework import status,viewsets

# Create your views here.
class EmployeeViewSet(viewsets.ViewSet):
    def list(sel,resquest):
        emp =Employee.objects.all()
        serializer = EmployeeSerializer(emp,many=True)
        return Response(serializer.data)

    def retrieve(sel,request,pk=None):
        id=pk
        if id is not None:
            stu=Employee.objects.get(id=id)
            serializer=EmployeeSerializer(stu)
            return Response(serializer.data)
    
    def create(sel,request):
        serializer=EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':"Data Created"},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def update(self,request,pk):
        id=pk
        emp=Employee.objects.get(pk=id)
        serializer=EmployeeSerializer(emp,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Complete Data Updated'})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self,request,pk):
        id=pk
        emp=Employee.objects.get(pk=id)
        serializer=EmployeeSerializer(emp,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Partial Data Updated'})
        return Response(serializer.errors)

    def destroy(self,request,pk):
        id=pk
        emp=Employee.objects.get(pk=id)
        emp.delete()
        return Response({'msg':'Data Deleted'})
        



    


