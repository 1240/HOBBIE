# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

from room.models import Room


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
    avatar = models.ImageField(verbose_name='Аватар', upload_to='images/%Y/%m/%d', blank=True, null=True, default='/media/images/avatar.jpg')
    name_image = models.ImageField(upload_to='images/name_image/%Y/%m/%d', blank=True, null=True)
    username_image = models.ImageField(upload_to='images/username_image/%Y/%m/%d', blank=True, null=True)
    first_name = models.CharField(verbose_name='Имя', max_length=255, blank=True)
    last_name = models.CharField(verbose_name='Фамилия', max_length=255, blank=True)
    date_of_birth = models.DateField(verbose_name='День рождения', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    friends = models.ManyToManyField("self", blank=True, null=True)
    room = models.ManyToManyField(Room,  through='UserRoom', null=True)
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

    @property
    def is_staff(self):
        return self.is_admin


class UserRoom(models.Model):
    room = models.ForeignKey(Room)
    user = models.ForeignKey(User)
    is_creator = models.BooleanField(default=False)
    can_edit = models.BooleanField(default=False)