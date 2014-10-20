from django.http import HttpResponse

# Create your views here.
from django.shortcuts import render_to_response
from django.template import Context
from django.template.loader import get_template


def room_one(request):
    view = "room_one"
    html = "<hml><body>THIS IS %s ROOM</hml></body>" % view
    return HttpResponse(html)


def template(request):
    view = "template"
    template = get_template('room.html')
    html = template.render(Context({'number': view}))
    return HttpResponse(html)

def home(request):
    view = "main page"
    return render_to_response('room.html', {'number': view})