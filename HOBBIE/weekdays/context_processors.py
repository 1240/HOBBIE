from django.contrib import auth

__author__ = '1240'


def user_global(request):
    return {'user': auth.get_user(request)}
