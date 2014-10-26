from django.contrib import admin
# Register your models here.
from room.models import Room, Message


class RoomMessage(admin.StackedInline):
    model = Message
    extra = 1


class RoomAdmin(admin.ModelAdmin):
    fields = ['room_title', 'room_text', 'room_to_date', 'room_region']
    inlines = [RoomMessage]
    list_filter = ['room_title', 'room_text', 'room_to_date', 'room_create_date']

admin.site.register(Room, RoomAdmin)
