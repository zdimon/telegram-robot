from django.core.management.base import BaseCommand, CommandError
from telethon import TelegramClient, events
from tr.settings import API_ID, SECRET_KEY
from main.models import Room, RoomMessage
import asyncio

#client = TelegramClient('session_name',API_ID,SECRET_KEY)
client = TelegramClient('zdimon_session',API_ID,SECRET_KEY)

async def get_channel():
    #channel = await client.get_entity('test_group')
    #print(channel)
    messages = await client.get_messages('t.me/test_wezom_group', limit=60)
    for m in messages:
        if(m.message):
            print(m.message)
    #return channel


def get_message_list(room):
    print('Process room %s' % room)
    channel = get_channel(room)
    
    '''
    for mes in client.iter_messages(room.name):
        print(mes)
        #if str(mes.to_id.channel_id) == room.id_key:
        
        m = RoomMessage()
        m.message = mes.text
        m.room = room
        m.sender_id = mes.sender_id
        m.save()
        print(mes.text)
        print(mes.sender_id)

    '''
    





class Command(BaseCommand):

    def handle(self, *args, **options):
        print('Getting messages')
        client.start()
        RoomMessage.objects.all().delete()


        #ioloop = asyncio.get_event_loop()
        #tasks = [
        #   ioloop.create_task(get_channel())
        #]
        #ioloop.run_until_complete(asyncio.wait(tasks))
        #ioloop.close()


        #for room in Room.objects.filter(is_active=True):
        #    get_message_list(room)
        #client.run_until_complete()    
        #client.run_until_disconnected()
        
