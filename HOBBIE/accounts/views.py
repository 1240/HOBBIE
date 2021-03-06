from django.contrib import auth
from django.core.context_processors import csrf
from django.core.files import File
from django.core.paginator import Paginator
from django.shortcuts import redirect, render_to_response, render

# Create your views here.
from accounts.forms import UserChangeForm
from accounts.models import User, UserRoom
from mainpage.models import Regions
from room.models import Room
from utils.utils import create_image


def edit(request):
    args = {}
    user = auth.get_user(request)
    args.update(csrf(request))
    user_change_form = UserChangeForm(instance=request.user)
    user_change_form.avatar = user.avatar
    args['form'] = user_change_form
    args['userreg'] = user.region_id
    args['header'] = 'Редактирование информации - %s' % user.username
    args['regions_list'] = Regions.objects.all()
    if request.method == 'POST':
        form = UserChangeForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            user = User.objects.get(id=auth.get_user(request).id)
            user.region_id = request.POST.get('region_select')
            f = open(create_image(user.username, user.username), 'rb')
            username_image = File(f)
            user.username_image.save(user.username + '.png', username_image)
            user.avatar = form.cleaned_data['avatar']
            user.save()
            args = {}
            args['user'] = auth.get_user(request)
            f.close()
            return redirect('/account/%s/' % auth.get_user(request).username, args)
        else:
            args['form'] = UserChangeForm(request.POST)
        args['form'] = form
    return render(request, 'edit.html', args)


def user_page(request, username):
    user = User.objects.get(username=username)
    current_page = Paginator(
        Room.objects.filter(user=user, userroom__message_text__isnull=True).order_by("-room_create_date"), per_page=10)
    args = {}
    args['rooms'] = current_page.page(1)
    args['friends'] = user.friends.all()
    args['account'] = user
    args['username'] = username.title()
    return render(request, 'user_page.html', args)


def friends(request):
    args = {}
    user = auth.get_user(request)
    args['user'] = user
    args['friends'] = user.friends.all()
    args['header'] = 'Ваши друзья'
    return render(request, 'friends.html', args)


def rooms(request):
    user = auth.get_user(request)
    current_page = Paginator(Room.objects.filter(user=user, userroom__message_text__isnull=True)
                             .order_by("-room_create_date"), per_page=10)
    args = {}
    args['rooms'] = current_page.page(1)
    args['toggle'] = 'notchecked'
    args['header'] = 'Ваши комнаты'
    return render(request, 'account_rooms.html', args)


def users(request):
    args = {}
    args['users'] = User.objects.all()
    args['header'] = 'Поиск пользователя'
    return render(request, 'users.html', args)


def invites(request):
    user = auth.get_user(request)
    current_page = Paginator(UserRoom.objects.filter(invite=1, user=user)
                             .order_by("-message_datetime"), per_page=10)
    args = {}
    args['header'] = 'Ваши приглашения'
    args['user_rooms'] = current_page.page(1)
    return render(request, 'invites.html', args)