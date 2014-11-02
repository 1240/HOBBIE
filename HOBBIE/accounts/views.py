from django.contrib import auth
from django.core.context_processors import csrf
from django.core.paginator import Paginator
from django.shortcuts import redirect, render_to_response

# Create your views here.
from accounts.forms import UserChangeForm


def edit(request):
    args = {}
    args.update(csrf(request))
    args['form'] = UserChangeForm(instance=request.user)
    args['user'] = auth.get_user(request)
    if request.method == 'POST':
        form = UserChangeForm(request.POST, request.FILES, instance=request.user)
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
    return render_to_response('user_page.html', args)


def friends(request):
    args = {}
    user = auth.get_user(request)
    args['user'] = user
    args['friends'] = user.friends.all()
    return render_to_response('friends.html')


def rooms(request):
    user = auth.get_user(request)
    current_page = Paginator(object_list=user.room.all()
                             .order_by("-room_create_date"), per_page=10)
    args = {}
    args['rooms'] = current_page.page(1)
    args['toggle'] = 'notchecked'
    args['user'] = user
    return render_to_response('account_rooms.html', args)

