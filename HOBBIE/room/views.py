# Create your views here.

from django.contrib import auth
from django.core.context_processors import csrf
from django.core.paginator import Paginator
from django.shortcuts import redirect, render
from django.utils import timezone
from django.contrib.auth.decorators import login_required

from accounts.models import UserRoom
from accounts.models import User
from mainpage.models import Regions
from room.forms import MessageForm, RoomForm
from room.models import Room
from room.models import Category, RoomImage, CategoryRooms


def rooms(request, region_name='all', category_name='all'):
    categories = {
        'common': '1',
        'communications': '2',
        'sports': '3',
        'cult_ent': '4',
    }
    if region_name == 'all':
        region_title = 'по всей России'
        if category_name == 'all':
            current_page = Paginator(object_list=Room.objects
                                     .filter(category__category_title__in=categories)
                                     .order_by("-room_create_date"), per_page=10)
        else:
            current_page = Paginator(object_list=Room.objects
                                     .filter(category__category_title=category_name)
                                     .order_by("-room_create_date"), per_page=10)
    else:
        region = Regions.objects.filter(region_url='/' + region_name)
        region_title = region[0].region_title
        if category_name == 'all':
            current_page = Paginator(object_list=Room.objects
                                     .filter(category__category_title__in=categories,
                                             room_region__region_url='/' + region_name)
                                     .order_by("-room_create_date"), per_page=10)
        else:
            current_page = Paginator(object_list=Room.objects
                                     .filter(category__category_title=category_name,
                                             room_region__region_url='/' + region_name)
                                     .order_by("-room_create_date"), per_page=10)
    args = {}
    args['rooms'] = current_page.page(1)
    args['user'] = auth.get_user(request)
    args['toggle'] = 'notchecked'
    args['regions_list'] = Regions.objects.all()
    args['region_id'] = '/' + region_name
    args['header'] = 'Комнаты ' + region_title
    args['categories'] = Category.objects.all()

    return render(request, 'rooms.html', args)


def room(request, room_id=1):
    message_form = MessageForm
    args = {}
    args.update(csrf(request))
    user = auth.get_user(request)
    room = Room.objects.get(id=room_id)
    # if not room.room_open:
    # redirect('/rooms/all/all/')
    args['room'] = room
    args['messages'] = UserRoom.objects.filter(room_id=room_id, message_text__isnull=False, invite=0).order_by(
        'message_datetime')
    for i in args['messages']:
        if i.message_datetime.date() == timezone.datetime.today().date():
            i.message_datetime = i.message_datetime.time()
        else:
            i.message_datetime = i.message_datetime.date()
    categories = {
        1: 'Общая',
        2: 'Общение',
        3: 'Спорт',
        4: 'Культура/Развлечения'
    }
    category_room = CategoryRooms.objects.get(room=room)
    args['categ'] = categories[category_room.category.id]
    if user.is_authenticated():
        args['friends'] = user.friends.all()
    args['form'] = message_form
    args['user'] = user
    usinroom = User.objects.filter(userroom__room_id=room_id, userroom__message_text__isnull=True, userroom__invite=0)
    args['users_in_room'] = usinroom
    for x in UserRoom.objects.filter(room=room):
        if x.is_creator:
            args['creator'] = x.user.username
            if x.user.id == user.id:
                args['you_creator'] = 1
            break

    if user in usinroom:
        args['is_creator'] = UserRoom.objects.get(room=room, user=user, message_text__isnull=True, invite=0)
        args['you_participant'] = 1
        if args['is_creator'].can_edit or args['is_creator'].is_creator:
            args['you_may_edit'] = 1

    if args['room'].room_region_id == 0:
        args['room_region'] = 'Все регионы'
    else:
        args['room_region'] = Regions.objects.get(id=args['room'].room_region_id).region_name
    if args['room'].room_open == True:
        args['openclose'] = 'открытая'
    else:
        args['openclose'] = 'закрытая'
    return render(request, 'room.html', args)


@login_required(login_url='/auth/login/')
def makeroom(request):
    room_form = RoomForm
    args = {}
    args.update(csrf(request))
    args['form'] = room_form
    args['regions_list'] = Regions.objects.all()
    imgs = RoomImage.objects.filter(roomimage_category_id=1)
    args['images'] = imgs

    args['image_first_id'] = imgs[0].id

    return render(request, 'makeroom.html', args)


@login_required(login_url='/auth/login/')
def addroom(request):
    if request.POST:
        form = RoomForm(request.POST)
        if form.is_valid():
            room = form.save(commit=False)
            # img_choice = request.POST.get('action_image')
            # room.room_image = f(img_choice)
            room.room_region_id = request.POST.get('region_select')
            categ = request.POST.get('view')
            categories = {
                'common': 1,
                'communication': 2,
                'sports': 3,
                'cult_ent': 4
            }
            category = Category.objects.get(id=categories[categ])
            imgid = request.POST.get('action_image')
            room.room_image = imgid
            if category.id == 1:
                category.category_room_count = len(CategoryRooms.objects.all())
            else:
                category.category_room_count += 1
            category.save()

            if request.POST.get('openclose'):
                room.room_open = False
            else:
                room.room_open = True
            form.save()
            user = auth.get_user(request)
            room = Room.objects.get(id=room.id)
            category_room = CategoryRooms(room=room, category=category)
            category_room.save()
            user_room = UserRoom(
                room=room,
                user=user,
                is_creator=True,
                can_edit=True
            )
            user_room.save()
        else:
            return redirect('/rooms/all/')
    return redirect('/rooms/get/%s' % room.id)


@login_required(login_url='/auth/login/')
def joinroom(request, room_id):
    user = auth.get_user(request)
    room = Room.objects.get(id=room_id)

    # user.room.add(room)
    user_room = UserRoom(
        room=room,
        user=user,
        is_creator=False,
        can_edit=False
    )
    user_room.save()
    usinroom = []
    for userroom in UserRoom.objects.filter(room_id=room_id, message_text__isnull=True):
        usinroom.append(userroom.user)
    room.room_people_count = len(usinroom)
    room.save()
    return redirect('/rooms/get/%s/' % room_id)


@login_required(login_url='/auth/login/')
def leave(request, room_id):
    user = auth.get_user(request)
    room = Room.objects.get(id=room_id)
    # auth.get_user(request).room.remove(Room.objects.get(id=room_id))
    user_room = UserRoom.objects.get(room=room, user=user, message_text__isnull=True)

    user_room.delete()  # если нашел
    usinroom = []
    for userroom in UserRoom.objects.filter(room_id=room_id, message_text__isnull=True):
        usinroom.append(userroom.user)
    room.room_people_count = len(usinroom)
    room.save()
    return redirect('/rooms/get/%s/' % room_id)


@login_required(login_url='/auth/login/')
def invite(request, room_id):
    return redirect('/rooms/get/%s/' % room_id)


@login_required(login_url='/auth/login/')
def editroom(request, room_id):
    user = auth.get_user(request)
    room = Room.objects.get(id=room_id)
    user_room = UserRoom.objects.get(room=room, user=user, message_text__isnull=True)
    if not user_room.can_edit:
        return redirect('/rooms/get/%s' % room_id)
    args = {}
    args.update(csrf(request))
    args['form'] = RoomForm(instance=Room.objects.get(id=room_id))
    if Room.objects.get(id=room_id).room_open:
        args['open'] = ''
    else:
        args['open'] = 'checked'

    args['nofimage'] = Room.objects.get(id=room_id).room_image

    args['roomreg'] = Room.objects.get(id=room_id).room_region_id
    args['regions_list'] = Regions.objects.all()
    category_room = CategoryRooms.objects.get(room=room)
    args['categ'] = category_room.category.id
    imgs = RoomImage.objects.filter(roomimage_category_id=category_room.category.id)

    args['images'] = imgs

    if request.method == 'POST':
        form = RoomForm(request.POST, instance=Room.objects.get(id=room_id))
        if form.is_valid():
            form.save()
            # img_choice = request.POST.get('action_image')
            room = Room.objects.get(id=room_id)
            # room.room_image = f(img_choice)
            room.room_region_id = request.POST.get('region_select')
            categ = request.POST.get('view')
            categories = {
                'common': 1,
                'communication': 2,
                'sports': 3,
                'cult_ent': 4
            }
            category = Category.objects.get(id=categories[categ])
            imgid = request.POST.get('action_image')
            room.room_image = imgid
            category_room = CategoryRooms.objects.get(room=room)
            if category_room.category != category:
                # Category.objects.get(id=category_room.category.id).category_room_count-=1
                category_room.category = category
                # category.category_room_count+=1

            # category.category_room_count+=1    если категория прежняя, ниче не делать, если изменилась +1
            category.save()
            category_room.save()
            if request.POST.get('openclose'):
                room.room_open = False
            else:
                room.room_open = True
            room.save()
            return redirect('/rooms/get/%s' % room_id)
        else:
            args['form'] = RoomForm(request.POST)
        args['form'] = form
    return render(request, 'editroom.html', args)
