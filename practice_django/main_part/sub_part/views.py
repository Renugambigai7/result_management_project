from django.shortcuts import render
from . models import *
# Create your views here.
def index(request):
    return render(request,'index.html')

def login(request):
    return render(request,'login.html')

def register(request):
    return render(request,'register.html')

def bca(request):
    return render(request,'bca.html')

def bsccs(request):
    return render(request,'bsccs.html')

def result(request):
    return render(request,'result.html')

def admin(request):
    return render(request,'admin.html')


def dashboard(request):
    return render(request,'dashboard.html')

def score(request):
    return render(request,'score.html')

def register_form_submission(request):
    username=request.POST.get('username')
    student_ID=request.POST.get('student_ID')
    password=request.POST.get('password')
    print( username,student_ID,password)
     
    ex1 = register_table(username=username, student_id=student_ID, password=password)

    ex1.save()
    print("data saved into database")
    return render(request,'login.html') 


def login_form_submission(request):

    if register_table.objects.filter(student_ID=request.POST.get('student_ID'),password=request.POST.get('password')).exists():
        print("login success")
        return render(request,'dashboard.html',)
    else:   
        print("login failed")
        return render(request,'login.html')
    
