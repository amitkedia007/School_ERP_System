from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.mainpanel, name='mainpanel'),
    path('studentinfo', views.studentinfo, name='studentinfo'),
    path('facultyinfo', views.facultyinfo, name='facultyinfo'),
    path('otherstaff', views.otherstaff, name='otherstaff')
]

