import email
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User

# Create your views here.

def index(request):
    user = User.objects.all()    
    context = {'users':user}
    return render(request,'student/index.html',context)

def studentlist(request):
      return render(request,'student/students.html')

def student(request,id):
    return render(request,'student/student.html')
