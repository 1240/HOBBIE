from django.contrib import auth
from django.core.context_processors import csrf
from django.core.files import File
from django.core.paginator import Paginator
from django.shortcuts import redirect, render_to_response, render

# Create your views here.
from accounts.forms import UserChangeForm
from accounts.models import User, UserRoom
from room.models import Room
from utils.utils import create_image


def edit(request):
    args = {}
    args.update(csrf(request))
    args['form'] = UserChangeForm(instance=request.user)
    args['user'] = auth.get_user(request)
    if request.method == 'POST':
        form = UserChangeForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            user = User.objects.get(id=auth.get_user(request).id)
            f = open(create_image('%s %s' % (user.first_name, user.last_name), user.first_name, W=500), 'rb')
            name_image = File(f)
            user.name_image.save(user.username + '_name.png', name_image)
            f = open(create_image(user.username, user.username), 'rb')
            username_image = File(f)
            user.username_image.save(user.username + '.png', username_image)
            user.save()
            args = {}
            args['user'] = auth.get_user(request)
            f.close()
            return redirect('/account/%s/' % auth.get_user(request).username, args)
        else:
            args['form'] = UserChangeForm(request.POST)
        args['form'] = form
    return render_to_response('edit.html', args)


def user_page(request, username):
    args = {}
    args['account'] = User.objects.get(username=username)
    return render(request, 'user_page.html', args)


def friends(request):
    args = {}
    user = auth.get_user(request)
    args['user'] = user
    args['friends'] = user.friends.all()
    args['header'] = 'Ваши друзья'
    return render_to_response('friends.html', args)


def rooms(request):
    user = auth.get_user(request)
    current_page = Paginator(Room.objects.filter(user=user, userroom__message_text__isnull=True)
                             .order_by("-room_create_date"), per_page=10)
    args = {}
    args['rooms'] = current_page.page(1)
    args['toggle'] = 'notchecked'
    return render(request, 'account_rooms.html', args)


def users(request):
    args = {}
    args['users'] = User.objects.all()
    args['header'] = 'Поиск пользователя'
    return render(request, 'users.html', args)