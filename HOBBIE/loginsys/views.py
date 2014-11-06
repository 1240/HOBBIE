# -*- coding: utf-8 -*-
from django.contrib import auth
from django.core.context_processors import csrf
from django.core.files import File
from django.shortcuts import redirect, render_to_response


# Create your views here.
from accounts.forms import UserCreationForm
from accounts.models import User
from utils.utils import create_image


def login(request):
    args = {}
    args.update(csrf(request))
    args['user'] = auth.get_user(request)
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
            newuser = auth.authenticate(username=newuser_from.cleaned_data['email'],
                                        password=newuser_from.cleaned_data['password2'])
            auth.login(request, newuser)
            user = User.objects.get(id=auth.get_user(request).id)
            f = open(create_image('%s %s' % (user.first_name, user.last_name), user.first_name, W=500), 'rb')
            name_image = File(f)
            user.name_image.save(user.username + '_name.png', name_image)
            f = open(create_image(user.username, user.username), 'rb')
            username_image = File(f)
            user.username_image.save(user.username + '.png', username_image)
            user.save()
            return redirect('/')
        else:
            args['form'] = newuser_from
    return render_to_response('register1.html', args)


def register1(request):
    args = {}
    args.update(csrf(request))
    return render_to_response('register.html')