from django.core.management.base import BaseCommand, CommandError
from telethon import TelegramClient, events
from tr.settings import API_ID, SECRET_KEY
from main.models import Room, RoomMessage

client = TelegramClient('session_name',API_ID,SECRET_KEY)

def get_message_list(room):
    print('Process room %s' % room)
    RoomMessage.objects.all().delete()
    for mes in client.iter_messages(room.name):
        m = RoomMessage()
        m.message = mes.text
        m.room = room
        m.sender_id = mes.sender_id
        m.save()
        print(mes.text)
        print(mes.sender_id)
    

rooms = []
for room in Room.objects.filter(is_active=True):
    rooms.append(room.name)
print(rooms)
@client.on(events.NewMessage(chats=tuple(rooms)))
async def normal_handler(event):
    print('got message')
    message = event.message.to_dict()
    key = '100%s' % str(event.to_id.channel_id)
    print(key)
    room = Room.objects.get(id_key=key)
    
    m = RoomMessage()
    m.room = room
    m.message = message['message']
    m.save()
    print(message['message'])
    



class Command(BaseCommand):

    def handle(self, *args, **options):
        print('Getting messages')
        client.start()

        client.run_until_disconnected()
        
