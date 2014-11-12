# -*- coding: utf-8 -*-
import math
import datetime
import os

from PIL import Image
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

from room.models import Room
from django.utils import timezone


class UserManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=UserManager.normalize_email(email),
            username=username)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(email,
                                password=password,
                                username=username)
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email',
        max_length=255,
        unique=True,
        db_index=True)
    username = models.CharField(verbose_name='username', max_length=255, unique=True)
    avatar = models.ImageField(verbose_name='Аватар', upload_to='images/%Y/%m/%d', blank=True, null=True,
                               default='images/avatar.jpg')
    username_image = models.ImageField(upload_to='images/username_image/%Y/%m/%d', blank=True, null=True)
    first_name = models.CharField(verbose_name='Имя', max_length=255, blank=True)
    last_name = models.CharField(verbose_name='Фамилия', max_length=255, blank=True)
    date_of_birth = models.DateField(verbose_name='День рождения', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    friends = models.ManyToManyField("self", blank=True, null=True)
    room = models.ManyToManyField(Room, through='UserRoom', null=True)
    # TODO сообщения

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def get_full_name(self):
        return '%s %s' % (self.first_name, self.last_name,)

    def get_short_name(self):
        return self.username

    def __unicode__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def save(self, *args, **kwargs):
        size=(225, 225)
        super(User, self).save()
        filename = str(self.avatar.path)
        image = Image.open(filename)

        W, H = image.size
        offset = round(math.fabs(W - H) / 2)
        if W > H:
            box = (offset, 0, offset + H, H)
        else:
            box = (0, offset, W, offset + W)
        image = image.crop(box)
        image.thumbnail(size, Image.ANTIALIAS)
        image.save(filename)
        super(User, self).save(*args, **kwargs)


    @property
    def is_staff(self):
        return self.is_admin


class UserRoom(models.Model):
    room = models.ForeignKey(Room)
    user = models.ForeignKey(User)
    is_creator = models.BooleanField(default=False)
    can_edit = models.BooleanField(default=False)
    message_text = models.TextField(verbose_name="Текст сообщения", null=True, blank=True)
    message_datetime = models.DateTimeField(default=timezone.now())
