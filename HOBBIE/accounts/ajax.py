# -*- coding: utf-8 -*-
from dajaxice.decorators import dajaxice_register
from django.contrib import auth
from django.core.context_processors import csrf
from django.shortcuts import redirect, render_to_response

__author__ = '1240'


@dajaxice_register
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