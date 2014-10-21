from django.http import HttpResponse

# Create your views here.
from django.shortcuts import render_to_response
from django.template import Context
from django.template.loader import get_template
from room.models import Room, Message


def room_one(request):
    view = "room_one"
    html = "<hml><body>THIS IS %s ROOM</hml></body>" % view
    return HttpResponse(html)


def template(request):
    view = "template"
    template = get_template('test.html')
    html = template.render(Context({'number': view}))
    return HttpResponse(html)


def home(request):
    view = "main page"
    return render_to_response('test.html', {'number': view})


def rooms(request):
    return render_to_response('rooms.html', {'rooms': Room.objects.all()})


def room(request, room_id=1):
    return render_to_response('room.html', {'room': Room.objects.get(id=room_id),
                                            'messages': Message.objects.filter(message_room_id=room_id)})