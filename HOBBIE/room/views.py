# Create your views here.
from django.contrib import auth
from django.core.context_processors import csrf
from django.core.paginator import Paginator
from django.shortcuts import render_to_response, redirect

from mainpage.models import Regions
from room.forms import MessageForm, RoomForm
from room.models import Room, Message


def rooms(request, region_name='all'):
    if (region_name == 'all'):
        current_page = Paginator(object_list=Room.objects.order_by("-room_create_date"), per_page=10)
    else:
        region = Regions.objects.filter(region_url='/' + region_name)
        current_page = Paginator(object_list=Room.objects.filter(room_region=region)
                                 .order_by("-room_create_date"), per_page=10)
    args = {}
    args['rooms'] = current_page.page(1)
    args['username'] = auth.get_user(request).username
    args['toggle'] = 'notchecked'
    args['regions_list'] = Regions.objects.all()
    args['region_id'] = '/' + region_name
    return render_to_response('rooms.html', args)


def room(request, room_id=1):
    message_form = MessageForm
    args = {}
    args.update(csrf(request))
    args['room'] = Room.objects.get(id=room_id)
    args['messages'] = Message.objects.filter(message_room_id=room_id).order_by('message_datetime')
    args['form'] = message_form
    args['username'] = auth.get_user(request).username
    return render_to_response('room.html', args)


'''
def addmessage(request, room_id):
    if request.POST:
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.message_room = Room.objects.get(id=room_id)
            form.save()
    return redirect('/rooms/get/%s/' % room_id)'''


def makeroom(request):
    room_form = RoomForm
    args2 = {}
    args2.update(csrf(request))
    args2['form'] = room_form

    return render_to_response('makeroom.html', args2)


def addroom(request):
    if request.POST:
        form = RoomForm(request.POST)
        if form.is_valid():
            room = form.save(commit=False)
            room.room_image = request.POST.get('args')
            img_choice = request.POST.get('action_image')
            room.room_image = f(img_choice)
            room.room_region_id = 1  # TODO
            form.save()
    return redirect('/rooms/all/')


def f(x):
    return {
        'a1': 'img/1.png',
        'a2': 'img/2.png',
        'a3': 'img/3.png',
        'a4': 'img/4.png',
        'a5': 'img/5.png',
        'a6': 'img/6.png',
        'a7': 'img/7.png',
        'a8': 'img/8.png',
        'a9': 'img/9.png',
        'a10': 'img/10.png',
        'a11': 'img/11.png',
        'a12': 'img/12.png',
        'a13': 'img/13.png',
        'a14': 'img/14.png',
        'a15': 'img/15.png',
        'a16': 'img/16.png',
    }[x]


def joinroom(request, room_id):
    return redirect('/rooms/get/%s/' % room_id)


def invite(request, room_id):
    return redirect('/rooms/get/%s/' % room_id)