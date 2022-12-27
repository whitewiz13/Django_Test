from django.shortcuts import render
from django.http import HttpResponse
from . models import Employee

def index(request):
    employee_list = Employee.objects.all()
    return render(request,'manageEmployee/index.html',{'employee_list':employee_list})
