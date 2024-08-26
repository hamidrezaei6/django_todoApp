from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, UserLoginForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


def user_register(requset):
    if requset.method == 'POST':
        form = UserRegistrationForm(requset.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = User.objects.create_user(cd['username'], cd['email'], cd['password'])
            user.first_name = cd['first_name']
            user.last_name = cd['last_name']
            user.save()
            messages.success(requset, 'ثبت نام شما با موفقیت انجام شد', 'success')
            return redirect('home')
    else:
        form = UserRegistrationForm()

    return render(requset, 'register.html', {'form': form})


def user_login(requset):
    if requset.method == 'POST':
        form = UserLoginForm(requset.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(requset, username=cd['username'], password=cd['password'])
            if user is not None:
                login(requset, user)
                messages.success(requset, 'شما با موفقیت وارد سایت شدید', 'success')
                return redirect('home')
            else:
                messages.error(requset, 'نام کاربری یا کلمه عبور اشتباه است', 'danger')
    else:
        form = UserLoginForm()
    return render(requset, 'login.html', {'form': form})


def user_logout(request):
    logout(request)
    messages.success(request, 'کاربر خارج شد', 'success')
    return redirect('home')
