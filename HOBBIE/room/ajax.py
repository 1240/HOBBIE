# -*- coding: utf-8 -*-
import json
import datetime

from dajax.core import Dajax
from dajaxice.decorators import dajaxice_register
from django.contrib import auth
from django.core.paginator import Paginator
from django.db.models import Q
from django.template.loader import render_to_string

from accounts.models import UserRoom
from room.models import Room,Category,RoomImage
from django.utils import timezone


_author__ = '1240'


@dajaxice_register
def rooms_list(request):
    json_string = request.POST.get('argv')
    argv = json.loads(json_string)
    categories = {
        'common': '1',
        'communications': '2',
        'sports': '3',
        'cult_ent': '4',
    }
    toggle = argv.get('toggle')
    region_index = argv.get('region')
    category_name = argv.get('category_name')
    page_number = argv.get('p')
    view = argv.get('view')
    search_string = argv.get('search_string')
    per_page = 10
    toggles = {
        'by_date': '-room_create_date',
        'by_people': '-room_people_count',
    }
    q = None
    q_aux = Q(category__category_title__in=categories) if category_name == 'all' else Q(category__category_title=category_name)
    q = ( q_aux & q ) if bool(q) else q_aux
    if region_index:
        q_aux = Q(room_region_id=region_index)
        q = ( q_aux & q ) if bool(q) else q_aux
        if (search_string != None):
            for word in search_string.split():
                q_aux = Q(room_title__icontains=word) | Q(hash_tags__icontains=word)
                q = ( q_aux & q ) if bool(q) else q_aux
        current_page = Paginator(object_list=Room.objects.filter(q)
                                 .order_by(toggles[toggle]), per_page=per_page)
    else:
        if (search_string != None):
            for word in search_string.split():
                q_aux = Q(room_title__icontains=word) | Q(hash_tags__icontains=word)
                q = ( q_aux & q ) if bool(q) else q_aux
        if (q == None):
            current_page = Paginator(object_list=Room.objects.filter(category__category_title__in=category_name)
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
def get_images_list(request):
    json_string = request.POST.get('argv')
    argv = json.loads(json_string)
    toggle = argv.get('toggle')

    toggles = {
        'by_common': 1,
        'by_communication': 2,
        'by_sports': 3,
        'by_cult_ent': 4,
    }
    args = {}
    imgs=RoomImage.objects.filter(roomimage_category_id=toggles[toggle])
    args['images']=imgs
    args['image_first_id']=imgs[0].id

    render =  render_to_string('image_choice_list.html', args)
    dajax = Dajax()
    dajax.assign('#imagechoicelist', 'innerHTML',render)

    return dajax.json()

@dajaxice_register
def send_message(request):
    json_string = request.POST.get('argv')
    argv = json.loads(json_string)

    room_id = argv.get('room_id')
    message_text = argv.get('message_text')
    #if len(message_text)>3:
    message_author = auth.get_user(request)
    room = Room.objects.get(id=room_id)
    message = UserRoom(message_text=message_text, room=room, user=message_author)

    message.save()

    return get_messages(request)

@dajaxice_register
def delete_message(request):
    json_string = request.POST.get('argv')
    argv = json.loads(json_string)

    message_id = argv.get('message_id')
    message = UserRoom(id=message_id)

    message.delete()

    return get_messages(request)

@dajaxice_register
def get_messages(request):
    json_string = request.POST.get('argv')
    argv = json.loads(json_string)


    user = auth.get_user(request)


    room_id = argv.get('room_id')
    room = Room.objects.get(id=room_id)
    messages = UserRoom.objects.filter(room_id=room_id, message_text__isnull=False).order_by('message_datetime')
    usinroom = []
    for userroom in UserRoom.objects.filter(room_id=room_id, message_text__isnull=True):
        usinroom.append(userroom.user)

    args = {}
    args['messages'] = messages
    args['room_id'] = room_id
    args['user']=user
    if user in usinroom:
        args['is_creator'] = UserRoom.objects.get(room=room, user=user, message_text__isnull=True)
        args['you_participant'] = 1
        if args['is_creator'].can_edit or args['is_creator'].is_creator:
            args['you_may_edit'] = 1

    for i in args['messages']:
        if i.message_datetime.date() == timezone.datetime.today().date():
            i.message_datetime = i.message_datetime.time()
        else:
            i.message_datetime = i.message_datetime.date()
    dajax = Dajax()
    dajax.assign('#messages_list', 'innerHTML', render_to_string('messages_list.html', args))
    return dajax.json()

