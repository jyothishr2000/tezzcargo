from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import auth
from django.contrib.auth.models import User

# Create your views here.

def home(req):
    return render(req,'home.html')

def about(req):
    return render(req,'about.html')

def log(req):
    if req.method=='POST':
        uname=req.POST['uname']
        password=req.POST['pas']
        user=auth.authenticate(username=uname,password=password)
        if user:
            auth.login(req,user)
            return redirect('/')
        msg="Invalid Username or Password"
        return render(req,'login.html',{'msg': msg})
    else:
        return render(req,'login.html')

def register(req):
    if req.method=='POST':
        uname=req.POST['uname']
        fname=req.POST['fname']
        lname=req.POST['lname']
        ename=req.POST['ename']
        password=req.POST['pas']
        repassword=req.POST['repas']
        if password==repassword:
            if User.objects.filter(username=uname):
                msg='Username already exists'
                return render(req,'register.html',{'msg': msg})
            elif User.objects.filter(email=ename):
                msg='E-mail address already exists'
                return render(req,'register.html',{'msg': msg})
            else:
                user=User.objects.create_user(username=uname,first_name=fname,last_name=lname,email=ename,password=password)
                user.save();
                auth.login(req,user)
                return redirect ('/')
        else:
            msg='Invalid password'
            return render(req,'register.html',{'msg': msg})
    else:
        return render(req,'register.html')
    
def logout(req):
    auth.logout(req)
    return redirect('/')

def order(req):
    return render(req,'tocargo.html')