from email import message
from django.shortcuts import render
from django.contrib import messages
from .models import login

def login1(request):
    print("inside login model")
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if login.objects.filter(username=username).exists() and login.objects.filter(password=password).exists(): 
            messages.info(request,'successfully logged in')
            return render(request,'login.html') 
        else:
            messages.info(request,'Invalid')
            return render(request,'register.html') 

    else:
        return render(request,'login.html') 

# Create your views here.
def register(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        email = request.POST['email']
        if login.objects.filter(username=username).exists():
            print('username is taken')
            messages.info(request,'username is taken')
            return render(request,'register.html')
        elif login.objects.filter(email=email).exists():
            print('email is taken')
            messages.info(request,'email is taken')
            return render(request,'register.html')
        elif password==cpassword:
            obj = login()
            obj.username = request.POST['username']
            obj.password = request.POST['password']
            obj.email = request.POST['email']
            obj.save()
            print('yess')
            return render(request,'register.html') 
        else:
            messages.info(request,'Password not matched')
            return render(request,'register.html')        
    else:
        return render(request,'register.html')