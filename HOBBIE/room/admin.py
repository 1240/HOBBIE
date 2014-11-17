from django.contrib import admin
# Register your models here.
from accounts.models import UserRoom
from room.models import Room
from room.models import Category,CategoryRooms,RoomImage


class RoomMessage(admin.StackedInline):
    model = UserRoom
    extra = 1

class RoomImage(admin.StackedInline):
    model = RoomImage
    extra = 1

class CategoryAdmin(admin.ModelAdmin):
    fields = ['category_title', 'category_image']
    inlines = [RoomImage]
    list_display = ('__unicode__', )

class RoomAdmin(admin.ModelAdmin):
    fields = ['room_title', 'room_text', 'room_to_date', 'room_region']
    inlines = [RoomMessage]
    list_filter = ['room_title', 'room_text', 'room_to_date', 'room_create_date']
    list_display = ('__unicode__', 'room_text', 'room_to_date', 'room_create_date')
    search_fields = ['id', 'room_title']


admin.site.register(Room, RoomAdmin)
admin.site.register(Category, CategoryAdmin)
