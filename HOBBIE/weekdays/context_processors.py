from django.contrib import auth
from accounts.models import UserRoom

__author__ = '1240'


def user_global(request):
    return {'user': auth.get_user(request)}


def invite_count(request):
    return {
    "invite_counts": len(UserRoom.objects.filter(room_id__isnull=False, invite='1', user_id=auth.get_user(request).id))
    }