from django.contrib import auth
from django.core.context_processors import csrf
from django.shortcuts import render, redirect, render_to_response

# Create your views here.
from accounts.forms import UserChangeForm


def edit(request):
    args = {}
    args['form'] = UserChangeForm()
    '''
    if request.POST:
        newuser_from = UserChangeForm(request.POST)
        if newuser_from.is_valid():
            newuser_from.save()
            newuser = auth.authenticate(username=newuser_from.cleaned_data['username'],
                                             password=newuser_from.cleaned_data['password2'])
            auth.login(request, newuser)
            return redirect('/')
        else:
            args['form'] = newuser_from'''
    return render_to_response('register1.html', args)