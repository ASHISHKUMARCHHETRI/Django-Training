from django.contrib import admin
from .models import DamcoEmployee

# Register your models here.
@admin.register(DamcoEmployee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display=['id','Name','Experiance','Location']

