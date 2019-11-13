from django.core.management.base import BaseCommand, CommandError
from telethon import TelegramClient, events
from tr.settings import API_ID, SECRET_KEY, SESSION_NAME, REPORT_CHANNEL
from main.models import Room, RoomMessage, Keywords
import asyncio
client = TelegramClient(SESSION_NAME,API_ID,SECRET_KEY)
client_sender = TelegramClient(SESSION_NAME,API_ID,SECRET_KEY)
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
    


def send_message(message):
    try:
        async def do_send(message):
            await client.send_message(REPORT_CHANNEL, message)

        client_sender.start()
        ioloop = asyncio.get_event_loop()
        tasks = [
            ioloop.create_task(do_send(message))
        ]       
        ioloop.run_until_complete(asyncio.wait(tasks)) 
        ioloop.close()    
    except Exception as e:
        print(str(e))

rooms = []
for room in Room.objects.filter(is_active=True):
    rooms.append(room.alias)
print(rooms)
@client.on(events.NewMessage(chats=tuple(rooms)))
async def normal_handler(event):
    print('got message')
    message = event.message.to_dict()
    print(message['message'])
    user = await client.get_entity(event.from_id)
    print(user.username)
    key = '100%s' % str(event.to_id.channel_id)
    room = Room.objects.get(id_key=key)
    m = RoomMessage()
    m.room = room
    m.message = message['message']
    m.save()

    
    for key in Keywords.objects.all():
        #print('searching %s' % key.name)
        rez = message['message'].find(key.name)
        #print(rez)
        if rez != -1:
            send_message('%s автор: @%s' % (message['message'],user.username))
   
    print(message['message'])
    

class Command(BaseCommand):

    def handle(self, *args, **options):
        print('Getting messages')
        client.start()
        client.run_until_disconnected()
        
