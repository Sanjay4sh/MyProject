import re
from urllib import response
from django.http import HttpResponse
from Employee.models import Employee
from django.shortcuts import render,redirect

def index(request):
    
    return render(request,'index.html')

def aboutus(request):
    return render(request,'aboutus.html')

def contact(request):
    return render(request,'contact.html')

def portfolio(request):
    return render(request,'portfolio.html')

def services(request):
    return render(request,'services.html')        
    
def register(request):
    return render(request,'register.html')  

def show(request):
    emp = Employee.objects.all().values()
    return render(request,'show.html',{'emp':emp})  

def save(request):
    emp  = Employee(firstname=request.GET['firstname'],lastname=request.GET['lastname'],salary=request.GET['salary'],dob=request.GET['dob'])
    emp.save();
    return redirect('/show')

def edit(request,id):
    emp = Employee.objects.get(id=id)
    return render(request,'edit.html',{'emp':emp}) 

def update(request,id):
    emp  = Employee.objects.get(id=id)
    emp.firstname =request.GET['firstname'] 
    emp.lastname =request.GET['lastname'] 
    emp.salary =request.GET['salary'] 
    emp.dob =request.GET['dob'] 
    emp.save();
    return redirect('/show')

def delete(request,id):
    emp = Employee.objects.filter(id=id).delete()
    return redirect('/show')