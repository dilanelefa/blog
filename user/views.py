from user.models import User
from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.contrib.auth import authenticate, login as Login, logout as Logout
from . import forms
from blog import settings
from .middlewares import auth


def login(request: HttpRequest):
    errors = ''
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if not form.is_valid():

            errors = form.errors.as_ul()
        else:
            user = authenticate(
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password']
            )

            if user is not None:
                Login(request, user)
                return redirect(settings.LOGIN_REDIRECT_URL)
            else:
                errors = 'login failed'

    context = {
        'errors': errors

    }

    return render(request, 'user/login.html', context)


def logout(request: HttpRequest):
    if request.method == 'POST':
        Logout(request)
        return redirect('login')


def register(request: HttpRequest):
    if request.method == 'GET':
        return render(request, 'user/register.html')
    else:
        form = forms.RegisterForm(request.POST)
        if form.is_valid():
            user_data = form.cleaned_data
            user = User.objects.create_user(email=user_data['email'], password=user_data['password'], username=user_data['username'])
            Login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
        else:
            return render(request, 'user/register.html', {'errors': form.errors.as_ul()})


@auth
def profile(request: HttpRequest):
    return render(request, 'user/profile.html')
