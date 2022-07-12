"""myProject URL Configuration

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

from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path
from myAPP import views

urlpatterns = [
    path('', views.home, name= 'home'),
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about'),
    path('studentreg', views.studentreg, name='studentreg'),
    path('askstaff', views.askstaff, name='askstaff'),
    path('teachingreg', views.teachingreg, name='teachingreg'),
    path('nonteachingreg', views.nonteachingreg, name='nonteachingreg'),
    path('fetch_all_view', views.fetch_all_view, name='fetch_all_view'),
    path('savestudent/', views.insert_view, name='savestudent'),
    path('fetch/',views.fetch_all_view,name='fetch'),
    path('edit/<int:pk>/',views.edit_view,name='edit'),
    path('delete/<int:pk>/',views.delete_view,name='delete'),
    path('editpage/',views.editpage_view,name='editpage'),
    path('login/', views.login, name='login'),
    path('logincheck/', views.logincheck, name='logincheck'),
    path('saveteacher/', views.saveteacher, name='saveteacher'),
    path('logincheckteach/', views.logincheckteach, name='logincheckteach'),
    path('loginteach/', views.loginteach, name='loginteach'),
    path('fetch_teacher/', views.fetch_teacher, name='fetch_teacher'),
    path('coursesave/', views.coursesave, name='coursesave'),
]
