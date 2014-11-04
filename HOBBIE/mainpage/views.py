from django.http import HttpResponse

# Create your views here.
from django.shortcuts import redirect
from django.template import Context
from django.template.loader import get_template
from django.core.context_processors import csrf
from django.contrib import auth
from django_geoip.models import IpRange
from mainpage.models import Regions
from accounts.forms import UserAvatarChangeForm

ip = "37.113.83.1"

def home(request):
    geoip_record = IpRange.objects.by_ip(ip)
    args = {}
    args.update(csrf(request))
    if request.method == 'POST':
        form1 = UserAvatarChangeForm(request.POST, request.FILES, instance=request.user)
        if form1.is_valid():
            form1.save()
        else:
            args['form1'] = UserAvatarChangeForm(request.POST)
        args['form1'] = form1
    if 'main_east' == request.COOKIES.get('world'):
        regions = Regions.objects.filter(is_west=False)
        t = get_template('main_east.html')

    else:
        regions = Regions.objects.filter(is_west=True)
        t = get_template('main_west.html')
    c = Context({
        "width": 621,
        "user": auth.get_user(request),
        "regions": regions,
        "id_user": auth.get_user(request).id,
        "form1": UserAvatarChangeForm(),
        "ip": geoip_record.region,
    })
    c.update(csrf(request))
    svg = t.render(c)
    r = HttpResponse(svg)

    r['Content-Type'] = "image/svg+xml"
    return HttpResponse(r, args)


def main_east(request):
    r = redirect('/')
    r.set_cookie('world', 'main_east')
    return r


def main_west(request):
    r = redirect('/')
    r.set_cookie('world', 'main_west')
    return r

