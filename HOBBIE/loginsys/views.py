# -*- coding: utf-8 -*-
from django.contrib import auth
from django.core.context_processors import csrf
from django.shortcuts import redirect, render_to_response

# Create your views here.
from accounts.forms import UserCreationForm


def login(request):
    args = {}
    args.update(csrf(request))
    args['username'] = auth.get_user(request).username
    args['is_authenticated'] = auth.get_user(request).is_authenticated()
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            args['login_error'] = "Пользователь не найден"
            return render_to_response('login.html', args)
    else:
        return render_to_response('login.html', args)


def logout(request):
    auth.logout(request)
    return redirect('/')


def register(request):
    args = {}
    args.update(csrf(request))
    args['form'] = UserCreationForm()
    if request.POST:
        newuser_from = UserCreationForm(request.POST)
        if newuser_from.is_valid():
            newuser_from.save()
            newuser = auth.authenticate(username=newuser_from.cleaned_data['username'],
                                             password=newuser_from.cleaned_data['password2'])
            auth.login(request, newuser)
            return redirect('/')
        else:
            args['form'] = newuser_from
    return render_to_response('register1.html', args)


def register1(request):
    args = {}
    args.update(csrf(request))
    return render_to_response('register.html')