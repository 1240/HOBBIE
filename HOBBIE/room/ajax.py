# -*- coding: utf-8 -*-
import json
from dajax.core import Dajax
from dajaxice.decorators import dajaxice_register
from django.template.loader import render_to_string
from room.models import Room

_author__ = '1240'



@dajaxice_register
def rooms_list(request, toggle=''):
    json_string = request.POST.get('argv')
    argv = json.loads(json_string)
    if argv.get('toggle') == 'notchecked':
        rooms = Room.objects.order_by("-room_people_count")
        checked = 'checked'
    else:
        rooms = Room.objects.order_by("-room_create_date")
        checked = 'notchecked'

    args = {}
    args['rooms'] = rooms
    args['toggle'] = checked

    render = render_to_string('rooms_list.html', args)

    dajax = Dajax()
    dajax.assign('#rooms', 'innerHTML', render)

    return dajax.json()
