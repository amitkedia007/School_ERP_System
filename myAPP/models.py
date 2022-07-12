from django.db import models

# Create your models here.


class Teaching(models.Model):
    tid = models.IntegerField(primary_key= True)
    tname = models.CharField(max_length=20)
    temail = models.EmailField()
    tpassword = models.CharField(max_length=20)
    tmobileno = models.IntegerField(10)
    tbranch = models.CharField(max_length= 15)

    def __str__(self):
        return self.tname

class Student(models.Model):
    sname = models.CharField(max_length=20, template_name= 'templates/homepage/welcomestu.html', orderable=False)
    semail = models.EmailField(template_name= 'templates/homepage/welcomestu.html', orderable=False)
    smobileno = models.IntegerField(template_name= 'templates/homepage/welcomestu.html', orderable=False)
    spassword= models.CharField(max_length=30, template_name= 'templates/homepage/welcomestu.html', orderable=False)
    sfaculty = models.ForeignKey(Teaching, default="foobar", on_delete=models.CASCADE)
    scourse= models.CharField(max_length=30, default="foobar")

    def __str__(self):
        return self.sname
