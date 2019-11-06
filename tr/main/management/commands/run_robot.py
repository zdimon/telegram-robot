from django.core.management.base import BaseCommand, CommandError
from telethon import TelegramClient
from tr.settings import API_ID, SECRET_KEY
from main.models import Room

client = TelegramClient('session_name',API_ID,SECRET_KEY)

def room_list():
    Room.objects.all().delete()
    for room in client.iter_dialogs():
        #print(room.name)
        #print(room.id)
        r = Room()
        r.id_key = room.id
        r.name = room.name
        r.save()
        print('Saving in DB %s' % room.name)

class Command(BaseCommand):
    help = 'Running robot'




    def handle(self, *args, **options):
        print('Running robot')
        client.start()
        room_list()
        client.run_until_disconnected()
        
