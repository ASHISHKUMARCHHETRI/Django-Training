import imp
from django.contrib import admin
from .models import Employee

# Register your models here.
admin.site.register(Employee)
class employeeAdmin(admin.ModelAdmin):
    list_display =['id','name','roll','city']
     