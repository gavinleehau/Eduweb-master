from django.shortcuts import render, redirect, HttpResponsePermanentRedirect
from django.contrib.auth import authenticate, login
from .forms import RegisterForm, LoginForm
from django.contrib import messages

def register_user(request):
    if request.method =="POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save_user()
            return redirect('index')
    
    return render(
        request=request,
        template_name= "user/register.html",
        context={}
    )

def login_user(request):
    message= ""
    if request.method =="POST":
        user=authenticate(
            username=request.POST['username'],
            password=request.POST['password'],
        )
        if user is not None:
            print("Dung")
            login(request, user)
            return redirect('index')
        else:
            print("sai")
            messages.info(request, "Tài khoản hoặc mật khẩu không đúng. Vui lòng thử lại")
    
    return render(
        request=request,
        template_name="login.html",
        context={
            'message':message
        }
    )