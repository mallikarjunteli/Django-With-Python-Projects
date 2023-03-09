from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect

from patientapp.models import Patient


# Create your views here.
def index_fun(request):
    return render(request,'index.html')


def read_data(request):
    sname = request.POST['txtName']
    sage = request.POST['txtAge']
    scity = request.POST['ddlCity']
    sdisease = request.POST['ddlDisease']

    p1 = Patient(name=sname,age=sage,city=scity,disease=sdisease)
    p1.save()
    return HttpResponse('inserted successfully')

def display_fun(request):
    p2 = Patient.objects.values()
    print(p2)
    return render(request, 'display.html', {'data': p2})

def update_fun(request,x):
    p1=Patient.objects.get(id=x)
    if request.method == 'POST':
        p1.name = request.POST['txtName']
        p1.age = request.POST['txtNum']
        p1.city = request.POST['ddlCity']
        p1.disease = request.POST['ddlDisease']
        p1.save()

        p2 = Patient.objects.values()
        return render(request,'display.html',{ 'data':p2 })

    return render(request,'update.html',{'data': p1})

def delete_fun(request,y):
    p1=Patient.objects.get(id=y)
    p1.delete()
    return redirect('display')

def register_fun(request):
    return render(request,'register.html')

def reg_data(request):
    uname = request.POST['txtName']
    mail = request.POST['txtMail']
    pswd = request.POST['txtPswd']
    u1 = User.objects.create_superuser(username=uname,password=pswd,email=mail)
    u1.save()
    return redirect('log')

def log_fun(request):
    return render(request,'login.html',{'data':''})

def log_data(request, _superuser=None):
    if request.method == 'POST':
        uname = request.POST['txtName']
        pswd = request.POST['txtPswd']
        myuser = authenticate(username=uname,password=pswd)
        if myuser is not None:
            if myuser.is_superuser:
                return render(request,'home.html',{'data1' : myuser})
        else:
            return render(request,'login.html',{'data':'Credentials are Invalid !!'})

def home_fun(request):
    return render(request,'home.html')

def logout_fun(request):
    messages.info(request,'you have successfully logged out')
    return redirect('log')