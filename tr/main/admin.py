from django.contrib import admin
from .models import Room, RoomMessage, Keywords
# Register your models here.

class RoomAdmin(admin.ModelAdmin):
    list_display = ['name', 'id_key', 'alias', 'is_active']
    list_editable = ('is_active', 'alias')
    search_fields = ['name']
    list_filter = [ 'is_active' ]


admin.site.register(Room, RoomAdmin)

class RoomMessageAdmin(admin.ModelAdmin):
    list_display = ['room', 'message']
    list_filter = [ 'room' ]


admin.site.register(RoomMessage, RoomMessageAdmin)

class KeywordsAdmin(admin.ModelAdmin):
    list_display = ['name']



admin.site.register(Keywords, KeywordsAdmin)
