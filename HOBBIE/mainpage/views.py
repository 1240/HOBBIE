from django.db.models import Q
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
    q = None
    search_string = geoip_record.region.name.split(' ')[0]
    if (search_string != None):
        for word in search_string.split():
            q_aux = Q(region_name__icontains=word) | Q(region_title__icontains=word)
            q = ( q_aux & q ) if bool(q) else q_aux
    region = Regions.objects.filter(q)

    args = {}
    args.update(csrf(request))
    if request.method == 'POST':
        user_avatar_change_form = UserAvatarChangeForm(request.POST, request.FILES, instance=request.user)
        if user_avatar_change_form.is_valid():
            user_avatar_change_form.save()
        else:
            args['user_avatar_change_form'] = UserAvatarChangeForm(request.POST)
        args['user_avatar_change_form'] = user_avatar_change_form
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
        "user_avatar_change_form": UserAvatarChangeForm(),
        "ip": region[0].region_name,
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

