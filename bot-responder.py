import datetime
import time

from telethon import events
from telethon.sync import TelegramClient

import logging

from telethon.tl.types import Channel

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.INFO)



from decouple import config
api_id = config('api_id')
api_hash =config('api_hash')
bot_token = config('bot_token')
# We have to manually call "start" if we want an explicit bot token
bot_responder = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)


async def main():
    my_channel = await bot_responder.get_entity("tstngg")
    print("Entity found:", my_channel)
    await bot_responder.send_message(my_channel, 'Hello, myself!')
    print("Message sent")


@bot_responder.on(events.NewMessage())
async def ping_handler(event):

    message = event.message.message.lower()
    message_id = event.message.from_id
    media = await event.message.download_media()

    logging.info(f"Received message: {message} from id: {message_id}")
    file = event.message.file
    logging.info(media)
    reply = "I do not understand this message"

    if message == "ping":
        reply = "PONG"

    elif message == "time":
        reply = datetime.datetime.utcnow().strftime("%I:%M:%S %p")

    m = await event.reply(reply)

    time.sleep(5)

    await bot_responder.delete_messages(event.chat_id, [m.id])
    logging.info(f"Deleted")

    logging.info(f"Message sent: {reply}")

channel = bot_responder.get_entity(2091664821)

#for new messages on channel tstngg
# @bot_responder.on(events.NewMessage(chats=channel))
# async def channel_ping_handler(event):
#     my_channel = await bot_responder.get_entity("tstngg")
#     message = event.message.message.lower()
#
#     message_id = event.message.id
#     logging.info(f"Message received: {message_id}")
#     print(event.message)
#     reply = 'I do not understand this message'
#     if message == "ping":
#         reply = 'fuck'
#     elif message == "time":
#         reply = datetime.datetime.utcnow().strftime("%I:%M:")
#     elif message == "bonk":
#         reply = event.message.message
#     #await event.reply(reply)
#     await bot_responder.send_message('pm_141592', f'{message_id} sent {message} and got the reply {reply}')
    #logging.info(f'Message sent: ')

# @bot_responder.on(events.NewMessage(pattern=r'time'))
# async def time_handler(event):
#     logging.info("Received message: time")
#     # Respond whenever someone says "Hello" and something else
#     await event.reply(datetime.datetime.now().strftime('%I:%M:%S %p'))
#     logging.info("Message sent: current time")


# with bot_responder:
#     bot_responder.loop.run_until_complete(handler())

logging.info("starting bot responder")
bot_responder.run_until_disconnected()
