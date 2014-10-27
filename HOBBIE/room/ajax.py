# -*- coding: utf-8 -*-
import json
from dajax.core import Dajax
from dajaxice.decorators import dajaxice_register
from django.core.paginator import Paginator
from django.template.loader import render_to_string
from room.models import Room,Message
from room.forms import MessageForm
from django.core.context_processors import csrf
from django.db.models import fields

_author__ = '1240'



@dajaxice_register
def rooms_list(request):
    json_string = request.POST.get('argv')
    argv = json.loads(json_string)

    if argv.get('toggle'):
        rooms = Room.objects.order_by("-room_people_count")
        checked = 'checked'
    else:
        rooms = Room.objects.order_by("-room_create_date")
        checked = 'notchecked'

    if (argv.get('region')):
        rooms = rooms.filter(room_region_id=argv.get('region'))

    page_number = argv.get('p')
    current_page = Paginator(object_list=rooms, per_page=2)
    args = {}
    args['rooms'] = current_page.page(page_number)

    render = render_to_string('rooms_list.html', args)

    dajax = Dajax()
    dajax.assign('#rooms', 'innerHTML', render)

    return dajax.json()

def chat(request,room_id=0):
    json_string = request.POST.get('argv')
    argv = json.loads(json_string)

    form = MessageForm
    if form.is_valid():
            message = form.save(commit=False)
            message.message_room = Room.objects.get(id=room_id)
            form.save()

    args = {}

    args.update(csrf(request))

    args['messages'] = Message.objects.filter(message_room_id=room_id).order_by('message_datetime')

    dajax = Dajax()
    dajax.assign('#chat', 'innerHTML', render_to_string('chat.html', args))
    return dajax.json()
