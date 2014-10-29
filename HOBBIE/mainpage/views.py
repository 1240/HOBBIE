from django.http import HttpResponse

# Create your views here.
from django.shortcuts import redirect
from django.template import Context
from django.template.loader import get_template
from django.contrib import auth
from mainpage.models import Regions


def home(request):
    if 'main_east' == request.COOKIES.get('world'):
        regions = Regions.objects.filter(is_west=False)
        t = get_template('main_east.html')
    else:
        regions = Regions.objects.filter(is_west=True)
        t = get_template('main_west.html')
    c = Context({
        "width": 621,
        "username": auth.get_user(request).username,
        "regions": regions,
        "id_user": auth.get_user(request).id,
    })
    svg = t.render(c)
    r = HttpResponse(svg)
    r['Content-Type'] = "image/svg+xml"
    return HttpResponse(r)


def main_east(request):
    r = redirect('/')
    r.set_cookie('world', 'main_east')
    return r


def main_west(request):
    r = redirect('/')
    r.set_cookie('world', 'main_west')
    return r
