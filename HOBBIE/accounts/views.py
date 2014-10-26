from django.contrib import auth
from django.core.context_processors import csrf
from django.shortcuts import render, redirect, render_to_response

# Create your views here.
from accounts.forms import UserChangeForm
from accounts.models import User



def edit(request):
    args = {}
    args['form'] = UserChangeForm()
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
    name = {}
    name['user'] = request.user
    name['username'] = auth.get_user(request).username
    name['id_email'] = request.user.email
    name['first_name'] = request.user.first_name
    name['last_name'] = request.user.last_name
    name['date_of_birth'] = request.user.date_of_birth

    return render_to_response('user_page.html', name)
