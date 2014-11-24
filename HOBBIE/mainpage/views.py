from django.db.models import Q
from django.http import HttpResponse

# Create your views here.
from django.shortcuts import redirect
from django.template import Context
from django.template.loader import get_template
from django.core.context_processors import csrf
from django.contrib import auth
from django.utils import timezone
from django_geoip.models import IpRange
from accounts.models import UserRoom
from mainpage.models import Regions
from accounts.forms import UserAvatarChangeForm
from room.models import Room, HashTags

kirov_ip = "37.113.83.1"
localhost_ip = "127.0.0.1"


def home(request):
    ip = get_client_ip(request)
    if get_client_ip(request) == localhost_ip:
        ip = kirov_ip
    geoip_record = IpRange.objects.by_ip(ip)
    q = None
    search_string = geoip_record.region.name.split(' ')[0]
    if (search_string != None):
        for word in search_string.split():
            q_aux = Q(region_name__icontains=word) | Q(region_title__icontains=word)
            q = ( q_aux & q ) if bool(q) else q_aux
    region = Regions.objects.filter(q)
    user = auth.get_user(request)
    rooms_soon = Room.objects.filter(room_to_date__gte=timezone.now()).order_by('room_to_date')[:5]
    for a in rooms_soon:
        a.room_to_date = a.room_to_date.date()
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
        "invite_counts": len(UserRoom.objects.filter(room_id__isnull=False, invite='1', user_id=user.id)),
        "current_region": region[0],
        "hash_tags": HashTags.objects.all()[:10],
        "rooms_soon": rooms_soon,
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


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
