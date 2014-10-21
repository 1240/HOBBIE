import mimetypes
from django.http import HttpResponse

# Create your views here.
from django.template import Context
from django.template.loader import get_template


def home(request):
    t = get_template('map.svg')
    c = Context({
    "width": 621,
    })
    svg = t.render(c)
    r = HttpResponse(svg)
    r['Content-Type'] = "image/svg+xml"
    return HttpResponse(r)
