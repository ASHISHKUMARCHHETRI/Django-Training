from django.contrib import admin
from django.urls import path
from api import views
from rest_framework.routers import DefaultRouter
 

router
urlpatterns= [
    path('admin/',admin.site.urls),
]