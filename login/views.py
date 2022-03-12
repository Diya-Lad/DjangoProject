from email import message
from xml.dom.minidom import Document
from django.shortcuts import render
from django.contrib import messages
from .models import login, importantDocuments

def login1(request):
    if request.method == 'POST':
        email = request.POST['email']
        print('loginnnn')
        request.session['email'] = email
        print(request.session['email'])
        
        password = request.POST['password']
        if login.objects.filter(email=email).exists() and login.objects.filter(password=password).exists(): 
            return render(request,'home.html') 
        else:
            return render(request,'login.html') 
    else:
        return render(request,'login.html') 

# # Create your views here.
def register(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        email = request.POST['email']
        if login.objects.filter(email=email).exists():
            print('email is taken')
            messages.info(request,'email is taken')
            return render(request,'register.html')
        elif password==cpassword:
            obj = login()
            obj.firstname = request.POST['firstname']
            obj.lastname = request.POST['lastname']
            obj.password = request.POST['password']
            obj.email = request.POST['email']
            obj.role = request.POST['role']
            obj.save()
            print("saved")
            return render(request,'login.html')        
    else:
        return render(request,'register.html')

def home(request):
    return render(request,'home.html')

def importantDocument(request):
    return render(request,'importantDocument.html')

def addDocument(request):
    if request.method == 'POST':
        title = request.POST['title']
        document = request.FILES['document']
        fileObj = importantDocuments()
        fileObj.title = title
        fileObj.document = document
        print("haaa")
        fileObj.email =request.session.get('email')
        print("nooo")
        # print(fileObj.email)
        # print(request.session.get('u_email'))
        fileObj.save()
        return render(request,'importantDocument.html')
    return render(request,'addDocument.html')