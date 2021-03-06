"""geekyshows URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from T1.views import EmployeeModelViewSet
from nested_serializer import views
from mixins.views import LCStudent,RUDStudent

router=DefaultRouter()
router.register('studentapi',EmployeeModelViewSet,basename='student')
router.register('singer',views.SingerViewSet,basename='sinder')
router.register('song',views.SongViewSet,basename='song')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('polls/', include('A1.urls')),
    path('',include(router.urls)),
    path('mixins',LCStudent.as_view()),
    path('mixinspk/<int:pk>/',RUDStudent.as_view()),
   


    
]
