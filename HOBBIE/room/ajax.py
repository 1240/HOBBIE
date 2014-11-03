# -*- coding: utf-8 -*-
import json

from dajax.core import Dajax
from dajaxice.decorators import dajaxice_register
from django.core.paginator import Paginator
from django.db.models import Q
from django.template.loader import render_to_string

from room.models import Room, Message


_author__ = '1240'


@dajaxice_register
def rooms_list(request):
    json_string = request.POST.get('argv')
    argv = json.loads(json_string)

    toggle = argv.get('toggle')
    region_index = argv.get('region')
    page_number = argv.get('p')
    view = argv.get('view')
    search_string = argv.get('search_string')
    per_page = 10
    toggles = {
        'by_date': '-room_create_date',
        'by_people': '-room_people_count',
    }
    q = None
    if region_index:
        q_aux = Q(room_region_id=region_index)
        q = ( q_aux & q ) if bool(q) else q_aux
        if (search_string != None):
            for word in search_string.split():
                q_aux = Q(room_title__icontains=word) | Q(hash_tags__icontains=word) & Q(room_region_id=region_index)
                q = ( q_aux & q ) if bool(q) else q_aux
        current_page = Paginator(object_list=Room.objects.filter(q)
                                 .order_by(toggles[toggle]), per_page=per_page)
    else:
        if (search_string != None):
            for word in search_string.split():
                q_aux = Q(room_title__icontains=word) | Q(hash_tags__icontains=word)
                q = ( q_aux & q ) if bool(q) else q_aux
        if (q == None):
            current_page = Paginator(object_list=Room.objects.all()
                                     .order_by(toggles[toggle]), per_page=per_page)
        else:
            current_page = Paginator(object_list=Room.objects.filter(q)
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

    return get_messages(request)


@dajaxice_register
def get_messages(request):
    json_string = request.POST.get('argv')
    argv = json.loads(json_string)

    room_id = argv.get('room_id')
    messages = Message.objects.filter(message_room_id=room_id).order_by('message_datetime')

    args = {}
    args['messages'] = messages
    dajax = Dajax()
    dajax.assign('#messages_list', 'innerHTML', render_to_string('messages_list.html', args))
    return dajax.json()

