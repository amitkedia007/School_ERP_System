from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def mainpanel(request):
    return HttpResponse('This is Main Panel')
    #return render(request, '')

def studentinfo(request):
    #return HttpResponse('Here you will get student information')
    return render(request,'studentinfo.html')

def facultyinfo(request):
    return HttpResponse('Here you will get faculties information')
    #return render(request, 'homepage/about.html')

def otherstaff(request):
    return HttpResponse('Other staff information')
    #return render(request, 'homepage/about.html')
