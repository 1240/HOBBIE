# Create your views here.
from django.core.context_processors import csrf
from django.shortcuts import render_to_response, redirect

from room.forms import MessageForm

from room.models import Room, Message


def rooms(request):
    return render_to_response('rooms.html', {'rooms': Room.objects.all()})


def room(request, room_id=1):
    message_form = MessageForm
    args = {}
    args.update(csrf(request))
    args['room'] = Room.objects.get(id=room_id)
    args['messages'] = Message.objects.filter(message_room_id=room_id).order_by('message_datetime')
    args['form'] = message_form
    return render_to_response('room.html', args)


def addmessage(request, room_id):
    if request.POST:
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.message_room = Room.objects.get(id=room_id)
            form.save()
    return redirect('/rooms/get/%s/' % room_id)