# -*- coding: utf-8 -*-
import json
from dajax.core import Dajax
from dajaxice.decorators import dajaxice_register
from django.contrib import auth
from django.core.context_processors import csrf
from django.core.paginator import Paginator
from django.shortcuts import redirect, render_to_response
from django.template.loader import render_to_string
from room.models import Room, Message

__author__ = '1240'


@dajaxice_register
def login(request):
    args = {}
    args.update(csrf(request))
    args['user'] = auth.get_user(request)
    args['is_authenticated'] = auth.get_user(request).is_authenticated()
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            args['login_error'] = "Пользователь не найден"
            return render_to_response('login.html', args)
    else:
        return render_to_response('login.html', args)

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
        current_page = Paginator(object_list=auth.get_user(request).room.all()
                                 .order_by(toggles[toggle]), per_page=per_page)
    else:
        current_page = Paginator(object_list=auth.get_user(request).room.all()
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