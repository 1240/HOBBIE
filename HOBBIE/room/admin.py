from django.contrib import admin
# Register your models here.
from accounts.models import UserRoom
from room.models import Room
from room.models import Category,CategoryRooms


class RoomMessage(admin.StackedInline):
    model = UserRoom
    extra = 1

class CategoryAdmin(admin.ModelAdmin):
    fields = ['category_title', 'category_image']

class RoomAdmin(admin.ModelAdmin):
    fields = ['room_title', 'room_text', 'room_to_date', 'room_region']
    inlines = [RoomMessage]
    list_filter = ['room_title', 'room_text', 'room_to_date', 'room_create_date']


admin.site.register(Room, RoomAdmin)
admin.site.register(Category, CategoryAdmin)
