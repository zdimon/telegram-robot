from django.contrib import admin
from .models import Room, RoomMessage, Keywords
from django.urls import path
from django.http import HttpResponseRedirect
# Register your models here.

from tr.settings import API_ID, SECRET_KEY, SESSION_NAME
from main.models import Room
from telethon import TelegramClient



def import_channels():
    client = TelegramClient(SESSION_ROOM_NAME,API_ID,SECRET_KEY)
    client.start()
    for room in client.iter_dialogs():
        #print(room)
        try:
            Room.objects.get(name=room.name)
        except:
            r = Room()
            r.id_key = str(room.id).replace('-','')
            r.name = room.name
            r.alias = room.name
            r.save()

class RoomAdmin(admin.ModelAdmin):
    list_display = ['name', 'id_key', 'alias', 'is_active']
    list_editable = ('is_active', 'alias')
    search_fields = ['name']
    list_filter = [ 'is_active' ]
    change_list_template = "admin/get_room.html"
    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('getrooms/', self.get_rooms),
        ]
        return my_urls + urls
    def get_rooms(self, request):
        import_channels()
        self.message_user(request, "Новые каналы импортированы!")
        return HttpResponseRedirect("../")


admin.site.register(Room, RoomAdmin)

class RoomMessageAdmin(admin.ModelAdmin):
    list_display = ['room', 'message']
    list_filter = [ 'room' ]


admin.site.register(RoomMessage, RoomMessageAdmin)

class KeywordsAdmin(admin.ModelAdmin):
    list_display = ['name']



admin.site.register(Keywords, KeywordsAdmin)
