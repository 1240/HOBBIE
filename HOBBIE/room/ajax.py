# -*- coding: utf-8 -*-
import json

from dajax.core import Dajax
from dajaxice.decorators import dajaxice_register
from django.core.paginator import Paginator
from django.template.loader import render_to_string
from django.core.context_processors import csrf

from room.models import Room, Message
from room.forms import MessageForm


_author__ = '1240'


@dajaxice_register
def rooms_list(request):
    json_string = request.POST.get('argv')
    argv = json.loads(json_string)

    toggle = argv.get('toggle')
    region_index = argv.get('region')
    page_number = argv.get('p')
    view = argv.get('view')
    per_page = 10
    toggles = {
        'by_date': '-room_create_date',
        'by_people': '-room_people_count',
    }
    if region_index:
        current_page = Paginator(object_list=Room.objects.filter(room_region_id=argv.get('region'))
                                 .order_by(toggles[toggle]), per_page=per_page)
    else:
        current_page = Paginator(object_list=Room.objects.all()
                                 .order_by(toggles[toggle]), per_page=per_page)
    views = {
        'gallery_view': 'rooms_ul.html',
        'table_view': 'rooms_div.html',
        'list_view': 'rooms_div.html',
    }

    args = {}
    args['rooms'] = current_page.page(page_number)

    render = render_to_string(views[view], args)

    dajax = Dajax()
    dajax.assign('#rooms', 'innerHTML', render)

    return dajax.json()


@dajaxice_register
def send_message(request):
    json_string = request.POST.get('argv')
    argv = json.loads(json_string)

    room_id = argv.get('room_id')
    message_text = argv.get('message_text')
    room = Room.objects.get(id=room_id)
    message = Message(message_text=message_text, message_room=room)
    message.save()

    messages = Message.objects.filter(message_room_id=room_id).order_by('message_datetime')

    args = {}
    args['messages'] = messages
    dajax = Dajax()
    dajax.assign('#messages_list', 'innerHTML', render_to_string('messages_list.html', args))
    return dajax.json()