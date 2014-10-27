# Create your views here.
from django import forms
from django.contrib import auth
from django.core.context_processors import csrf
from django.db.models import fields
from django.shortcuts import render_to_response, redirect
from django.template.loader import select_template
from mainpage.models import Regions

from room.forms import MessageForm, RoomForm

from room.models import Room, Message


def rooms(request):
    if 'toggle' in request.GET:
        checked = 'checked'
    else:
        checked = 'notchecked'
    if (checked == 'notchecked'):
        rooms = Room.objects.order_by("-room_create_date")
    else:
        rooms = Room.objects.order_by("-room_people_count")
    args = {}
    args['rooms'] = rooms
    args['username'] = auth.get_user(request).username
    args['toggle'] = checked
    args['regions_list'] = Regions.objects.all()
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
            #message = form.save(commit=False)
            #message.message_room = Room.objects.get(id=room_id)
            form.save()
    return redirect('/rooms/all/')


def joinroom(request, room_id):
    return redirect('/rooms/get/%s/' % room_id)


def invite(request, room_id):
    return redirect('/rooms/get/%s/' % room_id)