# Create your views here.
from django.shortcuts import render_to_response
from room.models import Room, Message


def rooms(request):
    return render_to_response('rooms.html', {'rooms': Room.objects.all()})


def room(request, room_id=1):
    return render_to_response('room.html', {'room': Room.objects.get(id=room_id),
                                            'messages': Message.objects.filter(message_room_id=room_id)})