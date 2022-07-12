from django.shortcuts import render, reverse, get_object_or_404
from myAPP.models import Student, Teaching, Course
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
def home(request):
    return render(request, 'homepage/home.html')

def studentreg(request):
    return render(request, 'homepage/studentreg.html')

def insert_view(request):
    sname = request.POST["sname"]
    semail = request.POST["semail"]
    smobileno = request.POST["smobileno"]
    spassword = request.POST["spassword"]
    course = request.POST["scourse"]
    faculty = request.POST["sfaculty"]
    students = Student(sname = sname, semail = semail, smobileno = smobileno, spassword = spassword, scourse= course, sfaculty = faculty)
    students.save()
    return HttpResponseRedirect(reverse('fetch'))

def fetch_all_view(request):
    students = Student.objects.all()
    return render(request,'homepage/success.html',{'students': students})

def edit_view(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, 'homepage/edit.html', {'student': student})


def editpage_view(request):
    id = request.POST["sid"]
    name = request.POST["sname"]
    email = request.POST["semail"]
    mobileno = request.POST["smobileno"]
    password = request.POST["spassword"]
    course = request.POST["scourse"]
    faculty = request.POST["sfaculty"]
    students = Student( id=id,sname = name, semail = email,smobileno = mobileno, spassword = password, scourse= course, sfaculty = faculty)
    students.save()
    return HttpResponseRedirect(reverse('fetch'))


def delete_view(request, pk):
    student = get_object_or_404(Student, pk=pk)
    student.delete()
    return HttpResponseRedirect(reverse('fetch'))

def contact(request):
    return render(request, 'homepage/contact.html')

def about(request):
    return render(request, 'homepage/about.html')

def askstaff(request):
    return  render(request, 'homepage/askstaff.html')

def teachingreg(request):
    return  render(request, 'homepage/teachingreg.html')

def nonteachingreg(request):
    return  render(request, 'homepage/nonteachingreg.html')

def login(request):
    return render(request, 'homepage/login.html')

def logincheck(request):
    email = request.POST.get("semail")
    password = request.POST.get("spassword")
    l = Student.objects.filter(semail = email , spassword = password)
    if l:
        msg = "Welcome " + l[0].sname
        teacher = Teaching.objects.all()
        return render(request, 'homepage/welcomestu.html', {"msg": msg, "teacher": teacher})
    else:
        msg = "Please Check Your Credentials!"
        return render(request, "homepage/login.html", {"msg": msg})

def saveteacher(request):
    tid = request.POST["tid"]
    tname = request.POST["tname"]
    temail = request.POST["temail"]
    tpassword = request.POST["tpassword"]
    tmobileno = request.POST["tmobileno"]
    tbranch = request.POST["tbranch"]
    teacher = Teaching(tid = tid, tname = tname, temail = temail, tmobileno = tmobileno, tpassword = tpassword, tbranch =tbranch)
    teacher.save()
    return HttpResponseRedirect(reverse('fetch_teacher'))

def fetch_teacher(request):
    teacher = Teaching.objects.all()
    return render(request, 'homepage/successteach.html', {'teacher': teacher})

def loginteach(request):
    return render(request, 'homepage/loginteach.html')

def logincheckteach(request):
    email = request.POST.get("temail")
    password = request.POST.get("tpassword")
    teacher = Teaching.objects.filter(temail=email, tpassword=password)
    if teacher:
        msg = "Welcome " + teacher[0].tname
        return render(request, 'homepage/welcometeach.html', {"msg": msg})
    else:
        msg = "Please Check Your Credentials!"
        return render(request, "homepage/loginteach.html", {"msg": msg})

def coursesave(request):
    course = request.POST.get("scourse")
    faculty = request.POST.get("sfaculty")

    c = Course.objects.filter(scourse = course, sfaculty = faculty)
    return render(request, 'homepage/success.html')


