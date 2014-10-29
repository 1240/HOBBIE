from django.contrib import auth
from django.core.context_processors import csrf
from django.shortcuts import render, redirect, render_to_response

# Create your views here.
from accounts.forms import UserChangeForm
from accounts.models import User



def edit(request):
    args = {}
    args.update(csrf(request))
    args['form'] = UserChangeForm(instance=request.user)
    args['username'] = auth.get_user(request).username
    if request.method == 'POST':
        form = UserChangeForm(request.POST,request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            args = {}
            args['user'] = auth.get_user(request)
            return redirect('/account/%s/' % auth.get_user(request).username, args)
        else:
            args['form'] = UserChangeForm(request.POST)
        args['form'] = form
    return render_to_response('edit.html', args)


def user_page(request, username):
    args = {}
    args['user'] = auth.get_user(request)
    args['username'] = auth.get_user(request).username
    return render_to_response('user_page.html', args)
