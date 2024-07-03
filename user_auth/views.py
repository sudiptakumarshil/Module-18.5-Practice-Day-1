from django.shortcuts import render,redirect
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout,authenticate

def user_register(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request,'User created Successfully!!')
                return redirect('home')
        else:
            form = RegisterForm()
        return render(request,'register.html',{'form':form})
    return redirect('home')

def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request = request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(username = username, password = password)
                if user is not None:
                    login(request,user)
                    messages.success(request,'Logged In Successfully!')
                    return redirect('user.profile')
            else:
                messages.warning(request,form.errors.as_text())
    
        form = AuthenticationForm()
        return render(request,'login.html',{'form':form})
    return redirect('user.profile')


def user_logout(request):
    logout(request)
    messages.success(request,'Logged Out Successfully!')
    return redirect('user.login')
