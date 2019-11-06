from django.core.management.base import BaseCommand, CommandError
from telethon import TelegramClient, events
from tr.settings import API_ID, SECRET_KEY, SESSION_NAME
from main.models import Room, RoomMessage
import asyncio
client = TelegramClient(SESSION_NAME,API_ID,SECRET_KEY)

async def send_message(group):
    await client.send_message(group, 'helooooooooo')

class Command(BaseCommand):

    def handle(self, *args, **options):
        print('Sending message')    

        client.start()
        ioloop = asyncio.get_event_loop()
        tasks = [
           ioloop.create_task(send_message('test_group_wezom'))
        ]       
        ioloop.run_until_complete(asyncio.wait(tasks)) 
        ioloop.close()