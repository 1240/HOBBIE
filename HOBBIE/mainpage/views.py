import mimetypes
from django.http import HttpResponse

# Create your views here.
from django.template import Context
from django.template.loader import get_template


def home2(request):
    t = get_template('map.svg')
    c = Context({
    "width": 621,
    })
    svg = t.render(c)
    r = HttpResponse(svg)
    r['Content-Type'] = "image/svg+xml"
    return HttpResponse(r)


def home1(request):
    t = get_template('test.html')
    c = Context({
    "width": 621,
    })
    svg = t.render(c)
    r = HttpResponse(svg)
    r['Content-Type'] = "image/svg+xml"
    return HttpResponse(r)


def home(request):
    t = get_template('main_page.html')
    c = Context({
    "width": 621,
    })
    svg = t.render(c)
    r = HttpResponse(svg)
    r['Content-Type'] = "image/svg+xml"
    return HttpResponse(r)
