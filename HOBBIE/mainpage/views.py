from django.http import HttpResponse

# Create your views here.
from django.template import Context
from django.template.loader import get_template
from django.contrib import auth
from mainpage.models import Regions


def home(request):
    t = get_template('main_page.html')
    c = Context({
        "width": 621,
        "username": auth.get_user(request).username,
        "regions": Regions.objects.all(),
        "id_user": auth.get_user(request).id,
    })
    svg = t.render(c)
    r = HttpResponse(svg)
    r['Content-Type'] = "image/svg+xml"
    return HttpResponse(r)
