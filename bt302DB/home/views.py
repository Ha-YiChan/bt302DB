from django.shortcuts import render
from .models import Student
# Create your views here.

def home(request):
    stdVar = Student.objects.all()
    return render(request,'home/index.html',{'data' : stdVar})