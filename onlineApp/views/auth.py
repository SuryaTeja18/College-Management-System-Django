from onlineApp.models import *
from django.shortcuts import render,redirect
from django.views import View
from django.urls import resolve
from onlineApp.Forms.colleges import *
from onlineApp.Forms.auth import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import *

def logout_user(request):
    logout(request)
    return redirect('login')

class Login(View):
    def get(self,request,*args,**kwargs):
        form = LoginForm()
        return render(request,"login.html",{'form':form})

    def post(self,request,*args,**kwargs):
        form = LoginForm(request.POST)
        if (form.is_valid()):
            uname = form.cleaned_data['username']
            passwd = form.cleaned_data['password']
            print(uname,passwd)
            user = authenticate(request,username=uname,password=passwd)
            print(user)
            if user is not None:
                login(request,user)
                return redirect('colleges')
            else:
                return redirect('login')

class SignUp(View):
    def get(self,request,*args,**kwargs):
        form = SignupForm()
        return render(request,"signup.html",{'form':form})

    def post(self,request,*args,**kwargs):
        form = SignupForm(request.POST)
        if(form.is_valid()):
            user = User.objects.create_user(**form.cleaned_data)
            user.save()
            if(user is not None):
                login(request,user)
                return redirect('colleges')

        return redirect('login')
