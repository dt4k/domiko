import os
import discord
import asyncio
#  http://discordpy.readthedocs.io/en/latest/
from lib import discord_helper

DISCORD_TOKEN = os.environ['DISCORD_TOKEN']
VOICE_CHATROOM_ID = os.environ['VOICE_CHATROOM_ID']
GENERAL_CHANNEL_ID = os.environ['GENERAL_CHANNEL_ID']

client = discord.Client()
helper = discord_helper.DiscordHelper(client, VOICE_CHATROOM_ID)

@client.event
async def on_ready():
    print('Process is launched. Logged in as %s(%s)' %
          (client.user.name, client.user.id))
    channel = client.get_channel(VOICE_CHATROOM_ID)
    # join to the voice channel
    await client.join_voice_channel(channel)
    print('joined to %s' % VOICE_CHATROOM_ID)
    await helper.speech('こんにちは！')
    while(True):
        print('start polling for status')
        if (await helper.get_game_status() in ('running', 'finished')) and await helper.is_hardware_connected():
            await helper.sitrep(client.get_channel(GENERAL_CHANNEL_ID))
        await asyncio.sleep(60)

@client.event
async def on_message(message):
    await helper.handle_message(message)

client.run(DISCORD_TOKEN)
