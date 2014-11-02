from django.http import HttpResponse

# Create your views here.
from django.shortcuts import redirect
from django.template import Context
from django.template.loader import get_template
from django.core.context_processors import csrf
from django.contrib import auth
from mainpage.models import Regions
from accounts.forms import UserChangeForm
from accounts.forms import UserAvatarChangeForm

def home(request):
    args = {}
    args.update(csrf(request))
    if request.method == 'POST':
        form = UserAvatarChangeForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
        else:
            args['form'] = UserAvatarChangeForm(request.POST)
        args['form'] = form
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
        "form":UserChangeForm(),

    })
    c.update(csrf(request))
    svg = t.render(c)
    r = HttpResponse(svg)

    r['Content-Type'] = "image/svg+xml"
    return HttpResponse(r,args)


def main_east(request):
    r = redirect('/')
    r.set_cookie('world', 'main_east')
    return r


def main_west(request):
    r = redirect('/')
    r.set_cookie('world', 'main_west')
    return r

