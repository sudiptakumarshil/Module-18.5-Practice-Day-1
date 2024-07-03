from django.shortcuts import render,redirect
from .forms import ChangeUserForm
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm,SetPasswordForm
from django.contrib.auth import update_session_auth_hash

# Create your views here.
def user_profile(request):
    if request.user.is_authenticated:
        return render(request,'profile.html',{'user':request.user})
    return redirect('user.login')

def password_change(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form  = PasswordChangeForm(user = request.user,data = request.POST)
            if form.is_valid():
                user = form.save()
                update_session_auth_hash(request, user)
                messages.success(request,'Password Changed Successfully!!')
                return redirect('user.profile')
            messages.warning(request,form.errors.as_text())
        else:
            form = PasswordChangeForm(user=request.user)
        return render(request,'change_password.html',{'form':form })
    return redirect('user.login')
    

def password_change_except_old(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form  = SetPasswordForm(user = request.user,data = request.POST)
            if form.is_valid():
                user = form.save()
                update_session_auth_hash(request, user)
                messages.success(request,'Password Changed Successfully!!')
                return redirect('user.profile')
            messages.warning(request,form.errors.as_text())
        else:
            form = SetPasswordForm(user=request.user)
        return render(request,'change_password.html',{'form':form })
    return redirect('user.login')


def changeUserProfile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form  = ChangeUserForm(request.POST,instance=request.user)
            if form.is_valid():
                form.save()
                messages.success(request,'User Info Updated Successfully!!')
                return redirect('user.profile')
            messages.warning(request,form.errors.as_text())
        else:
            form = ChangeUserForm(instance=request.user)
        return render(request,'profile.html',{'form':form })
    return redirect('user.login')