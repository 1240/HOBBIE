from django.contrib import auth
from django.core.context_processors import csrf
from django.shortcuts import render, redirect, render_to_response

# Create your views here.
from accounts.forms import UserChangeForm
from accounts.models import User



def edit(request):
    args = {}
    args['form'] = UserChangeForm(instance=request.user)
    args['user'] = request.user
    args['username'] = auth.get_user(request).username
    args['id_email'] = request.user.email
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
    return render_to_response('edit.html', args)


def user_page(request, username):
    argv = {}
    argv['user'] = auth.get_user(request)

    return render_to_response('user_page.html', argv)
