from django.contrib import auth
from django.utils import timezone

from accounts.models import UserRoom
from room.models import Room, HashTags


__author__ = '1240'


def invite_count(request):
    return {
        "invite_counts": len(
            UserRoom.objects.filter(room_id__isnull=False, invite='1', user_id=auth.get_user(request).id))
    }


def room_soon(request):
    rooms_soon = Room.objects.filter(room_to_date__gte=timezone.now()).exclude(room_to_date__day=timezone.now().day).order_by('room_to_date')[:5]
    for a in rooms_soon:
        a.room_to_date = a.room_to_date.date()

    return {
        "rooms_soon": rooms_soon
    }


def room_today(request):
    rooms_today = Room.objects.filter(room_to_date__day=timezone.now().day).order_by('room_to_date')[:5]
    for a in rooms_today:
        a.room_to_date = a.room_to_date.time()

    return {
        "rooms_today": rooms_today
    }


def popular_hash_tags(request):
    return  {
        "hash_tags": HashTags.objects.all().order_by('count')[:10]
    }